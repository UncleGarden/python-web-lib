# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

#url = raw_input('Enter - ')
#url = 'http://python-data.dr-chuck.net/known_by_Fikret.html'
url = 'http://python-data.dr-chuck.net/known_by_Amin.html'
times = 0

def parse_url(url, times):
    if times == 7:
        return

    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)

    # Retrieve all of the anchor tags
    count = 0
    tags = soup('a')
    for tag in tags:

        count += 1
        if count == 18:
            next_link = tag.get('href', None)
            print next_link
            parse_url(next_link, times+1)

parse_url(url, times)