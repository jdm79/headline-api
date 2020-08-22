from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions
from flask import Flask
from flask import jsonify
from flask_cors import CORS
import json
import datetime
import time
import random
import requests
from urls import urls
from scraper import scrape
from scraper import headlines
from requests import get
from datetime import date
from bs4 import BeautifulSoup

response = { "status": "success", "data": headlines}

def print_headlines():
  # clear the list so we only get the latest headlines
  headlines.clear()

  # run this function over each paper
  for url in urls.values():
    scrape(url)
    
  # the function returns the final list
  return response


#### ----------------------------------------------------- ####

# the Route(s)
app = FlaskAPI(__name__)
CORS(app)

@app.route("/headlines", methods=['GET'])

def headlines_list():
   
  # grab the latest response from the print_headlines function
  scraped_headlines = print_headlines()

  # turn this list into JSON for the front end to request
  return jsonify(scraped_headlines)
    
if __name__ == "__main__":
    app.run(debug=True)