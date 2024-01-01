import tweepy
from textblob import textblob

consumer_key = oDHdShdOECAnglZUKxOew8Zjk
consumer_secret = wBXaQ56HGNrwA0up2NYaAQ643G0U5E6L1t6oxQN1wFatymAn1K

access_token =  1688661168624168960-tS9l6OKtVrATrCekMQ8a7S47NtQIlB
access_token_secret = UAOt1uQFb1V8Nsi5SEqxitZzYWgbgeRowcqI99t55cVmT

auth = tweepy.OAuth1UserHandler (consumer_key, consumer_secret=)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

for tweet in public_tweets:
     print(tweet.text)
     analysis= TextBlob(tweet.text)
     print(analysis.sentment)


