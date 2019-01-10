import ml
import tweet_user_crawler
import sys

hello = sys.argv

company = hello[1]
conference = hello[2]

print("Getting tweets from @" + company + " ...   ", end="")
tweet_user_crawler.getTweets(company)
print("Evaluating relationship between @" + company + " and @" + conference + " ...   ", end="")
ml.flag(conference, company)  


