const axios = require('axios');

async function debugTwitterAPI() {
  // Note: This is a debug script - actual tokens would come from environment variables
  console.log('Debug script for Twitter API issues');
  
  const username = 'ANPL_Technion';
  
  try {
    console.log(`\n=== Debugging @${username} tweets ===`);
    
    // This would need actual bearer token from environment
    const bearerToken = process.env.TWITTER_BEARER_TOKEN_ANPL;
    
    if (!bearerToken) {
      console.log('❌ No bearer token found in environment variables');
      console.log('This script needs TWITTER_BEARER_TOKEN_ANPL to be set');
      return;
    }
    
    // Get user ID
    console.log('1. Getting user ID...');
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
    console.log(`✅ User ID: ${userId}`);
    
    // Test different API calls to see what we get
    const testConfigs = [
      {
        name: 'Current workflow config (excludes retweets/replies)',
        params: {
          'max_results': 5,
          'tweet.fields': 'created_at,public_metrics,entities',
          'expansions': 'attachments.media_keys',
          'media.fields': 'url,preview_image_url,type',
          'exclude': 'retweets,replies'
        }
      },
      {
        name: 'Include all tweets (no exclusions)',
        params: {
          'max_results': 10,
          'tweet.fields': 'created_at,public_metrics,entities',
          'expansions': 'attachments.media_keys',
          'media.fields': 'url,preview_image_url,type'
        }
      },
      {
        name: 'Recent tweets with minimal fields',
        params: {
          'max_results': 10,
          'tweet.fields': 'created_at'
        }
      }
    ];
    
    for (const config of testConfigs) {
      console.log(`\n2. Testing: ${config.name}`);
      try {
        const tweetsResponse = await axios.get(
          `https://api.twitter.com/2/users/${userId}/tweets`,
          {
            headers: {
              'Authorization': `Bearer ${bearerToken}`,
              'Content-Type': 'application/json',
            },
            params: config.params
          }
        );
        
        if (tweetsResponse.data.data) {
          console.log(`✅ Found ${tweetsResponse.data.data.length} tweets:`);
          tweetsResponse.data.data.forEach((tweet, index) => {
            const date = new Date(tweet.created_at).toLocaleDateString();
            console.log(`   ${index + 1}. ${date}: ${tweet.text.substring(0, 100)}...`);
          });
        } else {
          console.log('❌ No tweets found');
          console.log('Response:', JSON.stringify(tweetsResponse.data, null, 2));
        }
      } catch (error) {
        console.log(`❌ Error: ${error.response?.data?.title || error.message}`);
        if (error.response?.data) {
          console.log('API Error details:', JSON.stringify(error.response.data, null, 2));
        }
      }
    }
    
  } catch (error) {
    console.error('❌ Error getting user ID:', error.response?.data || error.message);
  }
}

debugTwitterAPI();