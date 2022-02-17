import re


def parse_convert_string(string):
    temp = re.findall(r"\d+", string)
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
    element_alt = soup.find(
        "div", {"class": "tec--timestamp__item z--font-bold"}
    )
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
    element_text = " ".join(re.findall("[a-zA-Z]+", element.text))

    if element_text == 'Compartilharam':
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
