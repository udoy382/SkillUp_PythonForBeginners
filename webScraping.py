# Web Scraping using Python


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re


url = "https://www.hubertiming.com/results/2018MLK"  # Open link
html = urlopen(url)


soup = BeautifulSoup(html)
# print(soup)


title = soup.title
# print(title.text)


links = soup.find_all('a')
# print(links)


# for link in links:
#     print(link("href"))


allrows = soup.find_all("tr")
# print(allrows)
# print(allrows[5])


"""
data = []
for row in allrows:
    row_list = row.find_all("td")
    dataRow = []
    for cell in row_list:
        dataRow.append(cell.text)
    data.append(dataRow)

# print(data)
# print(data[5])
"""

"""
header_list = []
col_headers = soup.find_all("th")
for col in col_headers:
    header_list.append(col.text)
print(header_list)
"""

"""
url2 = "saifurrahmanudoy.netlify.app"  # Open my website link
html = urlopen(url)

soup2 = BeautifulSoup(html)
print(soup2)
"""
