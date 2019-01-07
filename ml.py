def flag():

    f = open("user.txt", "r")
    name = f.readline()
    f.close()

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
            if h == name:
                foundHashtags += 1
        for m in mentions:
            if m == name:
                foundMentions += 1

        totalHashtags += len(hashtags)
        totalMentions += len(mentions)
        numTweets += 1
        
    total = (foundHashtags / numTweets) / averageHashtags + (foundMentions / numTweets) / averageMentions 

    toFlag = False
    found = False
    if total > 1.5:
        toFlag = True
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

    return toFlag
