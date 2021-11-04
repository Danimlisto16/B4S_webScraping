from bs4 import BeautifulSoup
import requests
import pandas as pd
from icecream import ic
import pdfkit

def url2pdf(url,name):
    try:
        pdfkit.from_url(url,
                        "./pdfArticles/"+"ARTICLE_"+name + ".pdf")
        return True
    except BaseException as e:
        print("Error: " ,e)
        return False

class article():
    def __init__(self, title,summary, link):
        self.title = title
        self.summary = summary
        self.link = link

#las etiquetass suelen cambiar luego de copiar el link, trabajar
#con las etiquetas  que aparecen despues de pegar aqui el enlace
webpage_response = requests.get('https://medium.com/tag/python')

webpage = webpage_response.content
soup = BeautifulSoup(webpage, "html.parser")
articles = []

i = 1
for divs in soup.find_all("div", id=False, class_="hk l"): #get all articles from web called ae fm
    try:
        title = divs.findChildren("h2" ,recursive = True ,id=False ,class_="az be hm hn ho hp hq hr hs ht hu hv hw hx hy hz ia ib ic id ie if hc he hf ig hh hi bc")
        for child in title:
            titleText = child.string #get text in h2    
        summary = divs.findChildren("h3" ,recursive = True ,id=False ,class_="az b fl ep hc ih he hf ig hh hi ee")
        for child in summary:
            summaryText = child.string #get text in h3
        link = divs.findChildren("a",recursive = True, id=False, class_="er es et eu ev ew ex ey ez fa fb fc fd fe ff",href = True)
        for child in link: 
            a = child #get all a tag in div
            #print("enlace ",a['href'],"\n")
        linkText = a['href']
        
        articleObj = article(titleText,summaryText, linkText)
        articles.append(articleObj)
        
    except BaseException as e:
        print(e)

totalItems = len(articles)
correct = 0
wrong = 0

#TODO extract 2 a Tags cause one of them brings the correct link
#TODO find other way to download webPDF  

for i in articles: 
    print("================================= ITEM =====================================")
    print("Título:  "+ i.title)
    print("Resumen: "+ i.summary)
    print("Enlace: " + i.link)
    print("============================================================================")
    if(url2pdf(i.link,i.title)):
        correct = correct + 1
    else:
        wrong = wrong + 1
print(".......REPORT.......")
print("CORRECT: "+ str(correct), "WRONG: "+ str(wrong),"TOTAL: "+ str(totalItems))