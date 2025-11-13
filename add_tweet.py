#!/usr/bin/env python3
"""
Script to add tweets to tweets.json and keep only top 4 per account

Usage:
    python add_tweet.py <tweet_link1> [tweet_link2] [tweet_link3] ...

Example:
    python add_tweet.py https://twitter.com/ANPL_Technion/status/1234567890 https://twitter.com/vadim_indelman/status/9876543210

The script will:
1. Fetch tweet data from the provided URLs
2. Merge with existing tweets in tweets.json
3. Keep only the top 4 tweets for ANPL_Technion and top 4 for vadim_indelman
4. Sort by date (newest first)
"""

import json
import sys
import re
import urllib.request
import urllib.parse
from datetime import datetime
from pathlib import Path
from html.parser import HTMLParser


class TwitterHTMLParser(HTMLParser):
    """Parse tweet HTML to extract text content"""
    def __init__(self):
        super().__init__()
        self.text_parts = []
        self.in_blockquote = False

    def handle_starttag(self, tag, attrs):
        if tag == 'blockquote':
            self.in_blockquote = True

    def handle_endtag(self, tag):
        if tag == 'blockquote':
            self.in_blockquote = False

    def handle_data(self, data):
        if self.in_blockquote:
            stripped = data.strip()
            if stripped and stripped not in ['—', '&mdash;']:
                self.text_parts.append(stripped)

    def get_text(self):
        # Remove the last part which is usually "— @username"
        if self.text_parts and self.text_parts[-1].startswith('—'):
            self.text_parts.pop()
        return '\n'.join(self.text_parts).strip()


def extract_tweet_info(tweet_link):
    """Extract tweet ID and account name from Twitter URL"""
    # Handle both twitter.com and x.com
    match = re.search(r'(?:twitter\.com|x\.com)/([^/]+)/status/(\d+)', tweet_link)
    if match:
        account = match.group(1)
        tweet_id = match.group(2)
        return account, tweet_id
    else:
        raise ValueError(f"Could not extract tweet info from link: {tweet_link}")


def fetch_tweet_data(tweet_link):
    """Fetch tweet data using Twitter's oEmbed API"""
    print(f"Fetching tweet data from: {tweet_link}")

    try:
        account, tweet_id = extract_tweet_info(tweet_link)
    except ValueError as e:
        print(f"  ❌ Error: {e}")
        return None

    # Normalize the link
    normalized_link = f"https://twitter.com/{account}/status/{tweet_id}"

    try:
        # Use Twitter's public oEmbed API
        oembed_url = f"https://publish.twitter.com/oembed?url={urllib.parse.quote(normalized_link)}&omit_script=true"

        with urllib.request.urlopen(oembed_url) as response:
            data = json.loads(response.read().decode())

        # Parse the HTML to extract tweet text
        parser = TwitterHTMLParser()
        parser.feed(data.get('html', ''))
        tweet_text = parser.get_text()

        if not tweet_text:
            print(f"  ⚠️  Could not extract tweet text from HTML")
            print(f"  Please enter tweet text manually:")
            tweet_text = input("  > ").strip()

        # Ask for creation date
        print(f"  Enter creation date (ISO format, e.g., 2025-11-08T13:32:36.000Z):")
        created_at = input("  > ").strip()

        if not created_at:
            created_at = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.000Z")
            print(f"  Using current time: {created_at}")

        # Extract URLs from tweet text (t.co links)
        urls = []
        url_pattern = r'https://t\.co/\w+'
        tco_urls = re.findall(url_pattern, tweet_text)

        if tco_urls:
            print(f"  Found {len(tco_urls)} URL(s) in tweet. Enter expanded URLs:")
            for tco_url in tco_urls:
                print(f"    For {tco_url}:")
                display = input(f"      Display URL (or Enter to skip): ").strip()
                if display:
                    expanded = input(f"      Expanded URL: ").strip() or tco_url
                    urls.append({
                        "display_url": display,
                        "expanded_url": expanded,
                        "url": tco_url
                    })

        tweet = {
            "id": tweet_id,
            "text": tweet_text,
            "created_at": created_at,
            "account": account,
            "handle": f"@{account}",
            "link": normalized_link
        }

        if urls:
            tweet["urls"] = urls

        print(f"  ✅ Successfully fetched tweet {tweet_id} from @{account}")
        return tweet

    except Exception as e:
        print(f"  ❌ Error fetching tweet: {e}")
        print(f"  Falling back to manual input...")
        return fetch_tweet_manually(account, tweet_id, normalized_link)


