import re
import requests
from urllib import URLopener
from bs4 import BeautifulSoup

opener = URLopener()
dl_count = 0


def get_a_game(permalink):
    global dl_count

    print 'Scraping {}...'.format(permalink)
    response = requests.get(permalink)
    response.raise_for_status()

    matches = re.search('"(http://mirrors\.coreduo\.me\.uk/.+?)"', response.text)
    if matches:
        dl_url = matches.group(1)
        dl_name = dl_url.replace('http://mirrors.coreduo.me.uk/', './result/')

        filesize = -1
        try:
            hd = requests.head(dl_url)
            filesize = int(hd.headers['content-length'])
        except Exception:
            pass

        dl_count += 1
        print '#{}: Saving "{}" to "{}". Wait for {:,} bytes...'.format(
            dl_count, dl_url, dl_name, filesize)

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
