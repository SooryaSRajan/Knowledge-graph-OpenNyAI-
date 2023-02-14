from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
caps = DesiredCapabilities().CHROME
options.add_argument("--window-size=1920x1080")
options.add_argument("--verbose")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options, desired_capabilities=caps)
url = "https://indiankanoon.org/search/?formInput=vehicle&pagenum=9"
driver.get(url)
print(driver.page_source)
# driver.switch_to.new_window('window')


