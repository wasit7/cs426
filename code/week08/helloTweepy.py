#!/usr/bin/env python
# -*- coding: utf-8 -*-
 #this code follows the tutorial
#http://www.dototot.com/how-to-write-a-twitter-bot-with-python-and-tweepy/
#http://tweepy.readthedocs.org/en/v3.2.0/getting_started.html#introduction
import tweepy
 
consumer_key = 'x1n8SGT4Vf1yK8YoYoubg5Tba'
consumer_secret = 'oxcKRn4PrJRMCOv0SFjGEZpb2qQb3HBVuP2fy9Fpx1tRn05IA0'
access_token = '222179585-9tBymOKPwWKyQgWKGtxyUk5iIMTbYWpq5lD6rsbw'
access_token_secret = 'cn2HZtRierqwTP7JDL2B4YiRHQEXJ54r0CHh6gPSTljyu'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
#public_tweets = api.home_timeline()
#for tweet in public_tweets:
#    print tweet.text
user = api.get_user('wasit7')
print user.screen_name
print user.followers_count
for friend in user.friends():
   print friend.screen_name
api.update_status(status='Hello tweepy!')
