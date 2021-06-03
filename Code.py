from bs4 import BeautifulSoup

import requests
import time
import csv

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

html_page = requests.get(START_URL)

time.sleep(10)

headers = ["Apparent Magnitude", "Proper Name", "Bayer Designation",
           "Distance", "Spectral Class", "Mass", "Radius", "Luminosity"]

star_data = []


def scrape():
    soup = BeautifulSoup(html_page.text, 'html.parser')

    temp_list = []
    star_data = soup.find('table')
    table_rows = star_data.find_all('tr')
    for tr_tag in table_rows:
        for td_tags in tr_tag.find_all("td"):
            for index, td_tag in enumerate(td_tags):
                print(td_tag)
                if index == 0:
                    temp_list.append(td_tag)
                else:
                    try:
                        temp_list.append(td_tag.contents[0])
                    except:
                        temp_list.append("")

            # print(temp_list)


scrape()
