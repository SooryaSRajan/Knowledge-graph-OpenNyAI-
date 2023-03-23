from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.service import Service
import webdriver_manager.chrome
from selenium import webdriver
from bs4 import BeautifulSoup
import re

option = webdriver.ChromeOptions()
option.add_argument("start-maximized")
option.add_argument("--window-size=1920x1080")
option.add_argument("--verbose")
caps = DesiredCapabilities().CHROME

doc_url = []

driver = webdriver.Chrome(service=Service(webdriver_manager.chrome.ChromeDriverManager().install()), options=option,
                          desired_capabilities=caps)

count = 0
while count < 2:
    driver.get(
        'https://indiankanoon.org/search/?formInput=motor%20vehicle%20%20%20%20doctypes%3A%20judgments&pagenum=' + str(
            count))
    # get page source
    page_source = driver.page_source

    # parse page source
    soup = BeautifulSoup(page_source, 'html.parser')
    for link in soup.find_all('div', class_='result_title'):
        print(link)
        for a in link.find_all('a', href=True):
            a['href'] = re.findall(r'\d+', a['href'])[0]
            doc_url.append('https://indiankanoon.org/doc/' + a['href'])

    # keep counting until page source is empty or not found
    count += 1

print(doc_url)

#write to file
with open('doc_url.json', 'w') as f:
    for item in doc_url:
        f.write("%s " % item)