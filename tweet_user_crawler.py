import sys
import tweepy
import simplejson as json
from tweepy.models import Status
import time
from sys import stdout

tempData = []
totalTweets=0

def readFilelines(fileName):
	f=open(fileName,"r")
	lines=f.readlines()
	f.close()
	return lines

def my_on_data(data):
	#global filename, tweetcount
	global tempData
	global totalTweets
	tempData.append(data.strip() + "\n")
	stdout.write("\r%d-%d" % (totalTweets,len(tempData)))
	stdout.flush()
	if len(tempData) == 1000:
		totalTweets=totalTweets+1000
		fileIndex=totalTweets/62000
		f = open("incoming-"+str(fileIndex), 'a')
		content = ''.join(tempData)
		f.write(content)
		f.close()
		tempData = []    

def my_on_error(status_code):
    print 'Error: ', str(status_code)

def main():
 while True:
    try:
	#amiri
		kw=[]		
		kw=readFilelines("keywords.txt")
		us=[]		
		us=readFilelines("users.txt")
		print "".join(kw)
		print "".join(us)
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
		print "Unexpected error:", sys.exc_info()[0]
		print "sleeping for a while"
		time.sleep(30)
		continue

if __name__ == '__main__':
	tempData = []
	totalTweets=0
	main()
