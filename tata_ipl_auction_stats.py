import requests
from bs4 import BeautifulSoup
import pandas as pd

url="https://www.iplt20.com/auction/2022"
r=requests.get(url)

soup=BeautifulSoup(r.text,"html.parser")
table=soup.find("table",class_="ih-td-tab auction-tbl")
title=table.find_all("th",attrs={'class':'skip-filter'})
header=[]
for i in title:
    name=i.text
    header.append(name)
    
df=pd.DataFrame(columns=header)
# print(df)

rows=table.find_all("tr")
# print((rows))
for i in rows[1:]:
    first_td=i.find_all("td")[0].find("div",class_="ih-pt-ic").text.strip()
    data=i.find_all("td")[1:]
    row=[tr.text for tr in data]
    row.insert(0, first_td)
    l=len(df)
    df.loc[l]=row
    
df.to_csv("ipl Auction Stats.csv")