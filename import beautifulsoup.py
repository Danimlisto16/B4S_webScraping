from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

webpage_response = requests.get(
    'https://content.codecademy.com/courses/beautifulsoup/cacao/index.html')

webpage = webpage_response.content

soup = BeautifulSoup(webpage, "html.parser")
#print(soup)

#GET DATA
ratings = soup.find_all(attrs={"class": "Rating"})
chocolatiers = soup.find_all(attrs={"class": "Company"})
cocoa = soup.find_all(attrs={"class": "CocoaPercent"})
origin = soup.find_all(attrs={"class": "Origin"})
companyLocation = soup.find_all(attrs={"class": "CompanyLocation"})

ratings_list = []
chocNames_list = []
cocoa_list = []
origin_list = []
companyLocation_list = []

#TREAT DATA
for x in range(1, len(ratings)):
    ratings_list.append(float(ratings[x].get_text()))

for x in range(1, len(chocolatiers)):
    chocNames_list.append(chocolatiers[x].get_text())

for x in range(1, len(cocoa)):
    cocoa_list.append(float(cocoa[x].get_text().strip("%")))
    
for x in range(1, len(origin)):
    origin_list.append(origin[x].get_text())
    
for x in range(1, len(companyLocation)):
    companyLocation_list.append(companyLocation[x].get_text())
    
print(companyLocation)
#matplotlib
#plt.hist(ratings_list)
#plt.show()

d = {"Companies": chocNames_list, 
     "Rating": ratings_list, 
     "CocoaPercentage":cocoa_list,
     "Origin":origin_list,
     "Countries": companyLocation_list
     }
cacao_df = pd.DataFrame.from_dict(d)

print(cacao_df)

mean_ratings = cacao_df.groupby("Origin").Rating.mean()
ten_best = mean_ratings.nlargest(10)
print(ten_best)

#print(cacao_df)

'''
z = np.polyfit(cacao_df.CocoaPercentage, cacao_df.Rating, 1)
line_function = np.poly1d(z)
plt.plot(cacao_df.CocoaPercentage, line_function(cacao_df.CocoaPercentage), "r--")

plt.scatter(cacao_df.CocoaPercentage, cacao_df.Rating)
plt.show()
'''