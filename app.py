from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions
import json
from scraper import print_headlines

app = FlaskAPI(__name__)

scraped_headlines = print_headlines()

print(scraped_headlines)


@app.route("/headlines", methods=['GET'])
def headlines_list():
   
    headlines = scraped_headlines

    return headlines, status.HTTP_201_CREATED

if __name__ == "__main__":
    app.run(debug=True)