# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# Set the executable path and initialize the chrome browser in splinter
executable_path = {'executable_path': "C:\\Users\\A Girl's Lenovo\\.wdm\\drivers\\chromedriver\\win32\\89.0.4389.23\\chromedriver.exe"}
browser = Browser('chrome', **executable_path, headless=False)


# Visit the mars nasa news site
url = 'https://data-class-mars.s3.amazonaws.com/Mars/index.html'
browser.visit(url)


# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# Convert the browser html to a soup object then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

# End the automated browsing session
browser.quit()