def fetch_tweet_manually(account, tweet_id, tweet_link):
    """Manually input tweet data"""
    print(f"\nManual input for tweet {tweet_id} from @{account}")

    print("Enter tweet text (end with Ctrl+D on Unix or Ctrl+Z on Windows):")
    tweet_lines = []
    try:
        while True:
            line = input()
            tweet_lines.append(line)
    except EOFError:
        pass

    tweet_text = '\n'.join(tweet_lines).strip()

    if not tweet_text:
        print("  ❌ Tweet text cannot be empty")
        return None

    print("Enter creation date (ISO format, e.g., 2025-11-08T13:32:36.000Z):")
    created_at = input().strip()

    if not created_at:
        created_at = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.000Z")

    tweet = {
        "id": tweet_id,
        "text": tweet_text,
        "created_at": created_at,
        "account": account,
        "handle": f"@{account}",
        "link": tweet_link
    }

    return tweet


def merge_and_filter_tweets(new_tweets, json_path="_data/tweets.json"):
    """Merge new tweets with existing ones and keep top 4 per account"""

    json_file = Path(json_path)

    # Read existing tweets
    if json_file.exists():
        with open(json_file, 'r', encoding='utf-8') as f:
            existing_tweets = json.load(f)
    else:
        existing_tweets = []

    # Create a dictionary of tweets by ID to avoid duplicates
    all_tweets_dict = {t['id']: t for t in existing_tweets}

    # Add/update with new tweets
    for tweet in new_tweets:
        if tweet:
            all_tweets_dict[tweet['id']] = tweet

    # Convert back to list
    all_tweets = list(all_tweets_dict.values())

    # Sort by creation date (newest first)
    all_tweets.sort(key=lambda t: t['created_at'], reverse=True)

    # Filter to keep only top 4 per account
    anpl_tweets = [t for t in all_tweets if t['account'] == 'ANPL_Technion'][:4]
    vadim_tweets = [t for t in all_tweets if t['account'] == 'vadim_indelman'][:4]

    # Combine and sort again
    final_tweets = anpl_tweets + vadim_tweets
    final_tweets.sort(key=lambda t: t['created_at'], reverse=True)

    # Write back to file
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(final_tweets, f, indent=2, ensure_ascii=False)

    print(f"\n✅ Successfully updated {json_path}")
    print(f"   Total tweets: {len(final_tweets)}")
    print(f"   ANPL_Technion: {len(anpl_tweets)}")
    print(f"   vadim_indelman: {len(vadim_tweets)}")

    print("\n📋 Final tweet list:")
    for i, tweet in enumerate(final_tweets, 1):
        date = tweet['created_at'][:10]
        preview = tweet['text'][:60].replace('\n', ' ')
        print(f"   {i}. [{date}] @{tweet['account']}: {preview}...")

    return final_tweets


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    tweet_links = sys.argv[1:]

    # Validate all links
    for link in tweet_links:
        if not re.search(r'twitter\.com|x\.com', link):
            print(f"Error: Invalid Twitter/X link: {link}")
            sys.exit(1)

    print(f"Processing {len(tweet_links)} tweet(s)...\n")

    # Fetch all tweets
    new_tweets = []
    for link in tweet_links:
        tweet = fetch_tweet_data(link)
        if tweet:
            new_tweets.append(tweet)
        print()

    if not new_tweets:
        print("❌ No tweets were successfully fetched")
        sys.exit(1)

    # Merge and filter
    merge_and_filter_tweets(new_tweets)


if __name__ == "__main__":
    main()
