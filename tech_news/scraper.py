import requests
from time import sleep
from requests import HTTPError, ReadTimeout


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
    """Seu código deve vir aqui"""


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
