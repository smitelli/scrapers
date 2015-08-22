import urllib
import urllib2
from bs4 import BeautifulSoup


def parse_page(url):
    body = urllib2.urlopen(url).read()
    soup = BeautifulSoup(body, 'html.parser')

    episodes = soup.find_all('div', class_='liContainer')
    for episode in episodes:
        yield episode.find('a')['href']


def parse_episode(url):
    body = urllib2.urlopen(url).read()
    soup = BeautifulSoup(body, 'html.parser')

    mp3 = soup.find('a', class_='downloadLink')['href']
    title = soup.find('h1', class_='mainTitle').find('span').string

    # This website sucks.
    title = title.strip()
    title = title[5:]
    title = title.replace(': ', ' - ')

    return (mp3, title)


opener = urllib.URLopener()
for page in xrange(17):
    url = 'http://podcast.getwebreader.com/cartalk/505/{}'.format(page + 1)

    print 'Reading {}'.format(url)
    for episode_url in parse_page(url):
        mp3, title = parse_episode(episode_url)

        print 'Downloading "{}" from {}'.format(title, mp3)
        realmp3 = urllib2.urlopen(mp3).geturl()
        opener.retrieve(realmp3, './result/{}.mp3'.format(title))
