import hashtags

company = input(print("Please enter the name of the company: "))
conference = input(print("Please enter the name of conference: "))

hashtags.analysis("tweet.json", company, conference)