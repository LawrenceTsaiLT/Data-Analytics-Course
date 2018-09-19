# Dependencies
from bs4 import BeautifulSoup
import requests
import pymongo
from splinter import Browser
import os
import pandas as pd

def scrape():
    #dictionary
    mars_dict = {}
    #news scrape
    conn = 'mongodb://localhost:27017'
    client = pymongo.MongoClient(conn)
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url) 
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    news_title = soup.find('div', class_="content_title").text
    news_p = soup.find("div", class_="article_teaser_body").text
    mars_dict["news_title"]=news_title
    mars_dict["news_p"]=news_p

    #featured picture scrape
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)
    url_pic = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    response = requests.get(url_pic)
    soup = BeautifulSoup(response.text, 'lxml')
    featured_pic_result = soup.find('div', class_='carousel_items')
    string_pic=str(featured_pic_result)
    get_pic_code=string_pic.split("PIA",1)[1]
    pic_code=get_pic_code.ljust(5)[:5].strip()
    url_pic="https://www.jpl.nasa.gov/spaceimages/images/wallpaper/PIA"+str(pic_code)+"-1600x1200.jpg"
    mars_dict["featured_pic_url"]=url_pic

    #weather scrape
    url_weather='https://twitter.com/marswxreport?lang=en'
    response = requests.get(url_weather)
    soup = BeautifulSoup(response.text,'lxml')
    weather_tweet = soup.find('p', class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
    mars_dict["weather"]=weather_tweet

    #facts scrape
    url_facts = 'https://space-facts.com/mars/'
    browser.visit(url_facts)
    html_table = browser.html
    soup = BeautifulSoup(html_table, 'html.parser')

    table = soup.find('table', class_='tablepress tablepress-id-mars')
    column1 = table.find_all('td', class_='column-1')
    column2 = table.find_all('td', class_='column-2')

    fields = []
    values = []

    for row in column1:
        field = row.text.strip()
        fields.append(field)
        
    for row in column2:
        value = row.text.strip()
        values.append(value)
        
    mars_facts = pd.DataFrame({
        "Facet":fields,
        "Value":values
        })

    html_table = html_table.to_html(header=False, index=False)
    mars_dict["facts_table"]=html_table

    #hemispheres
    hemisphere_image_urls = [
        {"title": "Valles Marineris Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg"},
        {"title": "Cerberus Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg"},
        {"title": "Schiaparelli Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg"},
        {"title": "Syrtis Major Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg"}
    ]
    mars_dict["hemispheres"]=hemisphere_image_urls

    return mars_dict