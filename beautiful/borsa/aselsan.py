#https://www.digitalocean.com/community/tutorials/how-to-scrape-web-pages-with-beautiful-soup-and-python-3
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import geckodriver_autoinstaller


geckodriver_autoinstaller.install()  # Check if the current version of geckodriver exists
                                     # and if it doesn't exist, download it automatically,
                                     # then add geckodriver to path

driver = webdriver.Firefox()
driver.get("http://www.python.org")
assert "Python" in driver.title


page = requests.get('https://www.investing.com/equities/aselsan-historical-data')
soup = BeautifulSoup(page.text, 'html.parser')
print(soup)
ts=soup.table
print(ts.tr.td)
tds=ts.tr.td
print(tds)

