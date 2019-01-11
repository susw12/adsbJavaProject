def flag(conferenceHashtag, conferenceHandle, company):
    f = open("averageHashtags.txt", "r")
    averageHashtags = float(f.readline())
    numTweetsH = float(f.readline())
    f.close()
    f = open("averageMentions.txt", "r")
    averageMentions = float(f.readline())
    numTweetsM = float(f.readline())
    f.close()

    foundHashtags = 0
    totalHashtags = 0
    foundMentions = 0
    totalMentions = 0
    numTweets = 0
    hashtags = []
    mentions = []

    lineNum = 0
    f = open("tweets.json", "r")
    for line in f:
        if (lineNum % 2 == 0):
            numTweets += 1
            hashtag = line.strip()
            if (len(hashtag) == 2):
                hashtag = ""
            else:
                hashtag = hashtag[1 : len(hashtag)-1].lower()
                hashtags = hashtag.split("}, ")
                for x in range(len(hashtags)):
                    hashtags[x] = (hashtags[x])[10 : hashtags[x].index(", 'indices'")-1].strip()
            for h in hashtags:
                print(h + " : " + str(numTweets))
                if h == conferenceHashtag:
                    foundHashtags += 1
        else:
            mention = line.strip()
            if (len(mention) == 2):
                mention = ""
            else:
                mention = mention[1 : len(mention)-1].lower()
                mentions = mention.split("}, ")
                for x in range(len(mentions)):
                    mentions[x] = (mentions[x])[17 : mentions[x].index(", 'name")-1].strip()
            for m in mentions:
                print(m + " : " + str(numTweets))
                if m == conferenceHandle:
                    foundMentions += 1
        lineNum += 1
            
    f.close()

    totalHashtags += len(hashtags)
    totalMentions += len(mentions)

    print("\n")
    print("foundHashtags: " + str(foundHashtags))
    print("foundMentions: " + str(foundMentions))
    print("numTweets:" + str(numTweets))
    print("averageHashtags: " + str(averageHashtags))
    print("averageMentions: " + str(averageMentions))
    total = ((float(foundHashtags) / float(numTweets)) / float(averageHashtags) + (float(foundMentions) / float(numTweets)) / float(averageMentions)) / 2
    
    toFlag = False
    #found = False
    if total > 0.35:
        toFlag = True
        """
        lines = open("dictionary.txt", "r").readlines()
        for lineNum in range(len(lines)):
            line = f.readline()
            if line[0 : line.index(":[")] == conference:
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
            f.write(conference + ":[[" + foundHashtags + "," + foundMentions + "]]")
            f.close()
        """
            
    averageHashtags = ((averageHashtags*numTweetsH)+totalHashtags) / (numTweetsH + numTweets)
    f = open("averageHashtags.txt", "w")
    f.write(str(averageHashtags))
    f.write("\n")
    f.write(str(numTweetsH+numTweets))
    f.close()
    averageMentions = ((averageMentions*numTweetsM)+totalMentions) / (numTweetsM + numTweets)
    f = open("averageMentions.txt", "w")
    f.write(str(averageMentions))
    f.write("\n")
    f.write(str(numTweetsM+numTweets))
    f.close()

    print("Done.\n")
    
    print("In "+ str(numTweets) + " tweets, " + "twitter user @" + company + " used " + str(foundHashtags) + " hashtags and " + str(foundMentions) + " mentions of the twitter user @" + conferenceHandle)
    if toFlag:
        print("@" + company + " and @" + conferenceHandle + " or #" + conferenceHashtag + " were found to have a " + str(total) + " correlation with each other, indicating the presence of a strong relationship.")
    else:
        print("@" + company + " and @" + conferenceHandle + " or #" + conferenceHashtag + " were found to have a " + str(total) + " correlation with each other, indicating the lack of a strong relationship.")
