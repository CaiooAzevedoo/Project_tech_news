from tech_news.database import find_news


# Requisito 7
def search_by_title(title):
    news = find_news()
    result = list()
    for item in news:
        if (title.upper() in item['title'].upper()):
            result.append((item['title'], item['url']))
    return result


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
