import requests
from bs4 import BeautifulSoup
import re

SITE = "https://www.merlininkazani.com"
page = requests.get(SITE)

soup = BeautifulSoup(page.content, "html.parser")

mainLinks = soup.find_all('a')
mainUrls = [tag['href'] for tag in mainLinks if 'href' in tag.attrs and 'oyun/' in tag['href']]
mainUrls = list(dict.fromkeys(mainUrls))

subUrls = list()
for url in mainUrls:
    print("Getting this url=>" + SITE + url)
    subPage = requests.get(SITE + url)
    subPageSoup = BeautifulSoup(subPage.content, 'html.parser')
    subTags = subPageSoup.find_all('a')
    subUrls = [tag['href'] for tag in subTags if 'href' in tag.attrs and bool(re.search(r'\w-\d', tag['href']))]


for sUrl in subUrls:
    contentPage = requests.get(SITE + sUrl)
    contentSoup = BeautifulSoup(contentPage.content, 'html.parser')
    contentText = contentSoup.find('div', class_='text detail-content-custom')
   # if not isinstance(contentText.get_text(), type(None)):
    print(contentText.get_text())