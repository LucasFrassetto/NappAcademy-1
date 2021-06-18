from bs4 import BeautifulSoup
from urllib import request
import requests
import mechanicalsoup

data = request.urlopen('https://www.nappsolutions.com.br/').read().decode()
soup = BeautifulSoup(data, "html.parser")
print(soup.title)
soup.find_all('a')


request1 = requests.get('https://www.nappsolutions.com.br/')
soup2 = BeautifulSoup(request1.text, "html.parser")
print(soup2.title)
soup2.find_all('a')


browser = mechanicalsoup.StatefulBrowser()
browser.open('https://www.nappsolutions.com.br/')
print(browser.page.title)
browser.page.find_all('a')


data = request.urlopen('http://127.0.0.1:8000/').read().decode()
soup = BeautifulSoup(data, "html.parser")
print(soup.title)
soup.find_all('div')
