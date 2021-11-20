import requests
from bs4 import BeautifulSoup
import re
import json

url = 'https://www.osta.ee/kategooria/arvutid/komponendid'
json_file = {'items': []}
counter = 0


def parse(url, json_file=None, counter=None):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    items = soup.find_all("li", class_='col-md-4 mb-30')

    for item in items:
        data = {'Title': item.h3.get_text().strip(),
                'Price': re.sub("[^0-9€.]+", "", item.find('div', class_='offer-thumb__price--current').text),
                'Picture href': item.find('figure', class_="offer-thumb__image").img['data-original']}
        item_number = 'item_' + str(counter)
        data_with_number = {item_number: []}
        data_with_number[item_number].append(data)
        json_file['items'].append(data_with_number)
        counter += 1

    try:
        next_page = 'https://www.osta.ee/' + soup.find("a", class_="icon next page-link")['href']
        if next_page:
            parse(next_page, json_file, counter)
    except KeyError:  # No more pages.
        with open('components.txt', 'w', encoding='utf-8') as outfile:
            json.dump(json_file, outfile, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    parse(url, json_file, counter)
