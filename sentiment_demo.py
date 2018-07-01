import tweepy
from textblob import TextBlob

#Enter Twitter API credentials
consumer_key = 'YOUR KEY HERE'
consumer_secret = 'YOUR SECRET HERE'
access_token = 'YOUR TOKEN HERE'
access_token_secret = 'YOUR TOKEN SECRET HERE'

#Use Twitter credentials to access tweets
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#Set topic you want to search for. In this case, Twenty One Pilots
public_tweets = api.search('twenty one pilots')

#Iterate through public tweets, print them, and 
#return the polarity and subjectiity values
for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
	