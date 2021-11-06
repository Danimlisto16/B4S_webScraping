from bs4 import BeautifulSoup
import requests
import pandas as pd
from icecream import ic
import pdfkit
import os
from datetime import date
import re


#define class tags to be scraping
divClass = "hn l"
h2TitleClass = "az be hp hq hr hs ht hu hv hw hx hy hz ia ib ic id ie if ig ih ii hd hf hg ij hi hj bc"
h3SummaryClass = "az b fl ep hd ik hf hg ij hi hj ee"
aLinkClass = "er es et eu ev ew ex ey ez fa fb fc fd fe ff"

# define the name of the directory to be created

def url2pdf(url, name):
    today = date.today()
    path = str(today) + "/"
    try:
        if (not os.path.isdir(path)):
            os.mkdir(path)
        pdfkit.from_url(url, path + str(name) + ".pdf")
        return True
    except BaseException as e:
        print("Error: ", e)
        return False


class article():
    def __init__(self, title, summary, link):
        self.title = title
        self.summary = summary
        self.link = link


def cleanTitle(title):
    s = re.sub('[^A-Za-z0-9]+', ' ', title)
    return s


def checkUrl(url):
    if url.find("https://") != -1:
        return url
    else:
        return "https://medium.com/" + url


#las etiquetass suelen cambiar luego de copiar el link, trabajar
#con las etiquetas  que aparecen despues de pegar aqui el enlace
webpage_response = requests.get('https://medium.com/tag/python')

webpage = webpage_response.content
soup = BeautifulSoup(webpage, "html.parser")
articles = []

i = 1
for divs in soup.find_all(
        "div", id=False,
        class_=divClass):  #get all articles from web called ae fm
    try:
        title = divs.findChildren(
            "h2",
            recursive=True,
            id=False,
            class_=
            h2TitleClass
        )
        
        for child in title:
            titleText = child.string  #get text in h2
        summary = divs.findChildren(
            "h3",
            recursive=True,
            id=False,
            class_=h3SummaryClass)
        
        for child in summary:
            summaryText = child.string  #get text in h3
        link = divs.findChildren(
            "a",
            recursive=True,
            id=False,
            class_=aLinkClass,
            href=True)
        for child in link:
            a = child  #get all a tag in div
            #print("enlace ",a['href'],"\n")
        linkText = a['href']

        articleObj = article(titleText, summaryText, linkText)
        articles.append(articleObj)

    except BaseException as e:
        print(e)

totalItems = len(articles)
correct = 0
wrong = 0

#TODO extract 2 a Tags cause one of them brings the correct link
#TODO find other way to download webPDF
iterador = 0
for i in articles:
    print(
        "================================= ITEM ====================================="
    )
    print("Título:  " + i.title)
    print("Resumen: " + i.summary)
    print("Enlace: " + i.link)
    print(
        "============================================================================"
    )
    if (url2pdf(checkUrl(i.link), cleanTitle(i.title))):
        correct = correct + 1
    else:
        wrong = wrong + 1
    iterador = iterador + 1
print(".......REPORT.......")
print("CORRECT: " + str(correct), "\nWRONG: " + str(wrong),
      "\nTOTAL: " + str(totalItems))
