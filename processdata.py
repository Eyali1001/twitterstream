import json

tweets_data = []
tweets_file = open("C:\dasd\output.txt", "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue
print len(tweets_data)

a= 0
for i in tweets_data:
	try:
		print i["text"]
		a+=1
	except:
		continue
print a
