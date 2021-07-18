from urllib.parse import urljoin

import requests

BASE = 'http://wp8m3he1wt.s3-website-ap-southeast-2.amazonaws.com'
ENDPOINT = '/api/products/1'
INDUSTRY_WEIGHT_FACTOR = 250
session = requests.session()


def driver_function(urls, category):
    """
    :param urls:
    :param category:
    :return: float
    """
    weights = list()
    for u in urls:
        response = session.get(u)
        weights.extend(
            filter_weights_from_categories(
                json=response.json()["objects"], category=category
            ))
    return average_equation(weights)


def average_equation(weights):
    """
    :param weights:
    :return: float
    """
    divisor = float(len(weights))
    total = sum(map(float, weights))
    average = (total / divisor) if total !=0 else 0
    return round(average, 3)


def get_urls():
    """
    :return: List of valid urls to hit.
    """
    pages = list()
    pages.append(ENDPOINT)
    endpoint = ENDPOINT

    while True:
        response = session.get(urljoin(BASE, endpoint))
        endpoint = response.json()["next"]
        pages.append(endpoint)
        if not endpoint:
            pages.pop(-1)
            session.close()
            break
    urls = list()
    for p in pages:
        urls.append(urljoin(BASE, p))
    return urls


def filter_weights_from_categories(json, category):
    """
    :param json:
    :param category:
    :return: list
    """
    return [calculate_cubic_weight(c["size"]) for c in json if c["category"] == category]


def calculate_cubic_weight(size):
    """
    :param size:
    :return: float
    """
    length = size["length"] / 100.0
    height = size["height"] / 100.0
    width = size["width"] / 100.0
    return width * length * height * INDUSTRY_WEIGHT_FACTOR

