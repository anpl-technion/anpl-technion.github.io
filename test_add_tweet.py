#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test script for add_tweet.py

Tests various scenarios:
1. Adding a tweet that is already displayed
2. Adding a tweet older than displayed tweets
3. Adding a tweet newer than all displayed tweets (normal case)
4. Fixing tweets in wrong chronological order
"""

import json
import sys
import os
from pathlib import Path
from datetime import datetime, timedelta

# Import the function we want to test
sys.path.insert(0, os.path.dirname(__file__))
from add_tweet import merge_and_filter_tweets


def create_test_tweet(tweet_id, account, text, days_ago=0):
    """Create a test tweet object"""
    created_at = (datetime.utcnow() - timedelta(days=days_ago)).strftime("%Y-%m-%dT%H:%M:%S.000Z")
    return {
        "id": str(tweet_id),
        "text": text,
        "created_at": created_at,
        "account": account,
        "handle": f"@{account}",
        "link": f"https://twitter.com/{account}/status/{tweet_id}"
    }


def setup_test_file(test_file, tweets):
    """Set up a test tweets.json file"""
    with open(test_file, 'w', encoding='utf-8') as f:
        json.dump(tweets, f, indent=2)


def read_test_file(test_file):
    """Read tweets from test file"""
    with open(test_file, 'r', encoding='utf-8') as f:
        return json.load(f)


def verify_order(tweets):
    """Verify tweets are in chronological order (newest first)"""
    for i in range(len(tweets) - 1):
        if tweets[i]['created_at'] < tweets[i + 1]['created_at']:
            return False, f"Out of order at position {i}: {tweets[i]['created_at']} < {tweets[i+1]['created_at']}"
    return True, "Order is correct"


def verify_top_4_per_account(tweets):
    """Verify we have at most 4 tweets per account"""
    anpl_count = sum(1 for t in tweets if t['account'] == 'ANPL_Technion')
    vadim_count = sum(1 for t in tweets if t['account'] == 'vadim_indelman')

    if anpl_count > 4:
        return False, f"Too many ANPL_Technion tweets: {anpl_count}"
    if vadim_count > 4:
        return False, f"Too many vadim_indelman tweets: {vadim_count}"

    return True, f"Counts OK: ANPL={anpl_count}, Vadim={vadim_count}"


def print_tweets(tweets, title="Tweets"):
    """Print tweets in a readable format"""
    print(f"\n{title}:")
    for i, tweet in enumerate(tweets, 1):
        date = tweet['created_at'][:10]
        print(f"  {i}. [{date}] @{tweet['account']} (ID: {tweet['id']}): {tweet['text'][:50]}...")


def run_test(test_name, initial_tweets, new_tweets, expected_conditions):
    """Run a single test case"""
    print(f"\n{'='*80}")
    print(f"TEST: {test_name}")
    print('='*80)

    # Create temporary test file
    test_file = "_data/tweets_test.json"

    # Setup initial state
    setup_test_file(test_file, initial_tweets)
    print_tweets(initial_tweets, "Initial tweets")
    print_tweets(new_tweets, "New tweets to add")

    # Run the merge
    result_tweets = merge_and_filter_tweets(new_tweets, test_file)

    # Verify results
    print("\n" + "-"*80)
    print("VERIFICATION:")

    all_passed = True

    # Check order
    order_ok, order_msg = verify_order(result_tweets)
    status = "✅" if order_ok else "❌"
    print(f"{status} Chronological order: {order_msg}")
    all_passed = all_passed and order_ok

    # Check top 4 per account
    count_ok, count_msg = verify_top_4_per_account(result_tweets)
    status = "✅" if count_ok else "❌"
    print(f"{status} Top 4 per account: {count_msg}")
    all_passed = all_passed and count_ok

    # Check custom conditions
    for condition_name, condition_func in expected_conditions.items():
        condition_ok, condition_msg = condition_func(result_tweets, initial_tweets, new_tweets)
        status = "✅" if condition_ok else "❌"
        print(f"{status} {condition_name}: {condition_msg}")
        all_passed = all_passed and condition_ok

    print_tweets(result_tweets, "\nFinal tweets")

    # Cleanup
    if os.path.exists(test_file):
        os.remove(test_file)

    return all_passed


def test_1_duplicate_tweet():
    """Test 1: Adding a tweet that is already displayed"""

    initial_tweets = [
        create_test_tweet(1001, "ANPL_Technion", "ANPL tweet 1", days_ago=1),
        create_test_tweet(1002, "ANPL_Technion", "ANPL tweet 2", days_ago=2),
        create_test_tweet(1003, "vadim_indelman", "Vadim tweet 1", days_ago=3),
        create_test_tweet(1004, "vadim_indelman", "Vadim tweet 2", days_ago=4),
    ]

    # Try to add an existing tweet (same ID)
    new_tweets = [
        create_test_tweet(1001, "ANPL_Technion", "ANPL tweet 1 UPDATED", days_ago=1),
    ]

    def check_no_duplicate(result, initial, new):
        # Should have same number of tweets (no duplicate added)
        ids = [t['id'] for t in result]
        if len(ids) != len(set(ids)):
            return False, "Duplicate IDs found"
        if len(result) != len(initial):
            return False, f"Tweet count changed: {len(initial)} -> {len(result)}"
        return True, "No duplicate added"

    return run_test(
        "Test 1: Adding a tweet that is already displayed",
        initial_tweets,
        new_tweets,
        {"No duplicates": check_no_duplicate}
    )


def test_2_older_tweet():
    """Test 2: Adding a tweet older than displayed tweets"""

    initial_tweets = [
        create_test_tweet(2001, "ANPL_Technion", "ANPL newest", days_ago=1),
        create_test_tweet(2002, "ANPL_Technion", "ANPL tweet 2", days_ago=2),
        create_test_tweet(2003, "ANPL_Technion", "ANPL tweet 3", days_ago=3),
        create_test_tweet(2004, "ANPL_Technion", "ANPL tweet 4", days_ago=4),
        create_test_tweet(2005, "vadim_indelman", "Vadim tweet 1", days_ago=5),
    ]

    # Add a very old tweet - should be ignored
    new_tweets = [
        create_test_tweet(2999, "ANPL_Technion", "ANPL very old tweet", days_ago=100),
    ]

    def check_old_tweet_ignored(result, initial, new):
        old_tweet_id = "2999"
        if any(t['id'] == old_tweet_id for t in result):
            return False, "Old tweet was added (should have been ignored)"
        # Count should still be correct
        anpl_tweets = [t for t in result if t['account'] == 'ANPL_Technion']
        if len(anpl_tweets) != 4:
            return False, f"Wrong ANPL count: {len(anpl_tweets)}"
        return True, "Old tweet correctly ignored"

    return run_test(
        "Test 2: Adding a tweet older than displayed tweets",
        initial_tweets,
        new_tweets,
        {"Old tweet ignored": check_old_tweet_ignored}
    )


def test_3_newer_tweet():
    """Test 3: Adding a tweet newer than all displayed tweets (normal case)"""

    initial_tweets = [
        create_test_tweet(3001, "ANPL_Technion", "ANPL tweet 1", days_ago=10),
        create_test_tweet(3002, "ANPL_Technion", "ANPL tweet 2", days_ago=20),
        create_test_tweet(3003, "vadim_indelman", "Vadim tweet 1", days_ago=15),
        create_test_tweet(3004, "vadim_indelman", "Vadim tweet 2", days_ago=25),
    ]

    # Add brand new tweets
    new_tweets = [
        create_test_tweet(3101, "ANPL_Technion", "ANPL NEWEST", days_ago=0),
        create_test_tweet(3102, "vadim_indelman", "Vadim NEWEST", days_ago=0),
    ]

    def check_newest_at_top(result, initial, new):
        # New tweets should be at the top
        if result[0]['id'] not in ['3101', '3102']:
            return False, f"Newest tweet not at top: {result[0]['id']}"
        if result[1]['id'] not in ['3101', '3102']:
            return False, f"Second newest not in top 2: {result[1]['id']}"
        return True, "Newest tweets at the top"

    def check_tweets_added(result, initial, new):
        if not any(t['id'] == '3101' for t in result):
            return False, "New ANPL tweet not added"
        if not any(t['id'] == '3102' for t in result):
            return False, "New Vadim tweet not added"
        return True, "New tweets successfully added"

    return run_test(
        "Test 3: Adding tweets newer than all displayed tweets",
        initial_tweets,
        new_tweets,
        {
            "Newest at top": check_newest_at_top,
            "Tweets added": check_tweets_added
        }
    )


def test_4_wrong_order():
    """Test 4: Tweets in wrong chronological order - verify it gets fixed"""

    # Initial tweets are intentionally in WRONG order
    initial_tweets = [
        create_test_tweet(4004, "vadim_indelman", "Vadim old", days_ago=40),  # Old but first
        create_test_tweet(4001, "ANPL_Technion", "ANPL newest", days_ago=1),  # Newest but not first
        create_test_tweet(4003, "vadim_indelman", "Vadim newer", days_ago=5),
        create_test_tweet(4002, "ANPL_Technion", "ANPL older", days_ago=20),
    ]

    # Don't add any new tweets, just reprocess existing ones
    new_tweets = []

    def check_order_fixed(result, initial, new):
        # Verify order is fixed
        for i in range(len(result) - 1):
            if result[i]['created_at'] < result[i + 1]['created_at']:
                return False, f"Still out of order at position {i}"

        # Newest should be first
        if result[0]['id'] != '4001':
            return False, f"Newest tweet (4001) not first, got {result[0]['id']}"

        return True, "Order successfully fixed"

    def check_all_tweets_preserved(result, initial, new):
        initial_ids = set(t['id'] for t in initial)
        result_ids = set(t['id'] for t in result)
        if initial_ids != result_ids:
            return False, f"Tweet IDs changed: {initial_ids} vs {result_ids}"
        return True, "All tweets preserved"

    return run_test(
        "Test 4: Fixing tweets in wrong chronological order",
        initial_tweets,
        new_tweets,
        {
            "Order fixed": check_order_fixed,
            "Tweets preserved": check_all_tweets_preserved
        }
    )


def test_5_mixed_scenario():
    """Test 5: Complex scenario with multiple changes"""

    initial_tweets = [
        create_test_tweet(5001, "ANPL_Technion", "ANPL 1", days_ago=5),
        create_test_tweet(5002, "ANPL_Technion", "ANPL 2", days_ago=10),
        create_test_tweet(5003, "ANPL_Technion", "ANPL 3", days_ago=15),
        create_test_tweet(5004, "ANPL_Technion", "ANPL 4", days_ago=20),
        create_test_tweet(5005, "ANPL_Technion", "ANPL 5 (should be removed)", days_ago=25),
        create_test_tweet(5006, "vadim_indelman", "Vadim 1", days_ago=8),
        create_test_tweet(5007, "vadim_indelman", "Vadim 2", days_ago=12),
    ]

    # Add new tweets including one that's older and one that's newer
    new_tweets = [
        create_test_tweet(5101, "ANPL_Technion", "ANPL BRAND NEW", days_ago=0),
        create_test_tweet(5102, "vadim_indelman", "Vadim NEW", days_ago=1),
        create_test_tweet(5103, "ANPL_Technion", "ANPL ancient (should be ignored)", days_ago=100),
    ]

    def check_limits_enforced(result, initial, new):
        anpl_count = sum(1 for t in result if t['account'] == 'ANPL_Technion')
        vadim_count = sum(1 for t in result if t['account'] == 'vadim_indelman')

        if anpl_count != 4:
            return False, f"ANPL count wrong: {anpl_count}"
        if vadim_count > 4:
            return False, f"Vadim count too high: {vadim_count}"

        # The oldest ANPL tweet (5005) should be gone
        if any(t['id'] == '5005' for t in result):
            return False, "Oldest ANPL tweet not removed"

        # Ancient tweet should not be present
        if any(t['id'] == '5103' for t in result):
            return False, "Ancient tweet was added"

        return True, "Limits correctly enforced"

    def check_new_tweets_added(result, initial, new):
        if not any(t['id'] == '5101' for t in result):
            return False, "New ANPL tweet not added"
        if not any(t['id'] == '5102' for t in result):
            return False, "New Vadim tweet not added"
        return True, "New tweets added correctly"

    return run_test(
        "Test 5: Complex mixed scenario",
        initial_tweets,
        new_tweets,
        {
            "Limits enforced": check_limits_enforced,
            "New tweets added": check_new_tweets_added
        }
    )


def main():
    """Run all tests"""
    print("="*80)
    print("RUNNING COMPREHENSIVE TESTS FOR add_tweet.py")
    print("="*80)

    # Create _data directory if it doesn't exist
    os.makedirs("_data", exist_ok=True)

    tests = [
        test_1_duplicate_tweet,
        test_2_older_tweet,
        test_3_newer_tweet,
        test_4_wrong_order,
        test_5_mixed_scenario,
    ]

    results = []
    for test_func in tests:
        passed = test_func()
        results.append((test_func.__name__, passed))

    # Print summary
    print("\n" + "="*80)
    print("TEST SUMMARY")
    print("="*80)

    for test_name, passed in results:
        status = "✅ PASSED" if passed else "❌ FAILED"
        print(f"{status}: {test_name}")

    total_passed = sum(1 for _, passed in results if passed)
    total_tests = len(results)

    print(f"\n{total_passed}/{total_tests} tests passed")

    if total_passed == total_tests:
        print("\n🎉 All tests passed!")
        return 0
    else:
        print("\n⚠️  Some tests failed")
        return 1


if __name__ == "__main__":
    sys.exit(main())
