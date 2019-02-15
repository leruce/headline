from flask import Flask
from flask import request
from flask import render_template
import feedparser


app = Flask(__name__)

RSSFEED = { 'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
            'cnn': 'http://rss.cnn.com/rss/edition.rss',
            'fox': 'http://feeds.foxnews.com/foxnews/latest'}


@app.route("/")
#@app.route("/<publication>")
#def get_news(publication = "bbc"):
def get_news():
    query = request.args.get("publication")
    if not query or  query.lower() not in RSSFEED:
        publication = "bbc"
    else:
        publication = query.lower()

    feed = feedparser.parse(RSSFEED[publication])
    return render_template("headline.html",articles = feed['entries'])



if __name__ == '__main__':
    app.run(port = 5000, debug = True)
