# How to Add Tweets Using add_tweet.py

The `add_tweet.py` script automatically fetches tweet data and manages the tweets displayed on your website.

## Features

- Accepts multiple tweet URLs as input
- Automatically extracts account name, tweet ID, and text from tweets
- Merges with existing tweets in `tweets.json`
- Keeps only the **top 4 tweets** for each account (ANPL_Technion and vadim_indelman)
- Automatically sorts by date (newest first)
- Older tweets are automatically removed if they're not in the top 4

## Usage

```bash
python add_tweet.py <tweet_url1> [tweet_url2] [tweet_url3] ...
```

## Examples

### Add a single tweet:
```bash
python add_tweet.py https://twitter.com/ANPL_Technion/status/1987151270092664853
```

### Add multiple tweets at once:
```bash
python add_tweet.py \
  https://twitter.com/ANPL_Technion/status/1987151270092664853 \
  https://twitter.com/vadim_indelman/status/1234567890123456789 \
  https://twitter.com/ANPL_Technion/status/1982887936183156917
```

### Works with both twitter.com and x.com:
```bash
python add_tweet.py https://x.com/ANPL_Technion/status/1987151270092664853
```

## Interactive Process

For each tweet URL, the script will:

1. **Automatically fetch** tweet data using Twitter's public oEmbed API
2. **Extract tweet text** from the fetched data
3. **Prompt for creation date**:
   ```
   Enter creation date (ISO format, e.g., 2025-11-08T13:32:36.000Z):
   >
   ```
   - Press Enter to use current time
   - Or enter the actual tweet date in ISO format

4. **Prompt for URLs** (if t.co links are found in tweet):
   ```
   Found 1 URL(s) in tweet. Enter expanded URLs:
     For https://t.co/m6e3MtMxyi:
       Display URL (or Enter to skip): arxiv.org/abs/2509.10162
       Expanded URL: https://arxiv.org/abs/2509.10162
   ```

## Example Session

```bash
$ python add_tweet.py https://twitter.com/ANPL_Technion/status/1987151270092664853

Processing 1 tweet(s)...

Fetching tweet data from: https://twitter.com/ANPL_Technion/status/1987151270092664853
  Enter creation date (ISO format, e.g., 2025-11-08T13:32:36.000Z):
  > 2025-11-08T13:32:36.000Z
  Found 1 URL(s) in tweet. Enter expanded URLs:
    For https://t.co/m6e3MtMxyi:
      Display URL (or Enter to skip): arxiv.org/abs/2509.10162
      Expanded URL: https://arxiv.org/abs/2509.10162
  ✅ Successfully fetched tweet 1987151270092664853 from @ANPL_Technion

✅ Successfully updated _data/tweets.json
   Total tweets: 8
   ANPL_Technion: 4
   vadim_indelman: 4

📋 Final tweet list:
   1. [2025-11-08] @ANPL_Technion: The paper "Online Robust Planning under Model Uncertainty...
   2. [2025-10-27] @ANPL_Technion: The paper "Online POMDP Planning with Anytime Determini...
   3. [2025-09-15] @ANPL_Technion: A preprint entitled "Online Robust Planning under Mode...
   4. [2025-09-04] @vadim_indelman: Today was the PhD ceremony at the Technion, and I'm t...
   5. [2025-08-28] @ANPL_Technion: The paper "Anytime Probabilistically Constrained Prov...
   6. [2025-05-29] @vadim_indelman: 🚀 Happy to share my recent Robotics Seminar presenta...
   7. [2025-05-16] @vadim_indelman: Had a great time visiting MIT and delivering a robo...
   8. [2025-04-28] @vadim_indelman: An MSc seminar by Ron Benchetrit on "Anytime Increm...
```

## How It Works

1. **Fetches tweet data**: Uses Twitter's public oEmbed API to get tweet information
2. **Extracts account and ID**: Automatically detects if it's from ANPL_Technion or vadim_indelman
3. **Merges with existing tweets**: Reads `_data/tweets.json` and adds new tweets
4. **Removes duplicates**: If a tweet ID already exists, it updates the data
5. **Filters to top 4 per account**:
   - Keeps 4 newest ANPL_Technion tweets
   - Keeps 4 newest vadim_indelman tweets
   - Older tweets are automatically removed
6. **Sorts by date**: Final list is sorted with newest tweets first
7. **Saves back to file**: Updates `_data/tweets.json`

## After Adding

1. The tweets are automatically managed (only top 4 per account)
2. Rebuild the site to see changes:
   ```bash
   bundle exec jekyll build
   ```
3. Commit the updated `_data/tweets.json`:
   ```bash
   git add _data/tweets.json
   git commit -m "Update tweets"
   git push
   ```

## Troubleshooting

### If automatic fetching fails:
The script will fall back to manual input where you can type/paste the tweet text.

### If you need to bypass the prompts:
You can pre-populate the tweet data in the JSON file manually if needed.

## Notes

- Only tweets from `ANPL_Technion` and `vadim_indelman` are kept
- Maximum 4 tweets per account will be displayed
- The script uses Twitter's **public oEmbed API** (no authentication required)
- Both `twitter.com` and `x.com` URLs are supported
