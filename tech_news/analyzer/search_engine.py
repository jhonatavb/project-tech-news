from tech_news.database import search_news
from datetime import datetime


def search_by_title(title):
    search_list = search_news({"title": {"$regex": title, "$options": "i"}})

    list_tuple = list()

    if search_list:
        list_tuple.append((search_list[0]["title"], search_list[0]["url"]))

    return list_tuple


def search_by_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")

    list_tuple = list()
    date_list_new = search_news({"timestamp": {"$regex": date}})

    if date_list_new:
        list_tuple.append((date_list_new[0]["title"], date_list_new[0]["url"]))

    return list_tuple


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
