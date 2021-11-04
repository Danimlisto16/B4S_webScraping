html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
    <div>
        <div>
            <a href="http://example.com/elsie"  class="ay az ba bb bc bd be bf bg bh bi bj bk bl bm" id="link1">Elsie</a>,
        </div>
    </div>
<a href="http://example.com/elsie"  class="ay az ba bb bc bd be bf bg bh bi bj bk bl bm" id="link1">Elsie</a>, and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc, 'html.parser')
links = []
links = soup.find_all("a",
                      class_="er es et eu ev ew ex ey ez fa fb fc fd fe ff")
print(links)
