import requests
from bs4 import BeautifulSoup
import time
import re


def fetch(url):
    time.sleep(1)
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5)" +
            "AppleWebKit/537.36 (KHTML, like Gecko)" +
            "Chrome/50.0.2661.102 Safari/537.36"
        }
        html = requests.get(url, headers=headers, timeout=3)

        if html.status_code == 200:
            return html.text

    except requests.ReadTimeout:
        return None


def scrape_novidades(html_content):
    try:
        soup = BeautifulSoup(html_content, "html.parser")
        soup.prettify()

        news = []
        for new in soup.find_all("div", {"class": "tec--list__item"}):
            news.append(
                new.find("a", {"class": "tec--card__thumb__link"})["href"]
            )

        return news

    except Exception:
        return []


def scrape_next_page_link(html_content):
    try:
        soup = BeautifulSoup(html_content, "html.parser")
        soup.prettify()

        button_pagination = soup.find(
            "a",
            {
                "class": "tec--btn tec--btn--lg" +
                " tec--btn--primary z--mx-auto z--mt-48"
            },
        )["href"]

        return button_pagination

    except Exception:
        return None


def parse_convert_string(string):
    temp = re.findall(r'\d+', string)
    list_num = list(map(int, temp))
    result = list_num.pop()
    return result


def get_title(soup):
    element = soup.find("h1", {"id": "js-article-title"})
    if element:
       return element.text

    return None


def get_timestamp(soup):
    element = soup.find("time", {"id": "js-article-date"})
    if element:
        return element["datetime"]

    return None


def get_writer(soup):
    element = soup.find("a", {"class": "tec--author__info__link"})
    element_alt = soup.find("div", {"class": "tec--timestamp__item z--font-bold"})
    element_leg = soup.find("div", {"id": "js-author-bar"})

    if element: 
        return element.text.strip()
    elif element_alt: 
        return element_alt.a.text.strip()
    elif element_leg:
        return element_leg.p.text.strip()

    return None


def get_shares(soup):
    element = soup.find("div", {"class": "tec--toolbar__item"})
    
    if element:
        element = parse_convert_string(element.text)
        return element

    return 0


def get_comments(soup):
    element = soup.find("button", {"id": "js-comments-btn"})

    if element:
        element = parse_convert_string(element.text)
        return element

    return 0

def get_summary(soup):
    element = soup.find("div", {"class": "tec--article__body"})

    if element:
        return element.p.text

    return None

def get_sources(soup):
    elements = soup.find("div", {"class": "z--mb-16"})
    list_sources = []

    if elements:
        for element in elements.div:
            list_sources.append(element.text.strip())

    list_sources = list(filter(lambda x: x != "", list_sources))

    return list_sources


def get_categories(soup):
    elements = soup.find("div", {"id": "js-categories"})
    list_categories = []

    if elements:
        for element in elements:
            list_categories.append(element.text.strip()) 

    list_categories = list(filter(lambda x: x != "", list_categories))

    return list_categories


def scrape_noticia(html_content):
    #links = scrape_novidades(html_content)
    soup = BeautifulSoup(html_content, "html.parser")
    soup.prettify()
    links = []
    new_dict = dict()
    
    links.append(soup.find("link", {"rel": "canonical"})['href'])


    for link in links:
        #html_page = fetch(link)
        #soup = BeautifulSoup(html_page, "html.parser")
        #soup.prettify()

        new_dict["url"] = link
        new_dict["title"] = get_title(soup)
        new_dict["timestamp"] = get_timestamp(soup)
        new_dict["writer"] = get_writer(soup)
        new_dict["shares_count"] = get_shares(soup)
        new_dict["comments_count"] = get_comments(soup)
        new_dict["summary"] = get_summary(soup)
        new_dict["sources"] = get_sources(soup)
        new_dict["categories"] = get_categories(soup)


    return new_dict


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
