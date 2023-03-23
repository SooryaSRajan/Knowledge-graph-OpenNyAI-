from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.service import Service
import webdriver_manager.chrome
from selenium import webdriver
from bs4 import BeautifulSoup
import re

import sys
sys.path.append('my/path/to/module/folder')

#print path to module folder

print(sys.path)

option = webdriver.ChromeOptions()
option.add_argument("start-maximized")
option.add_argument("--window-size=1920x1080")
option.add_argument("--verbose")
caps = DesiredCapabilities().CHROME

doc_url = []

driver = webdriver.Chrome(service=Service(webdriver_manager.chrome.ChromeDriverManager().install()), options=option,
                          desired_capabilities=caps)

count = 0
while count < 1:
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

driver.quit()

for url in doc_url:

    option = webdriver.ChromeOptions()
    option.add_argument('--headless')
    option.add_argument('--disable-gpu')  # Last I checked this was necessary.
    driver = webdriver.Chrome(service=Service(webdriver_manager.chrome.ChromeDriverManager().install()), options=option, desired_capabilities=caps)
    driver.get(url)

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    data = {}

    try:
        title = soup.find('div', class_='doc_title').text
    except:
        title = ''
    try:
        author = soup.find('div', class_='doc_author').text
    except:
        author = ''

    data['title'] = title
    data['author'] = author

    text = ''

    for p in soup.find_all('p', id=re.compile('^p_')):
        p_id = re.findall(r'\d+', p['id'])[0]
        text += p.text

    text = re.sub(r'[\n\t]', '', text)
    text = re.sub(r'[\*#@$]', '', text)
    text = re.sub(r'[\xa0]', '', text)

    data['text'] = text
    print(data)

doc = []

#write to JSON file
with open('data.json', 'w') as outfile:
    json.dump(doc, outfile)
