"""
import sys
import tweepy
from tweepy.models import Status
import time
from sys import stdout

def getTweets(user):
	try:
		auth = tweepy.OAuthHandler('Zy0XiNaCGttJbbgzSCQCqB9uM', 'W56O2AoXtbOzbaZvzy9pKYkt8JBJwpq2pwYgwB16PGzzepSlh0') # get consumerkey, consumersecret at https://apps.twitter.com/
		auth.set_access_token('2802732985-htE2S85uKlrIIAnF0GrbQjBSTEM1b91agBJCHDQ', 'LgeaVntKYRKwtB57f4hOyjp14GaAmYKBkK8ivFjKAnBXy') # get accesstoken, accesstokensecret at https://apps.twitter.com/
		api = tweepy.API(auth)
		f = open("tweets.json", "w")
		count = 0
		for tweet in tweepy.Cursor(api.user_timeline, id=user).items():
			f.write(str(tweet) + "\n")
			count += 1
			if count >= 10:
				break
		f.close()
	except:
		print("Unexpected error:", sys.exc_info()[0])
		print("sleeping for a while")
		time.sleep(30)
	print("Done.")
"""
import sys
import tweepy
from tweepy.models import Status
import time
from sys import stdout

def getTweets(user):
	try:
		auth = tweepy.OAuthHandler('Zy0XiNaCGttJbbgzSCQCqB9uM', 'W56O2AoXtbOzbaZvzy9pKYkt8JBJwpq2pwYgwB16PGzzepSlh0') # get consumerkey, consumersecret at https://apps.twitter.com/
		auth.set_access_token('2802732985-htE2S85uKlrIIAnF0GrbQjBSTEM1b91agBJCHDQ', 'LgeaVntKYRKwtB57f4hOyjp14GaAmYKBkK8ivFjKAnBXy') # get accesstoken, accesstokensecret at https://apps.twitter.com/
		api = tweepy.API(auth)
		f = open("tweets.json", "w")
		count = 0
		for tweet in tweepy.Cursor(api.user_timeline, id=user, tweet_mode='extended').items():
			f.write(str(tweet.entities.get("hashtags")) + "\n" + str(tweet.entities.get("user_mentions")) + "\n")
			count += 1
			if count >= 200:
				break
		f.close()
	except:
		print("Unexpected error:", sys.exc_info()[0])
		print("sleeping for a while")
		time.sleep(30)
	print("Done.")
