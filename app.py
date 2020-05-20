from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions
from flask import Flask
from flask_cors import CORS
import json
from scraper import print_headlines

app = FlaskAPI(__name__)
CORS(app)


scraped_headlines = print_headlines()

print(scraped_headlines)


@app.route("/headlines", methods=['GET'])
def headlines_list():
    print_headlines()
   
    headlines = json.dumps(scraped_headlines)

    return headlines, status.HTTP_201_CREATED

if __name__ == "__main__":
    app.run(debug=True)