const axios = require('axios');
const fs = require('fs');

async function fetchTwitterAPI() {
  // Note: You'll need to set these environment variables or replace with actual tokens
  const bearerTokens = {
    'ANPL_Technion': process.env.TWITTER_BEARER_TOKEN_ANPL || 'YOUR_ANPL_TOKEN_HERE',
    'vadim_indelman': process.env.TWITTER_BEARER_TOKEN_VADIM || 'YOUR_VADIM_TOKEN_HERE'
  };
  
  console.log('🔍 Checking bearer tokens...');
  if (!process.env.TWITTER_BEARER_TOKEN_ANPL) {
    console.log('❌ TWITTER_BEARER_TOKEN_ANPL not found in environment');
  }
  if (!process.env.TWITTER_BEARER_TOKEN_VADIM) {
    console.log('❌ TWITTER_BEARER_TOKEN_VADIM not found in environment');
  }
  
  if (!process.env.TWITTER_BEARER_TOKEN_ANPL && !process.env.TWITTER_BEARER_TOKEN_VADIM) {
    console.log('\n💡 To run this script, you need to set environment variables:');
    console.log('export TWITTER_BEARER_TOKEN_ANPL="your_token_here"');
    console.log('export TWITTER_BEARER_TOKEN_VADIM="your_token_here"');
    console.log('\nTokens can be found in GitHub repository secrets or Twitter Developer Portal');
    return;
  }
  
  const accounts = ['ANPL_Technion', 'vadim_indelman'];
  let allTweets = [];
  
  for (const username of accounts) {
    const bearerToken = bearerTokens[username];
    
    if (!bearerToken || bearerToken.includes('YOUR_') || bearerToken === '') {
      console.log(`⚠️ Skipping @${username} - no valid bearer token`);
      continue;
    }
    
    try {
      console.log(`\n🐦 Fetching tweets for @${username}...`);
      
      // First get user ID
      const userResponse = await axios.get(
        `https://api.twitter.com/2/users/by/username/${username}`,
        {
          headers: {
            'Authorization': `Bearer ${bearerToken}`,
            'Content-Type': 'application/json',
          }
        }
      );
      
      const userId = userResponse.data.data.id;
      console.log(`✅ Got user ID for @${username}: ${userId}`);
      
      // Get recent tweets
      const tweetsResponse = await axios.get(
        `https://api.twitter.com/2/users/${userId}/tweets`,
        {
          headers: {
            'Authorization': `Bearer ${bearerToken}`,
            'Content-Type': 'application/json',
          },
          params: {
            'max_results': 5,
            'tweet.fields': 'created_at,public_metrics,entities',
            'expansions': 'attachments.media_keys',
            'media.fields': 'url,preview_image_url,type',
            'exclude': 'retweets,replies'
          }
        }
      );
      
      if (tweetsResponse.data.data) {
        const mediaMap = {};
        if (tweetsResponse.data.includes && tweetsResponse.data.includes.media) {
          tweetsResponse.data.includes.media.forEach(media => {
            mediaMap[media.media_key] = media;
          });
        }
        
        const tweets = tweetsResponse.data.data.slice(0, 4).map(tweet => {
          const tweetData = {
            id: tweet.id,
            text: tweet.text,
            created_at: tweet.created_at,
            account: username,
            handle: `@${username}`,
            link: `https://twitter.com/${username}/status/${tweet.id}`
          };
          
          // Add expanded URLs
          if (tweet.entities && tweet.entities.urls) {
            tweetData.urls = tweet.entities.urls.map(url => ({
              display_url: url.display_url,
              expanded_url: url.expanded_url,
              url: url.url
            }));
          }
          
          // Add media attachments
          if (tweet.attachments && tweet.attachments.media_keys) {
            tweetData.media = tweet.attachments.media_keys.map(key => mediaMap[key]).filter(Boolean);
          }
          
          return tweetData;
        });
        
        allTweets.push(...tweets);
        console.log(`✅ Fetched ${tweets.length} tweets for @${username}`);
        tweets.forEach((tweet, i) => {
          const date = new Date(tweet.created_at).toLocaleString('en-US', {timeZone: 'UTC'});
          console.log(`   ${i+1}. ${date}: ${tweet.text.substring(0, 80)}...`);
        });
      } else {
        console.log(`❌ No tweets found for @${username}`);
      }
      
    } catch (error) {
      console.error(`❌ Error fetching tweets for @${username}:`);
      if (error.response) {
        console.error(`   Status: ${error.response.status}`);
        console.error(`   Response:`, JSON.stringify(error.response.data, null, 2));
      } else {
        console.error(`   Message: ${error.message}`);
      }
    }
  }
  
  if (allTweets.length > 0) {
    // Sort by creation date (newest first)
    allTweets.sort((a, b) => new Date(b.created_at) - new Date(a.created_at));
    
    console.log(`\n🔄 Final sorted tweet list (${allTweets.length} total):`);
    allTweets.forEach((tweet, i) => {
      const date = new Date(tweet.created_at).toLocaleString('en-US', {timeZone: 'UTC'});
      console.log(`   ${i+1}. [${tweet.account}] ${date}: ${tweet.text.substring(0, 80)}...`);
    });
    
    // Write to file
    fs.writeFileSync('_data/tweets.json', JSON.stringify(allTweets, null, 2));
    console.log(`\n✅ Successfully updated _data/tweets.json with ${allTweets.length} tweets!`);
  } else {
    console.log('\n❌ No tweets fetched, keeping existing data');
  }
}

fetchTwitterAPI().catch(console.error);