from flask import Flask
from flask_cors import CORS
from flask import Blueprint

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
    @app.errorhandler(404)
    def page_not_found(e):
        return """<!DOCTYPE html> <html> <head> <title>Page not found</title> <style> /* Center the message vertically and horizontally */ #message { display: flex; justify-content: center; align-items: center; height: 100%; text-align: center; } /* Add some styling to the message */ #message h1 { font-size: 2em; font-weight: bold; color: #555; margin: 0; } #message p { font-size: 1.5em; color: #888; margin: 0; } </style> </head> <body> <div id="message"> <div> <h1>Route not found</h1> <p>The requested route could not be found.</p><p>Refer the <a href="https://newssource.pythonanywhere.com/">NewsSource API Documentation
</a></p> </div> </div> </body> </html>"""

    return app


app = create_app()

# Create a blueprint
my_blueprint = Blueprint('my_blueprint', __name__)

# Enable CORS for all routes under the blueprint
cors = CORS(my_blueprint, resources={r"/*": {"origins": "*"}})


@app.route('/')
def home():
    with open('/home/NewsSource/mysite/Documentation/index.html', mode='r') as my_file:
        text = my_file.read()
    return text


@my_blueprint.route('/query/<query>')
def req(query):
    tweets = getTweets.gettweets(query)
    news = getNews.getNews([query])
    wiki = getWikipedia.get_wiki(query)

    res = tweets+news+wiki

    return res


@my_blueprint.route('/trendingNews')
def trendingNews():
    # res = getNews.getNews()
    return newsData


@my_blueprint.route('/api')
def api():
    with open('data.json', mode='r') as my_file:
        text = my_file.read()
        return text


# Register the blueprint to the application
app.register_blueprint(my_blueprint)

if __name__ == "__main__":
    app.run(debug=True)
