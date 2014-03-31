import sys
import json
import difflib
import itertools
import operator
 
# Input argument is the filename of the JSON ascii file from the Twitter API
filename = sys.argv[1]
sentimentTextLabelList = []
# Loop over all lines
f = file(filename, "r")
lines = f.readlines()
#print lines

#Method for the most frequent label

def mostFrequentLabel(L):
  # get an iterable of (item, iterable) pairs
	SL = sorted((x, i) for i, x in enumerate(L))
  # print 'SL:', SL
  	groups = itertools.groupby(SL, key=operator.itemgetter(0))
  # auxiliary function to get "quality" for an item
  	def auxilaryFunc(g):
  		
  		item = g
  		iterable = g
  		count = 0
  		min_index = len(L)
  		
  		for _, where in iterable:
  			count +=1
  			min_index = min(min_index, where)
  		
  		
  		return count, -min_index
  	return max(groups, key=auxilaryFunc)[0]
  			
  # 	def _auxfun(g):
#     	item = g
#     	iterable = g
#     	count = 0
#     	min_index = len(L)
#      	for _, where in iterable:
#       		count += 1
#       		min_index = min(min_index, where)
#     		# print 'item %r, count %r, minind %r' % (item, count, min_index)
#     	return count, -min_index
#   # pick the highest-count/earliest item
	#return max(groups, key=_auxfun)[0]

fileData = open('sentiment_datavalues.txt','w')
for line in lines:
        try:
                dataLine = json.loads(line)
                sentimentText = dataLine[0]['sentiment']
                # Fetch text from tweet
                sentimentTextLabel = sentimentText['label']
                sentimentTextLabelList.append( sentimentTextLabel )
                print sentimentTextLabel
                sentimentTextPositive = sentimentText['positive']
                print sentimentTextPositive
                sentimentTextNegative = sentimentText['negative']
                print sentimentTextNegative
                sentimentTextNeutral = sentimentText['neutral']
                print sentimentTextNeutral
                sentimentTextConfidence = sentimentText['confidence']
                print sentimentTextConfidence
                # Show result

                
                fileData.write(sentimentTextLabel + ' ')
                fileData.write(str(sentimentTextPositive) + ' ')
                fileData.write(str(sentimentTextNegative) + ' ')
                fileData.write(str(sentimentTextNeutral) + ' ')
                fileData.write(str(sentimentTextConfidence) + '\n')
			    
               	#print text + '\n'
               	#fileData.write(sentiment +'\n')
                #tweets_text.append( text )
                #tweets_location.append( tweet['user']['location'] )
                #tweets_timezone.append( tweet['user']['time_zone'] )
 
        except ValueError:
                pass

mostFrequentLabel(sentimentTextLabelList)

fileData.close()
