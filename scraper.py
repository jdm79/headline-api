import random
import requests
import datetime
import time
from urls import urls
from bs4 import BeautifulSoup

# initialising my headlines list to be populated by dictionary objects
headlines = []
fail = "Currently unable to get headlines for "

guardian_url = "https://www.theguardian.com/uk"
times_url = "https://www.thetimes.co.uk/"
telegraph_url = "https://www.telegraph.co.uk/"
dailymail_url = "https://www.dailymail.co.uk/home/index.html"
dailymirror_url = "https://www.mirror.co.uk/"
dailyexpress_url = "https://www.express.co.uk/"
independent_url = "https://www.independent.co.uk/news/uk"
financialtimes_url = "https://www.ft.com/"
inews_url = "https://inews.co.uk/"
morningstar_url = "https://morningstaronline.co.uk/"
dailystar_url = "https://www.dailystar.co.uk/"
sun_url = "https://www.thesun.co.uk/"
eveningstandard_url = "https://www.standard.co.uk/"
irishsun_url = "https://www.thesun.ie/"
thescotsman_url = "https://www.scotsman.com/news/uk-news/"
metro_url = "https://metro.co.uk/"

def scrape(url):
  
  randomUrls = [ 
    "https://www.facebook.com/", 
    "https://www.google.co.uk", 
    "https://www.twitter.com"
    ]

  headers = {
    'User-Agent': 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
    'Referer': random.choice(randomUrls) 
    }

  results = requests.get(url, headers=headers, allow_redirects=False)

  # beautiful soup methods are now available to clean this data response
  soup = BeautifulSoup(results.text, "html.parser")

 
  if url == guardian_url:
    paper = "The Guardian"
    headline_html = soup.find('span', class_='js-headline-text')
    link = url
    if headline_html != None:
      headline = headline_html.text.strip()
    else:
      headline = fail + paper

  if url == times_url:
    paper = "The Times"
    headline_html = soup.find('h3', class_='Headline--xl')
    link = url
    if headline_html != None:
      headline = headline_html.text.strip()
    else:
      headline = fail + paper

  if url == telegraph_url:
    paper = "The Telegraph"
    headline_html = soup.find('span', class_='list-headline__text')
    link = url
    if headline_html != None:
      headline = headline_html.text.strip()
    else:
      headline = fail + paper

  if url == dailymail_url:
    paper = "Daily Mail"
    headline_html = soup.find('h2', class_='linkro-darkred')
    link = url
    if headline_html != None:
      headline = headline_html.text.strip()
    else:
      headline = fail + paper

  if url == dailymirror_url:
    paper = "Daily Mirror"
    headline_html = soup.find('a', class_='publication-font')
    link = url
    if headline_html != None:
      headline = headline_html.text.strip()
    else:
      headline = fail + paper

  if url == dailyexpress_url:
    paper = "Daily Express"
    headline_html = soup.find('h2')
    link = url
    if headline_html != None:
      headline = headline_html.text.strip()
    else:
      headline = fail + paper

  if url == independent_url:
    paper = "Independent"
    headline_html_array = soup.find_all('h2')
    headline_html = headline_html_array[0]
    link = url
    if headline_html != None:
      headline = headline_html.text.strip()
    else:
      headline = fail + paper

  if url == financialtimes_url:
    paper = "Financial Times"
    headline_html = soup.find('div', class_="o-teaser__heading")
    link = url
    if headline_html != None:
      headline = headline_html.text.strip()
    else:
      headline = fail + paper

  if url == metro_url:
    paper = "Metro"
    headline_html = soup.find('span', class_="colour-box")
    link = url
    if headline_html != None:
      headline = headline_html.text.strip()
    else:
      headline = fail + paper

  if url == dailystar_url:
    paper = "Daily Star"
    headline_html = soup.find('a', class_="publication-font")
    link = url
    if headline_html != None:
      headline = headline_html.text.strip()
    else:
      headline = fail + paper

  if url == inews_url:
    paper = "The i"
    headline_html = soup.find('div', class_="inews__post-hero__content")
    link = url
    if headline_html != None:
      headline = headline_html.text.strip()
    else:
      headline = fail + paper

  if url == sun_url:
    paper = "The Sun"
    headline_html = soup.find('p', class_="teaser__subdeck")
    link = url
    if headline_html != None:
      headline = headline_html.text.strip()
    else:
      headline = fail + paper

  if url == morningstar_url:
    paper = "Morning Star"
    headline_html = soup.find('h1')
    link = url
    if headline_html != None:
      headline = headline_html.text.strip()
    else:
      headline = fail + paper

  if url == eveningstandard_url:
    paper = "Evening Standard"
    headline_html = soup.find('div', class_="content")
    link = url
    if headline_html != None:
      headline = headline_html.text.strip()
    else:
      headline = fail + paper

  if url == irishsun_url:
    paper = "The Irish Sun"
    headline_html = soup.find('p', class_="teaser__subdeck")
    link = url
    if headline_html != None:
      headline = headline_html.text.strip()
    else:
      headline = fail + paper
  
  if url == thescotsman_url:
    paper = "The Scotsman"
    headline_html = soup.find('a', class_='article-title sc-iNhVCk favtwH')
    link = url
    if headline_html != None:
      headline = headline_html.text.strip()
    else:
      headline = fail + paper

  time_stamp = datetime.datetime.now()
  date_stamp = time_stamp.strftime("%H:%M:%S (%Y-%m-%d)")
 
  # here i create the dictionary object, populating it with the following key/value pairs
  # these key/value pairs will be available on the front end app to display
  myDictObj = { "paper": paper, "headline": headline, "updated": date_stamp, "link": link }
  # once the dictionary object is created, each one goes into my headlines list
  headlines.append(myDictObj)