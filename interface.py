import ml
import tweet_user_crawler

conference = input("Please enter the name of conference: ")
company = input("Please enter the name of conference: ")

tweet_user_crawler.getTweets(company)
print(ml.flag(conference))
