import sys
import tweepy
import simplejson as json
from tweepy.models import Status
import time
from sys import stdout

try:
	f = open("user.txt", "r")
	us = f.readline()
	f.close()

	auth = tweepy.OAuthHandler('Zy0XiNaCGttJbbgzSCQCqB9uM', 'W56O2AoXtbOzbaZvzy9pKYkt8JBJwpq2pwYgwB16PGzzepSlh0') # get consumerkey, consumersecret at https://apps.twitter.com/
	auth.set_access_token('2802732985-htE2S85uKlrIIAnF0GrbQjBSTEM1b91agBJCHDQ', 'LgeaVntKYRKwtB57f4hOyjp14GaAmYKBkK8ivFjKAnBXy') # get accesstoken, accesstokensecret at https://apps.twitter.com/
	api = tweepy.API(auth)
	f = open("tweets.json", "w")
	count = 0
	for tweet in tweepy.Cursor(api.user_timeline, id=us).items():
		f.write(str(tweet) + "\n")
		count += 1
		if count > 50000:
			break
	f.close()
except:
	print("Unexpected error:", sys.exc_info()[0])
	print("sleeping for a while")
	time.sleep(30)
print("fun")