import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver 
from selenium.webdriver.firefox.options import Options

# Get content
url = "https://www.vlr.gg/event/1189/champions-tour-2023-americas-league/regular-season"
option = Options()
option.add_argument("--headless=new")
driver = webdriver.Firefox()

driver.get(url)
time.sleep(1)

element = driver.find_element("xpath", "//div[@class='event-teams-container']")
html_content = element.get_attribute('outerHTML')

# Parser HTML content
soup = BeautifulSoup(html_content, 'html.parser')


atributes = {'class': 'wf-card event-team'}
respostas = soup.find_all("div", attrs=atributes)
content = respostas[0].get_text()
print(content)



driver.quit()