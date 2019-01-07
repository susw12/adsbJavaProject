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

<<<<<<< HEAD
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
=======
def main():
 while True:
    try:
	#amiri
		kw=[]		
		kw=readFilelines("keywords.txt")
		us=[]		
		us=readFilelines("users.txt")
		print ("\n".join(kw))
		print ("\n".join(us))
		auth = tweepy.OAuthHandler('Zy0XiNaCGttJbbgzSCQCqB9uM', 'W56O2AoXtbOzbaZvzy9pKYkt8JBJwpq2pwYgwB16PGzzepSlh0') # get consumerkey, consumersecret at https://apps.twitter.com/
		auth.set_access_token('2802732985-htE2S85uKlrIIAnF0GrbQjBSTEM1b91agBJCHDQ', 'LgeaVntKYRKwtB57f4hOyjp14GaAmYKBkK8ivFjKAnBXy') # get accesstoken, accesstokensecret at https://apps.twitter.com/
		api = tweepy.API(auth)
		streamlistener = tweepy.StreamListener(api)
		streamlistener.on_data = my_on_data
		streamlistener.on_error = my_on_error
		stream = tweepy.Stream(auth, listener=streamlistener, secure=True)
		stream.filter(track=kw,follow=us)
		#stream.filter(track=['notonus'])

		#tweetcount = 0
		#filename = gen_file_name()
		
		stream.sample()
    except:
        #f = open(filename + '.unlock', 'w')
        #f.close()
        #filename = gen_file_name()
		print ("Unexpected error:", sys.exc_info()[0])
		print ("sleeping for a while")
		time.sleep(30)
		continue

if __name__ == '__main__':
	tempData = []
	totalTweets=0
	main()
>>>>>>> master
