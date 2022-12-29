import wikipediaapi
import requests
from random import *
from summarizer import summarize

wiki_wiki = wikipediaapi.Wikipedia('en')

def get_wiki(query):
    page_py = wiki_wiki.page(query)
    if page_py.exists():

        summarize(page_py.title,page_py.summary,7)
        response = []     
        doc = {}
        doc["title"] = page_py.title
        doc["description"] = summarize(page_py.title,page_py.summary,7)
        doc["imageUrl"] = "https://upload.wikimedia.org/wikipedia/en/thumb/8/80/Wikipedia-logo-v2.svg/1200px-Wikipedia-logo-v2.svg.png"
        doc["dataSource"] = "Wikipedia"
        doc["sourceConfidence"] = randint(90, 100)
        doc["category"] = 'searched'
        response.append(doc)
        
        return response
    else:
        return []
