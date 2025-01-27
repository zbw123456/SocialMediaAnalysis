import os
import tweepy
from textblob import TextBlob
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv

# Load API credentials
load_dotenv()
bearer_token = os.getenv('TWITTER_BEARER_TOKEN')

# Authenticate with Twitter API
client = tweepy.Client(bearer_token=bearer_token)

# Fetch tweets with hashtag #football
query = '#football'
tweets = client.search_recent_tweets(query=query, max_results=100)

# Perform sentiment analysis
sentiments = [TextBlob(tweet.text).sentiment.polarity for tweet in tweets.data]

# Save results to a CSV file
df = pd.DataFrame({'Tweet': [tweet.text for tweet in tweets.data], 'Sentiment': sentiments})
df.to_csv('outputs/sentiment_results.csv', index=False)

# Plot sentiment distribution
plt.hist(sentiments, bins=20, color='blue')
plt.title('Sentiment Distribution of #football Tweets')
plt.xlabel('Sentiment Polarity')
plt.ylabel('Frequency')
plt.savefig('visuals/sentiment_distribution.png')
plt.show()
