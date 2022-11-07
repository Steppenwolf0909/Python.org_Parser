import requests
from bs4 import BeautifulSoup


if __name__ == '__main__':
    html = requests.get('https://www.python.org/')
    page = html.text
    soup = BeautifulSoup(page)
    shrubbery = soup.find(
        "div", {"class": "shrubbery"}
    )
    ul = shrubbery.find(
        "ul", {"class": "menu"}
    )
    lis = ul.find_all("li")
    for li in lis:
        event = li.find("a")
        print(event.text)


