from tech_news.database import search_news


def search_by_title(title):
    list_search = search_news({"title": {"$regex": title, "$options": "i"}})

    list_tuple = list()

    if list_search:
        list_tuple.append((list_search[0]["title"], list_search[0]["url"]))

    return list_tuple


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
