import re

import requests
from bs4 import BeautifulSoup
import os
from PIL import Image

example_html = """
<html>
<head>
<title>Your Title Here</title>
</head>
<body bgcolor="#ffffff">
<center>
<img align="bottom" src="clouds.jpg"/>
</center>
<hr/>
<a href="http://somegreatsite.com">Link Name</a> is a link to
another nifty site
<h1>This is a Header</h1>
<h2>This is a Medium Header</h2>
Send me mail at <a href="mailto:support@yourcompany.
com">support@yourcompany.com</a>.
<p>This is a paragraph!</p>
<p>
<b>This is a new paragraph!</b><br/>
<b><i>This is a new sentence without a paragraph break, in bold
italics.</i></b>
<a>This is an empty anchor</a>
</p>
<hr/>
</body>
</html>
"""
URL = "https://en.wikipedia.org/wiki/Margrethe_II"
response = requests.get(URL)
print(response.status_code)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    # print(soup.prettify())
    links = soup.find_all("a", href=True)
    out = []
    with open("wiki_margaritha_links.txt", "w") as fp:
        for link in links:
            if link["href"].startswith("http"):
                fp.write(link["href"] + "\n")
            else:
                fp.write(URL + link["href"] + "\n")
