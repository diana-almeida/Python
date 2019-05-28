import csv
import tweepy
import datetime

consumer_key=''
consumer_secret=''
access_token=''
access_token_secret=''


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

date1=datetime.datetime(2017,1,1)

api = tweepy.API(auth)

for tweet in tweepy.Cursor(api.user_timeline, screen_name="insert twitter username", since_id=date1).items():

    print(str(tweet.text.encode("utf-8")),str(tweet.created_at).encode("utf-8"))
