def flag(conference, company):
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
    
    f = open("tweets.json", "r")
    for line in f:
        hashtag = ""
        hashtags = []
        try:
            hashtag = line[line.index("[",line.index("hashtags\":")) : line.index("]}]},",line.index("hashtags\":"))+1]
            if hashtag[1] == "]":
                hashtag = ""
        except:
            try:
                hashtag = line[line.index("[",line.index("hashtags\":")) : line.index("],",line.index("hashtags\":"))+1]
                if hashtag[1] == "]":
                    hashtag = ""
            except:
                hashtag = ""	
        if (len(hashtag) != 2 and len(hashtag) != 0):
            hashtag = hashtag[1 : len(hashtag)-1].lower()
            hashtags = hashtag.split("},")
            for x in range(len(hashtags)):
                try:
                    hashtags[x] = (hashtags[x])[9 : hashtags[x].index("indices")-3]
                except:
                    hashtags[x] = ""
        f.close()

        f = open("tweet.json", "r")
        line = f.readline()
        mention = ""
        mentions = []
        try:
            mention = line[line.index("[",line.index("user_mentions\":")) : line.index("]}]},",line.index("user_mentions\":"))+1]
            if mention[1] == "]":
                mention = ""
        except:
            try:
                mention = line[line.index("[",line.index("user_mentions\":")) : line.index("}]",line.index("user_mentions\":"))+2]
                if mention[1] == "]":
                    mention = ""
            except:
                mention = ""
        if (len(mention) != 2 and len(mention) != 0):
            mention = mention[1 : len(mention)-1].lower()
            mentions = mention.split("},")
            for x in range(len(mentions)):
                try:
                    mentions[x] = (mentions[x])[mentions[x].index("screen_name\":")+14 : mentions[x].index("\",")]
                except:
                    mentions[x] = ""
        f.close()
        
        for h in hashtags:
            if h == conference:
                foundHashtags += 1
        for m in mentions:
            if m == conference:
                foundMentions += 1

        totalHashtags += len(hashtags)
        totalMentions += len(mentions)
        numTweets += 1
        
    total = ((foundHashtags / numTweets) / averageHashtags + (foundMentions / numTweets) / averageMentions) / 2

    toFlag = False
    found = False
    if total > 0.5:
        toFlag = True
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
            
    averageHashtags = ((averageHashtags*numTweetsH)+totalHashtags) / (numTweetsH + numTweets)
    f = open("averageHashtags.txt", "w")
    f.write(averageHashtags)
    f.write(numTweetsH+numTweets)
    f.close()
    averageMentions = ((averageMentions*numTweetsM)+totalMentions) / (numTweetsM + numTweets)
    f = open("averageMentions.txt", "w")
    f.write(averageMentions)
    f.write(numTweetsM+numTweets)
    f.close()

    print("Done.\n")
    
    print("In "+"numTweets" + " tweets, " + "twitter user @" + company + " used " + totalHashtags + " hashtags and " + totalMentions + "mentions of the twitter user @" + conference)
    if toFlag:
        print("@" + company + " and @" + conference + " were found to have a " + total + " correlation with each other, indicating the presence of a strong relationship.")
    else:
        print("@" + company + " and @" + conference + " were found to have a " + total + " correlation with each other, indicating the lack of a strong relationship.")

