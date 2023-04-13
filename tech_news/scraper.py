import requests
from time import sleep
from requests import HTTPError, ReadTimeout
# from bs4 import BeautifulSoup
from parsel import Selector


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
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
