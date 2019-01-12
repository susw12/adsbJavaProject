User-Organization Relationships

To execute this program, run the RUNME.class program. This can be done by using the function "java RUNME". This requires Python 3.5+ and the tweepy library, so make sure to have them installed. The program prompts the user for a user twitter handle as well as a hashtag and handle of another user to look for. It then gets 5000 tweets from the user (using tweet_user_crawler.py) and looks through them to find any of the inputted hashtags or mentions (using ml.py). 
The number of found hashtags and mentions are compared to the average hashtags and mentions, obtained through training the program with many test cases (other twitter users). If the number (representing the correlation) passes a threshold, a relationship is established between the user and the result is outputted. The number of tweets analyzed and number of hashtags and mentions are also printed out.

Default averages were tested by analyzing 5000 tweets from each of the following twitter users:
lgus
adobe
sony
samsung
google
microsoft
intel
ces
amd
qualcomm
msitweets
razer
nvidia
radeon
asus
coolermaster
corsair
teamevga
