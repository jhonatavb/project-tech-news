import requests
from bs4 import BeautifulSoup
import time


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

    except len(news) == 0:
        return []


# Requisito 3
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

    except Exception as e: 
        return None


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
