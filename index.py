from flask import Flask
import threading
import DataWarehouse.news as getNews
import DataWarehouse.tweets as getTweets
import DataWarehouse.wikipedia as getWikipedia

def printit():
    threading.Timer(5.0, printit).start()
    global newsData
    newsData = getNews.getNews()


def create_app():
    app = Flask(__name__)
    printit()
    return app


app = create_app()


@app.route('/')
def home():
    return '<H6>/query/<query> : Will give to data regrading the specfic query<br> /n /api : will give to all trending data</h6>'


@app.route('/query/<query>')
def req(query):
    tweets=getTweets.gettweets(query)
    news=getNews.getNews([query])
    wiki=getWikipedia.get_wiki(query)
     
    res=tweets+news+wiki

    return res


@app.route('/trendingNews')
def trendingNews():
    # res = getNews.getNews()
    return newsData


@app.route('/api')
def api():
    with open('data.json', mode='r') as my_file:
        text = my_file.read()
        return text


if __name__ == "__main__":
    app.run(debug=True)
