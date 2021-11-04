from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from icecream import ic

print("======================================================================")
webpage_response = requests.get('https://medium.com/tag/python')

webpage = webpage_response.content

soup = BeautifulSoup(webpage, "html.parser")
print(soup.title.text)

titles = []
summary = []
links = []

#GET DATA
print("LINKS GOT")
links_with_text = []
number = 0

sopa = soup.select(".agk .il .y .jy")
for a in sopa:
    numer = number + 1
    print(number)
    texto = a['href']
    links.append(texto)

table = {"Enlaces": links}
resume_df = pd.DataFrame.from_dict(table)
print(resume_df)
