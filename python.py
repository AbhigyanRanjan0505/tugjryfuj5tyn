import time
import requests
from bs4 import BeautifulSoup
import pandas
import csv

url = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

time.sleep(10)

page = requests.get(url)

soup = BeautifulSoup(page.text, "html.parser")

star_table = soup.find_all("table")
table_rows = star_table[4].find_all("tr")

temp_list= []
for tr in table_rows:
    td = tr.find_all("td")
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

Star_names = []
Distance = []
Mass = []
Radius = []

for i in range(1, len(temp_list)):
    Star_names.append(temp_list[i][0])
    Distance.append(temp_list[i][5])
    Mass.append(temp_list[i][7])
    Radius.append(temp_list[i][8])

df = pandas.DataFrame(list(zip(Star_names, Distance, Mass, Radius)), columns=["Star_name", "Distance", "Mass", "Radius"])
df.to_csv("List_of_brown_dwarfs.csv")