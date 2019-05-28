import csv
import tweepy
import datetime

consumer_key='Ay04N33Qc8WUcAh0jB1dQ5XCn'
consumer_secret='qDBzJjqGvs9Vuw0ZIMTgpymkfGpTYqG3JHZrln0Ssw7oMwZj0E'
access_token='175534607-hQBPvWd0ZzYk3mhOVODRYAH3LKHyTbaKmzThYcl3'
access_token_secret='9aDkeUbfuH4NuA9WQkzQaFsgX5mAxPcfqp00HhlWJonJY'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

date1=datetime.datetime(2017,1,1)

api = tweepy.API(auth)

for tweet in tweepy.Cursor(api.user_timeline, screen_name="insert twitter username", since_id=date1).items():

    print(str(tweet.text.encode("utf-8")),str(tweet.created_at).encode("utf-8"))
