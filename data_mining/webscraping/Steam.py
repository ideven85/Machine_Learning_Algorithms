import requests
import lxml.html
import html5lib
import bs4

html = requests.get("https://store.steampowered.com/explore/new/")
doc = lxml.html.fromstring(html.content)
