import requests
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time
import csv

import requests
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

chrome_options = Options()
chrome_options.add_argument("--headless")
# chrome_options.add_argument(
#     '--user-agent="Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 640 XL LTE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10166"')
# chrome_options.add_argument("--window-size=1920x1080")
driver = webdriver.Chrome(options=chrome_options,
                          executable_path=ChromeDriverManager().install())


with open('demo_1.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        temp = row
        address = temp[2]

        driver.get('https://www.google.com/maps')
        driver.find_element_by_id('searchboxinput').send_keys(str(address) + ' ' + str(temp[3]))
        driver.find_element_by_id('searchbox-searchbutton').click()

        time.sleep(3)

        html2 = driver.page_source
        html = BeautifulSoup(html2, "lxml", from_encoding="utf-8")

        divs = html.find_all('div', {'role': 'link'})


        for div in divs:
            heading = ''
            type = ''
            try:
                heading = div.find('div',{'class':'qBF1Pd-haAclf'}).text.strip()
                try:
                    type_dv = div.find_all('div',{'class':'ZY2y6b-RWgCYc'})

                    if len(type_dv) >=2:
                        type_dv = type_dv[2]
                        type= type_dv.find('span').text.strip()

                except:
                    print("Errp")

            except:
                print("eror")


            temp.append(heading)
            temp.append(type)


        row1 = []
        row1.append(temp)

        print(row1)

        # if len(row1) > 6 and row1[6] != '':
        with open('main1.csv', 'a+') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerows(row1)

        # else:
        #     with open('error.csv', 'a+') as csvfile:
        #         csvwriter = csv.writer(csvfile)
        #         csvwriter.writerows(row1)



