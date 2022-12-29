import tweepy
from random import *
import re

api_key = 'kWEOXDiOPxGdQsm84mxmmpkAw'
api_key_secret = 'pBvKCfKkGYmhdt6G4L1Uo8rOkJLJJSYZBlUyfIr997SjmXwgCL'

access_token = '1257540231168958465-Qv5n1A9mZ4sCqHx6jqJ6bkJAtaWMN0'
access_token_secret = 'urLKNB2SisxNAmPsRvH1XfrBBRgwSSGSWlEd0HIAUT8bF'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAOkekwEAAAAAkPI3%2BkeFniVXwCOgfC3Q5Fnkd%2Bs%3Dl1cCqkmXyjECkSnUwSLYPalh4BDKrOB6A4Bii9SW0sZVrnaxdk'

client = tweepy.Client(bearer_token= bearer_token,consumer_key= api_key,consumer_secret= api_key_secret,access_token= access_token,access_token_secret= access_token_secret)


def gettweets(query):
    tweets = client.search_recent_tweets(query=query)
    # print(tweets)
    response = []
    if tweets.data==type(None) or tweets.data==None:  
        return response
    else:   
        for tweet in tweets.data:
            x = re.search(r"@\w+", tweet.text)
            # m=int(x.span()[0])
            # n=int(x.span()[1])
            # print(tweet.text[m:n])

            doc = {}
            doc["title"] = query
            doc["description"] = tweet.text
            doc["imageUrl"] = "https://pbs.twimg.com/profile_images/1488548719062654976/u6qfBBkF_400x400.jpg"
            doc["dataSource"] = f"Twitter "
            doc["sourceConfidence"] = randint(40, 70)
            doc["category"] = 'trending'
            response.append(doc)
            
    return response


# print(gettweets("new year")) 

 