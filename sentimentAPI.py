import affectr
import sys
import os
import time
import re
from collections import Counter

affectr.set_details("gangulys@theysayanalytics.com", "Disent-Ils3915")
filename = sys.argv[1]
output_file = sys.argv[2]


def file_len(fname):
	i = 0
	with open(fname) as f:
		for i, l in enumerate(f):
			pass
	return i + 1

len = file_len(filename)
print len

f = file(filename, "r")
lines = f.readlines()

file_data = open(output_file,'w')
# senti = []
entity_pos = []
entity_neg = []
li = 0

for line in lines:
		try:
			if(str(line).__len__() > 10):#print line
				s = affectr.client.classify_entity_sentiment(line)[0].sentiment
				#senti.append( str(s.label) )
				e = affectr.client.classify_entity_sentiment(line)[0].headNoun
				if str(s.label) == 'POSITIVE': 
					entity_pos.append( e )
				if str(s.label) == 'NEGATIVE':
					entity_neg.append( e )
			#s = affectr.client.classify_sentiment(line)
			#file_data.write(str(s.sentiment.label) + ' ')
				file_data.write(str(e) + '\n')
				file_data.write(str(s.label) + '\n')
		
		
			
			#print s.sentiment.label + '\n'
			print s.label 
			print e 
		
		
		except IndexError:
			pass
		time.sleep(0.3)
#	li = li + 1		
		
file_data.close()

def match_of_the_match_predictor(object):
	freq_counter = {}
	for entity in object:
		if entity in freq_counter:
			freq_counter[entity] += 1
		else:
			freq_counter[entity] = 1
		
	freq_words = sorted(freq_counter, key = freq_counter.get, reverse = True)
	
	top_results = freq_words[:20]
	print top_results
	
		

match_of_the_match_predictor(entity_pos)

match_of_the_match_predictor(entity_neg)