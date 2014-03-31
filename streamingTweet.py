import tweepy
from tweepy import OAuthHandler
from s_listener import S_Listener
import time, tweepy, sys
auth1 = tweepy.auth.OAuthHandler('ayDey2CtHA9fnPqW4r5M8A','ZukFL2NY2kzv5SAXqPpuOicLDIIJwUPqCbZiEquzOY')
auth1.set_access_token('84429310-IPNfaovbNSl46WKCIfM9SMaNwm00ifvOfWOfDE5p5','C8LP6Oy6n2PjojipoE8bXvtF0oA0lnFiNOZpG4pC4')
api = tweepy.API(auth1)
print api.me().name
api = tweepy.API(auth1)

def main():
	track = ['Barclays Premier League']
	#['Barca']
	#['MUFC','swansea','manchester','manutd']
	#['England Australia', 'Cricket', 'Lords', 'The ashes', 'England vs Australia', 'Eng vs Aus', 'EngvsAus', 'ashes', 'Australia vs England', 'Aus vs Eng', 'AusvsEng']
    #['mufc','wembley', 'Wigan', 'Man Utd vs Wigan', 'Man Utd v Wigan', 'Manchester UTD', 'Manchester United'] 
    
    #['England vs Australia', 'EngvsAus', 'The Ashes','Ashes','Australia vs England','espncricinfo','ausvseng']
	
	#['England Australia', 'Cricket', 'Lords', 'The ashes', 'England vs Australia', 'Eng vs Aus', 'EngvsAus', 'ashes', 'Australia vs England', 'Aus vs Eng', 'AusvsEng']

	listen = S_Listener(api, 'ManNU')
	stream = tweepy.Stream(auth1, listen)

	print "Streaming started..."

	try: 
		stream.filter(track = track)
	except:
		print "error!"
		stream.disconnect()

if __name__ == '__main__':
	main()