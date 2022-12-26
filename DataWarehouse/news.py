from pytrends.request import TrendReq
import requests
from random import *
pytrend = TrendReq()


def getNews():
    # print("news updated")
    df = pytrend.trending_searches()
    df = df.values.tolist()
    for keyword in df:
        # print(keyword[0])
        url = ('https://newsapi.org/v2/everything?'
               f'q={keyword[0]}&'
               'sortBy=popularity&'
               'apiKey=725ba7ccb67f4ec0b6e1750cfdccc4bb')
        response = requests.get(url)
        results = response.json()["articles"]
        response = []
        for data in results:
            doc = {}
            doc["title"] = data["title"]
            doc["description"] = data["content"]
            doc["imageUrl"] = data["urlToImage"]
            doc["dataSource"] = data["source"]["name"]
            doc["sourceConfidence"] = randint(80, 95)
            doc["category"] = 'trending'
            response.append(doc)

        return response
