import tweepy
from textblob import TextBlob

consumer_key = 'YOUR KEY HERE'
consumer_secret = 'YOUR SECRET HERE'
access_token = 'YOUR TOKEN HERE'
access_token_secret = 'YOUR TOKEN SECRET HERE'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('twenty one pilots')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
	