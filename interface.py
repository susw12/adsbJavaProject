import ml
import tweet_user_crawler

company = input("Please enter the twitter handle of the company: ")
conference = input("Please enter the twitter handle of the conference: ")

print("Getting tweets from @" + company + " ...   ", end="")
tweet_user_crawler.getTweets(company)
print("Evaluating relationship between @" + company + " and @" + conference + " ...   ", end="")
ml.flag(conference, company) 
