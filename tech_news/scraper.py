import requests
from time import sleep
from requests import HTTPError, ReadTimeout
# from bs4 import BeautifulSoup
from parsel import Selector
import re


# Requisito 1
def fetch(url):
    headers = {"user-agent": "Fake user-agent"}
    try:
        sleep(1)
        response = requests.get(url, timeout=3, headers=headers)
        response.raise_for_status()
        return response.text
    except (HTTPError, ReadTimeout):
        return None


# Requisito 2
def scrape_updates(html_content):
    urls = list()
    selector = Selector(html_content)
    for url in selector.css('h2.entry-title a::attr(href)'):
        urls.append(url.get())
    return urls


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    link = selector.css('a.next::attr(href)').get()
    if (link is None):
        return None
    return link


# Requisito 4
def scrape_news(html_content):
    selector = Selector(html_content)

    url = selector.css('link[rel=canonical]::attr(href)').get()
    title = selector.css('h1.entry-title::text').get()
    timestamp = selector.css('li.meta-date::text').get()
    writer = selector.css('span.author a::text').get()
    reading_time = selector.css('li.meta-reading-time::text').get()
    summary = selector.css('div.entry-content p').get()
    category = selector.css('div.meta-category span.label::text').get()

    return {
        'url': url,
        'title': title.rstrip(),
        'timestamp': timestamp,
        'writer': writer,
        'reading_time': int(reading_time.split(' ')[0]),
        'summary': re.sub('<.*?>', '', summary).rstrip(),
        # https://www.pythontutorial.net/python-regex/python-regex-sub/
        'category': category
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
