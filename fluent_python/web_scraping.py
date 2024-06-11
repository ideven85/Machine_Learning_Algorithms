from urllib.error import HTTPError, URLError
from urllib.request import urlopen

from bs4 import BeautifulSoup


def open(path):
    try:
        html = urlopen(path)
    except HTTPError|URLError as e:
        print(e)
    else:
        print("Working")
        return html

URL='https://www.pythonscraping.com/pages/page3.html'
html = open(URL)

bs = BeautifulSoup(html,'html.parser')


for sibling in list(bs.find('table',{'id':'giftList'}).tr.next_siblings):
    print(sibling)