import requests
from requests import get
from datetime import date
from bs4 import BeautifulSoup
import datetime
import time
import json
from json import JSONEncoder

urls = {
  "guardian_url": "https://www.theguardian.com/uk", 
  "times_url": "https://www.thetimes.co.uk/",
  "telegraph_url": "https://www.telegraph.co.uk/",
  "dailymail_url": "https://www.dailymail.co.uk/home/index.html",
  "dailymirror_url":"https://www.mirror.co.uk/",
  "dailyexpress_url": "https://www.express.co.uk/",
  "independent_url": "https://www.independent.co.uk/",
  "financialtimes_url": "https://www.ft.com/"

}

guardian_url = "https://www.theguardian.com/uk"
times_url = "https://www.thetimes.co.uk/"
telegraph_url = "https://www.telegraph.co.uk/"
dailymail_url = "https://www.dailymail.co.uk/home/index.html"
dailymirror_url = "https://www.mirror.co.uk/"
dailyexpress_url = "https://www.express.co.uk/"
independent_url = "https://www.independent.co.uk/"
financialtimes_url = "https://www.ft.com/"
# inews_url = "https://inews.co.uk/"
# morningpost_url = "https://morningstaronline.co.uk/"
# dailystar_url = "https://www.dailystar.co.uk/"
# sun_url = "https://www.thesun.co.uk/"
# eveningstandard_url = "https://www.standard.co.uk/"
# irishsun_url = "https://www.thesun.ie/"
# thescotsman = "https://www.scotsman.com/"
# metro_url = "https://metro.co.uk/"
# herald_url = "https://www.heraldscotland.com/"

headlines = []

response = { "status": "success", "data": headlines}


# class Headline:
#   def __init__(self, paper, headline):
#     self.paper = paper
#     self.headline = headline

# # subclass JSONEncoder
# class HeadlineEncoder(JSONEncoder):
#   def default(self, o):
#       return o.__dict__

def scrape(url):

  headers = {'User-Agent': 'Mozilla/5.0'}
  results = requests.get(url, headers=headers)
  soup = BeautifulSoup(results.text, "html.parser")

  if url == guardian_url:
    paper = "The Guardian"
    headline_html = soup.find('span', class_='js-headline-text')
    if headline_html != None:
      headline = headline_html.text.strip()
    else:
      headline = "Error - failed to scrape " + paper

  if url == times_url:
    paper = "The Times"
    headline_html = soup.find('h3', class_='Headline--xl')
    if headline_html != None:
      headline = headline_html.text.strip()
    else:
      headline = "Error - failed to scrape " + paper

  if url == telegraph_url:
    paper = "The Telegraph"
    headline_html = soup.find('span', class_='list-headline__text')
    if headline_html != None:
      headline = headline_html.text.strip()
    else:
      headline = "Error - failed to scrape " + paper

  if url == dailymail_url:
    paper = "Daily Mail"
    headline_html = soup.find('h2', class_='linkro-darkred')
    if headline_html != None:
      headline = headline_html.text.strip()
    else:
      headline = "Error - failed to scrape " + paper

  if url == dailymirror_url:
    paper = "Daily Mirror"
    headline_html = soup.find('div', class_='teaser-hero')
    if headline_html != None:
      headline = headline_html.text.strip()
    else:
      headline = "Error - failed to scrape " + paper

  if url == dailyexpress_url:
    paper = "The Daily Express"
    headline_html = soup.find('h2')
    if headline_html != None:
      headline = headline_html.text.strip()
    else:
      headline = "Error - failed to scrape " + paper

  if url == independent_url:
    paper = "The Independent"
    headline_html = soup.find('h2')
    if headline_html != None:
      headline = headline_html.text.strip()
    else:
      headline = "Error - failed to scrape " + paper

  if url == financialtimes_url:
    paper = "The Financial Times"
    headline_html = soup.find('div', class_="o-teaser__heading")
    if headline_html != None:
      headline = headline_html.text.strip()
    else:
      headline = "Error - failed to scrape the " + paper

  # head = Headline(paper, headline)
  myDictObj = { "paper":paper, "headline":headline }

  # headlineJSONData = json.dumps(head, cls=HeadlineEncoder)
  # json.dumps(json.JSONDecoder().decode(str_w_quotes))

  headlines.append(myDictObj)
  # add a timestamp to be used on the app as last updated - maybe

def print_headlines():
  # time_stamp = datetime.datetime.now()
  # date_stamp = time_stamp.strftime("%H:%M:%S (%Y-%m-%d)")
 
  for url in urls.values():
    scrape(url)
    
  return response
