import re
import requests
from urllib import URLopener
from bs4 import BeautifulSoup

opener = URLopener()


def get_a_game(permalink):
    print 'Scraping {}...'.format(permalink)
    response = requests.get(permalink)
    response.raise_for_status()

    matches = re.search('"(http://mirrors\.coreduo\.me\.uk/.+?)"', response.text)
    if matches:
        dl_url = matches.group(1)
        dl_name = dl_url.replace('http://mirrors.coreduo.me.uk/', './result/')

        print 'Saving {} to {}...'.format(dl_url, dl_name)
        opener.retrieve(dl_url, dl_name)
    else:
        print 'UH-OH, no download matches on page!'


page = 1
while True:
    print 'On page {}...'.format(page)
    response = requests.get('http://coreduo.me.uk/category/games/feed/?paged={}'.format(page))
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')
    for item in soup.find_all('item'):
        for link in item.find_all('link'):
            get_a_game(link.string)

    page += 1
