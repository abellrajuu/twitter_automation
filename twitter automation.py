import tweepy
import time
import random

# Credentials
api_key = "INSERT API KEY HERE"
api_secret = "INSERT SECRET API KEY HERE"
bearer_token = "INSERT BEARER TOKEN HERE"
access_token = "INSERT ACCESS TOKEN HERE"
access_token_secret = "INSERT SECRET ACCESS TOKEN HERE"

# Gaining access and connecting to Twitter API using Credentials
client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)

# Creating API instance for Twitter API V1 features
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Function to like, retweet, and comment on tweets
def engage_with_tweets():
    query = "#example"  # Change to your desired hashtag or keyword
    tweets = client.search_recent_tweets(query=query, max_results=10)

    for tweet in tweets.data:
        try:
            api.create_favorite(tweet.id)
            print(f"Liked tweet by @{tweet.author_id}")

            api.retweet(tweet.id)
            print(f"Retweeted tweet by @{tweet.author_id}")

            comment = "Great post!"
            api.update_status(status=comment, in_reply_to_status_id=tweet.id, auto_populate_reply_metadata=True)
            print(f"Commented on tweet by @{tweet.author_id}")

            time.sleep(random.randint(10, 30))

        except Exception as e:
            print(f"An error occurred: {e}")

# Main loop to run the bot every hour
while True:
    engage_with_tweets()
    time.sleep(3600)
