from twython import Twython, TwythonError
import time

APP_KEY = 'nal6mPbOPa5rBT2uhvtRIX03b'
APP_SECRET = 'TPcWCRJCuALFVD737MjjN5XI08gAsApikFUlS7JNLh50se0kTd'


OAUTH_TOKEN = '909530490931236864-qMe00WRFdrguxgbUud8HJfFCGOYIpDg'
OAUTH_TOKEN_SECRET = 'qmkxswK4l3Tu3dLZLHXlqVa8unHnWmsJPLV7TaTs7vtrT'



twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

try:
    
    try:
        search_results = twitter.search(q='Trump', count=1)
    
    except TwythonError as e:
        print (e)



    for tweet in search_results['statuses']:
        twitter.retweet (id=tweet['id'])
        
        print (tweet['text'].encode('utf-8'), '\n', tweet['created_at'])

