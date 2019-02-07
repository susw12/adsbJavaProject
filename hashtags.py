##This is ml.py made to work for jsons
##Bumjin Joo
##January 3rd, 2019

import json

f = open("flag.txt", "r")
name = f.readline()
f.close()

#all tweets
##fileAll = open("tweet.json", "r")
##line = fileAll.readline(s)
##lineNum = len(lines)
##fileAll.close()
##
##tweets = open("tweet.json", "r")
##
##hashtags = []
##for num in range(lineNum):
##    #load should be loads if the file is a .txt
##    line = tweets.readline()
##    jsonTweet = json.load(line)
##    hashtags += jsonTweet["hashtag"]
##    
##tweets.close()
# Testing
#1 tweet
def analysis(file, user, name):
    #get hashtags
    file = open(file, "r")
    tweetLine = file.readline()
    jsonTweet = json.load(tweetLine)
    hashtags = jsonTweet["hashtags"]
    file.close()

    #get mentions
    f = open("tweet.json", "r")
    line = f.readline()
    jsonTweet = json.load(line)
    mentions = jsonTweet["user_mentions"] 
    f.close()

    #get average hashtags (given, present in textfile)
    #line 1 will be the average hashtags
    #line 2 will be number of tweets
    f = open("averageHashtags.txt", "r")
    averageHashtags = float(f.readline())
    numTweetsH = float(f.readline())
    f.close()

    #get average mentions
    #line 1 will be average mentions
    #line 2 will be number of tweets
    f= open("averageMentions.txt", "r")
    averageMentions = float(f.readline())
    numTweetsM = float(f.readline())
    f.close()

    #count number of hashtags referencing conference
    foundHashtags = 0
    for h in hashtags:
        if h == name:
            foundHashtags += 1

    #count number of mentions referencing conference
    foundMentions = 0
    for m in mentions:
        if m == name:
            foundMentions += 1

    #calculate found/avg for both hashtags and mentions
    total = foundHashtags / averageHashtags + foundMentions / averageMentions

    #determine whether user(?) should be flagged
    #I trust that this works @jason, although i want it to be explained to me xd - Bumjin
    f = open("dictionary.txt", "r")
    found = False
    if total > 1.5:
        lines = open("dictionary.txt", "r").readlines()
        for lineNum in range(len(lines)):
            line = f.readline()
            if line[0 : line.index(":[")] == name:
                found = True
                lines[lineNum] = (lines[lineNum])[0:len(lines[lineNum])-1] + ",[" + foundHashtags + "," + foundMentions + "]]"
                break
        if found:
            f = open("dictionary.txt", "w")
            f.writelines(lines)
            f.close()
            lines.close()
        else:
            f = open("dictionary.txt", "a")
            f.write(name + ":[[" + foundHashtags + "," + foundMentions + "]]")
            f.close()
        f = open("flag.txt", "w")
        f.write("true")
        f.close()
    else:
        f = open("flag.txt", "w")
        f.write("false")
        f.close()

    #determine new average hashtags
    averageHashtags = ((averageHashtags*numTweetsH)+len(hashtags)) / (numTweetsH + 1)
    f = open("averageHashtags.txt", "w")
    f.write(averageHashtags)
    f.write(numTweetsH+1)
    f.close()

    #determine new average mentions
    averageMentions = ((averageMentions*numTweetsM)+len(mentions)) / (numTweetsM + 1)
    f = open("averageMentions.txt", "w")
    f.write(averageMentions)
    f.write(numTweetsM+1)
    f.close()
