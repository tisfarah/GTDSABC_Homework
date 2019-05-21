import os
from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser
import pandas as pd 
import time 

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape_info_mars():
    browser = init_browser()

    # Visit website 
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # Get the list section that has the articles and grab the first instance 
    article_section = soup.select_one("ul.item_list li.slide")


    # Get the latest article title in text format
    mars_title = article_section.find("div", class_="content_title").get_text()

    # Get the latest article body in text format 
    mars_body = article_section.find("div", class_="article_teaser_body").get_text()

    # Store data in a dictionary
    latest_mars = {
        "mars_title": mars_title,
        "mars_body": mars_body,
    }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_body, mars_title

def featured_image_mars():
    browser = init_browser()
    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)
    time.sleep(1)

    # Click the full image button
    full_image = browser.find_by_id("full_image")
    full_image.click()

    # Click the more info button
    browser.is_element_present_by_text("more info")
    more_info = browser.find_link_by_partial_text("more info")
    more_info.click()

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")
    
    #image is nested in class under figure, a link, and img tag
    image = soup.select_one("figure.lede a img")

    image_url = image.get("src")

    # Use the base url to create an absolute url
    featured_image_url = f"https://www.jpl.nasa.gov{image_url}"

    # Close the browser after scraping
    browser.quit()

    # Return results
    return featured_image_url 

def weather():
    browser = init_browser()
    url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(url)
    
    response = requests.get(url)
    soup = bs(response.text, 'html.parser')

    tweet_weather = soup.find('p',{"class": "TweetTextSize TweetTextSize--normal js-tweet-text tweet-text"}).get_text()
    
    # Close the browser after scraping
    browser.quit()

    # Return results
    return tweet_weather 

def facts():
    browser = init_browser()
    url = 'https://space-facts.com/mars/'
    data_table = pd.read_html(url)
    data_table = data_table[0]
    data_table.columns = ['Description', 'Value']
    
    html_table = data_table.to_html()
    
    # Stop webdriver and return data
    browser.quit()
    return html_table

def all_data():
    
    browser = init_browser()
    mars_body, mars_title = scrape_info_mars()
    all_data = {
        "mars_title": mars_title,
        "mars_body": mars_body,
        "featured_image_url": featured_image_mars(),
        "twitter_weather": weather(),
        "facts_table":facts(),
    }

    # Close the browser after scraping
    browser.quit()
    
    # Return results
    return all_data