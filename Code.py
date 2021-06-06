from enum import EnumMeta
from re import T
from bs4 import BeautifulSoup

import requests
import time
import csv

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

html_page = requests.get(START_URL).text

time.sleep(10)

headers = ["Apparent Magnitude", "Proper Name", "Bayer Designation",
           "Distance", "Spectral Class", "Mass", "Radius", "Luminosity"]

star_data = []


def scrape():
    soup = BeautifulSoup(html_page, 'html.parser')

    tr_tags = soup.find_all('tr')
    tr_tags.pop(0)

    for count, tr_tag in enumerate(tr_tags):
        temp_list = []
        for index, td_tag in enumerate(tr_tag.find_all('td')):
            value = 0
            if index == 0 or index == 3:
                if count <= 4 and index != 3:
                    try:
                        value = td_tag.contents[2].replace('\n', '')
                    except:
                        value = ""

                else:
                    try:
                        value = td_tag.contents[1].replace('\n', '')
                    except:
                        value = td_tag.contents[0].replace('\n', '')

            else:
                try:
                    value = td_tag.find_all(
                        'a')[0].contents[0].replace('\n', '')
                except:
                    value = td_tag.contents[0].replace('\n', '')

            temp_list.append(value)
        star_data.append(temp_list)


scrape()
print(star_data)

with open(r'Projects\C127\venv\data.csv', 'w+', encoding="utf-8") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(star_data)
