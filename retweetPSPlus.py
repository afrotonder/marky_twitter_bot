#!/usr/bin/env python
# tweepy-bots/bots/followfollowers.py
# TODO: RUN THIS FROM THE 20TH OF THE CURRENT MONTH TO THE 10TH OF THE NEXT MONTH. ELSE SLEEP 
import tweepy
import logging
from config import create_api, logger
import time
import calendar
import json

# psPLusID = api.get_user("SonyPSPlus")

def retweetPSPlus(api):

    myId = 3302239551
    sonyId = 10671602
    psPlus_unofficial = 899074496
    # pspls_tweets = []
    pspls_tweet_ids = []
    months = calendar.month_name[1:]
    
    for Tweet in api.user_timeline(sonyId):
        text = str(Tweet.text.encode("utf-8"))
        # check if tweet contains specific PsPlus text
        # replace this text search with regex
        if "PlayStation Plus" not in text :
            continue
        # TODO: replace this if with regex
        # if text contains any month text, add to possible tweets.
        if  any(word in text for word in months):
            pspls_tweet_ids.append(Tweet.id) 
            # pspls_tweets.append(Tweet)
    
    # print(pspls_tweet_ids)

    # check all 24vg  tweets, skip if it doesnt have 
    for Tweet in api.user_timeline(myId):
        # status = api.get_status(Tweet.id)
        
        if (Tweet.retweeted):
            # print(Tweet.retweeted_status)
        # if ("retweeted_status" in tweet_dict):
            rtId = Tweet.retweeted_status
            if (rtId.id in pspls_tweet_ids):
                pspls_tweet_ids.remove(rtId.id)
                print('Tweet already retweeted.')
        else:
            continue

    print('final ps plus tweet ',pspls_tweet_ids)

    if (len(pspls_tweet_ids) == 1):
        # api.retweet(pspls_tweet_ids[0])
        print('EA DIALO RETWEET')
    else:
        print('No new monthly ps plus game list.')

def main():
    api = create_api()
    # while True:
    retweetPSPlus(api)

    exit()
        # logger.info("Waiting...")
        # time.sleep(60)

if __name__ == "__main__":
    main()