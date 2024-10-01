from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.metalsdaily.com/live-prices/gold/').text
soup = BeautifulSoup(html_text,'lxml')
#print(soup)
gold_table = soup.find('table', class_='table table-striped')
