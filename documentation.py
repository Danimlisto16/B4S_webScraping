from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from icecream import ic

webpage_response = requests.get('https://medium.com/tag/python')

webpage = webpage_response.content
soup = BeautifulSoup(webpage, "html.parser")

for a in soup.find_all("a", id=False, class_="er es et eu ev ew ex ey ez fa fb fc fd fe ff"):
    print("enlace: " , a['href'] , "\n")
    