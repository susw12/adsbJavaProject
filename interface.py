import ml
import tweet_user_crawler
import sys

variables = sys.argv

company = variables[1]
conferenceHashtag = variables[2]
conferenceHandle = variables[3]

print("Getting tweets from @" + company + " ...   ", end="")
tweet_user_crawler.getTweets(company)
print("Evaluating relationship between @" + company + " and @" + conferenceHandle + " or #" + conferenceHashtag + " ...")
ml.flag(conferenceHashtag, conferenceHandle, company)  


