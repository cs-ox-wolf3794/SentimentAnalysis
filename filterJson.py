import sys
import json
import difflib
 
# Input argument is the filename of the JSON ascii file from the Twitter API

filename = sys.argv[1]
filtered_file = sys.argv[2]

tweets_text = [] # We will store the text of every tweet in this list
tweets_location = [] # Location of every tweet (free text field - not always accurate or given)
tweets_timezone = [] # Timezone name of every tweet
 
# Loop over all lines
f = file(filename, "r")
lines = f.readlines()
fileData = open(filtered_file,'w')
for line in lines:
        try:
                tweet = json.loads(line)
               
                # Ignore retweets!
                if tweet.has_key("retweeted_status") or not tweet.has_key("text"):
                        continue
               
                # Fetch text from tweet
                text = tweet["text"].lower()
               
                # Ignore 'manual' retweets, i.e. messages starting with RT             
                if text.find("rt ") > -1:
                        continue
               
               	#print text + '\n'
               	if str(text).__len__() > 10:
               		print str(text).__len__()
               		fileData.write(text +'\n')
               		#tweets_text.append( text )
                #tweets_location.append( tweet['user']['location'] )
                #tweets_timezone.append( tweet['user']['time_zone'] )
 
        except ValueError:
                pass
                
       
#fileData.write(tweets_text)
fileData.close()


# Show result
#print tweets_text.newline()
#print tweets_location
#print tweets_timezone