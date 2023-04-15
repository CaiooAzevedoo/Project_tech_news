from tech_news.database import find_news
import datetime


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
    news = find_news()
    result = list()

    try:
        datetime.date.fromisoformat(date)
        # https://docs.python.org/3/library/datetime.html
    except ValueError:
        raise ValueError('Data inválida')

    day = date[8:10]
    month = date[5:7]
    year = date[0:4]
    formatted_date = f"{day}/{month}/{year}"

    for item in news:
        if (formatted_date == item['timestamp']):
            result.append((item['title'], item['url']))
    return result


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
