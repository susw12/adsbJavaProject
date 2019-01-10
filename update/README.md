User-Organization Relationships

To execute this program, run the interface.py program. This requires Python 3.5+ and the tweepy library, so make sure to have them installed. 
The program prompts the user for a conference and a company name. It then gets 5000 tweets from the company (using tweet_user_crawler.py) and looks through them to find any hashtags or mentions of the conference (using ml.py). 
The number of found hashtags and mentions are compared to the average hashtags and mentions, obtained through training the program with many test cases. If the number passes a threshold (1.5), a relationship is established between the conference and company.
The program outputs 
