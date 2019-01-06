import ml

company = input("Please enter the name of the company: ")
conference = input("Please enter the name of conference: ")

ml.analysis("tweet.json", company, conference)