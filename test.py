import requests
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time


import requests
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

chrome_options = Options()
# chrome_options.add_argument("--headless")
# chrome_options.add_argument(
#     '--user-agent="Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 640 XL LTE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10166"')
# chrome_options.add_argument("--window-size=1920x1080")
driver = webdriver.Chrome(options=chrome_options,
                          executable_path=ChromeDriverManager().install())

driver.get('https://www.google.com/maps')
driver.find_element_by_id('searchboxinput').send_keys('852 W Fulton Market St Chicago')
driver.find_element_by_id('searchbox-searchbutton').click()

time.sleep(5)


html2 = driver.page_source
html = BeautifulSoup(html2, "lxml", from_encoding="utf-8")

divs = html.find_all('div', {'role': 'link'})

for div in divs:
    print(div.find('div',{'class':'qBF1Pd-haAclf'}).text.strip())
    type_dv = div.find_all('div', {'class': 'ZY2y6b-RWgCYc'})

    if len(type_dv) >= 2:
        type_dv = type_dv[2]
        type = type_dv.find('span').text.strip()
        print(type)