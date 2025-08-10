const axios = require('axios');

// Test script to check Twitter API status without bearer tokens
async function testTwitterAPI() {
  const accounts = ['ANPL_Technion', 'vadim_indelman'];
  
  console.log('🔍 Testing Twitter API access (without authentication)...\n');
  
  for (const username of accounts) {
    try {
      console.log(`Testing @${username}:`);
      
      // Test without authentication to see what error we get
      const response = await axios.get(
        `https://api.twitter.com/2/users/by/username/${username}`,
        {
          headers: {
            'Content-Type': 'application/json',
          },
          validateStatus: () => true // Don't throw on HTTP errors
        }
      );
      
      console.log(`  Status: ${response.status}`);
      console.log(`  Response:`, JSON.stringify(response.data, null, 2));
      
    } catch (error) {
      console.log(`  Error: ${error.message}`);
    }
    console.log('');
  }
  
  console.log('Expected errors:');
  console.log('- 401 Unauthorized: Missing/invalid bearer token (normal without auth)');
  console.log('- 403 Forbidden: Account suspended/private');
  console.log('- 404 Not Found: Account doesn\'t exist');
  console.log('- 429 Too Many Requests: Rate limited');
}

testTwitterAPI();