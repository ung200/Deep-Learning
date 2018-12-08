import tweepy
import pprint
import config

import pandas as pd

#print(config.CREDENTIALS['access_token'])
#exit()
auth = tweepy.OAuthHandler(config.CREDENTIALS['consumer']['key'], config.CREDENTIALS['consumer']['secret'])
auth.set_access_token(config.CREDENTIALS['access']['token'], config.CREDENTIALS['access']['secret'])
api = tweepy.API(auth)

user = api.get_user('BarackObama')
#print(user.followers_count)
data = api.user_timeline(id='BarackObama', count=20, tweet_mode='extended')

#print(data[0]._json['full_text'])

all_tweets = []

for tweet in data:
    all_tweets.append(tweet._json['full_text'])

pd_all_tweets = pd.DataFrame(all_tweets)
print(pd_all_tweets)

pd_all_tweets.to_csv('obama_data.csv')

#print(data)
