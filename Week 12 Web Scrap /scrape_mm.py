from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
import requests 

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
    return latest_mars

# def all_data():

#     browser = Browser("chrome", executable_path="chromedriver", headless=True)
#     news_title, news_p = mars_news()

#     # Each scraping function will store the results in a dictionary.   Define the dictionaries.
#     data = {
#         "news_title": news_title,
#         "news_paragraph": news_p,
#         "featured_image": featured_image(),
#         "hemispheres": hemispheres(),
#         "weather": twitter_weather(),
#         "facts": mars_facts(),
#         "last_modified": dt.datetime.now()
#     }

#     # Stop webdriver and return data
#     browser.quit()
#     return data