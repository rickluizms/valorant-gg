import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver 
from selenium.webdriver.firefox.options import Options

def get_americas():
    # Get content
    url = "https://www.vlr.gg/event/1189/champions-tour-2023-americas-league"
    option = Options()
    option.add_argument("--headless=new")
    driver = webdriver.Firefox()

    driver.get(url)
    time.sleep(1)

    element = driver.find_element("xpath", "//div[@class='event-group mod-fullwidth']//table[@class='wf-table mod-simple mod-group']")
    html_content = element.get_attribute('outerHTML')

    # Parser HTML content
    soup = BeautifulSoup(html_content, 'html.parser')
    table = soup.find(name='table')


    # Make a dataframe
    df_full = pd.read_html(str(table))[0]
    df = df_full[['Unnamed: 0', 'W', 'L', 'T', 'MAP', 'RND', 'Δ']]
    df.columns = ['Team', 'Wins', 'Loss', 'Ties', 'MAP', 'RND', 'Δ']

    df.to_csv("team_stats-americas.csv")

    driver.quit() 

def get_emea():
    # Get content
    url = "https://www.vlr.gg/event/1190/champions-tour-2023-emea-league"
    option = Options()
    option.add_argument("--headless=new")
    driver = webdriver.Firefox()

    driver.get(url)
    time.sleep(1)

    element = driver.find_element("xpath", "//div[@class='event-group mod-fullwidth']//table[@class='wf-table mod-simple mod-group']")
    html_content = element.get_attribute('outerHTML')

    # Parser HTML content
    soup = BeautifulSoup(html_content, 'html.parser')
    table = soup.find(name='table')


    # Make a dataframe
    df_full = pd.read_html(str(table))[0]
    df = df_full[['Unnamed: 0', 'W', 'L', 'T', 'MAP', 'RND', 'Δ']]
    df.columns = ['Team', 'Wins', 'Loss', 'Ties', 'MAP', 'RND', 'Δ']

    df.to_csv("team_stats-emea.csv")

    driver.quit() 

def get_pacific():
    # Get content
    url = "https://www.vlr.gg/event/1191/champions-tour-2023-pacific-league"
    option = Options()
    option.add_argument("--headless=new")
    driver = webdriver.Firefox()

    driver.get(url)
    time.sleep(1)

    element = driver.find_element("xpath", "//div[@class='event-group mod-fullwidth']//table[@class='wf-table mod-simple mod-group']")
    html_content = element.get_attribute('outerHTML')

    # Parser HTML content
    soup = BeautifulSoup(html_content, 'html.parser')
    table = soup.find(name='table')


    # Make a dataframe
    df_full = pd.read_html(str(table))[0]
    df = df_full[['Unnamed: 0', 'W', 'L', 'T', 'MAP', 'RND', 'Δ']]
    df.columns = ['Team', 'Wins', 'Loss', 'Ties', 'MAP', 'RND', 'Δ']

    df.to_csv("team_stats-pacific.csv")    

    driver.quit() 

def get_players():
    # Get content
    url = "https://www.vlr.gg/stats"
    option = Options()
    option.add_argument("--headless=new")
    driver = webdriver.Firefox()

    driver.get(url)
    time.sleep(1)

    element = driver.find_element("xpath", "//div[@class='wf-card mod-table mod-dark']//table[@class='wf-table mod-stats mod-scroll']")
    html_content = element.get_attribute('outerHTML')

    # Parser HTML content
    soup = BeautifulSoup(html_content, 'html.parser')
    table = soup.find(name='table')

    # Make a dataframe
    df_full = pd.read_html(str(table))[0]
    df = df_full[['Player', 'Agents', 'Rnd', 'R',  'ACS', 'K:D', 'KAST', 'ADR', 'KPR', 'APR', 'FKPR', 'FDPR', 'HS%', 'CL%', 'CL', 'KMax', 'K', 'D', 'A', 'FK', 'FD']]
    df.columns = ['Player', 'Agents', 'Rnd', 'R',  'ACS', 'K:D', 'KAST', 'ADR', 'KPR', 'APR', 'FKPR', 'FDPR', 'HS%', 'CL%', 'CL', 'KMax', 'K', 'D', 'A', 'FK', 'FD']

    df.to_csv("player_stats.csv")

    driver.quit() 

def get_teams():
    # Get content
    url = "https://www.vlr.gg/stats"
    option = Options()
    option.add_argument("--headless=new")
    driver = webdriver.Firefox()

    driver.get(url)
    time.sleep(1)

    element = driver.find_element("xpath", "//div[@class='event-teams-container']//div[@class='wf-card event-team']//div[@class=event-team-players]")
    html_content = element.get_attribute('outerHTML')

    # Parser HTML content
    soup = BeautifulSoup(html_content, 'html.parser')
    table = soup.find(name='table')

    # Make a dataframe
    df_full = pd.read_html(str(table))[0]
    df = df_full[[]]
    df.columns = []

    df.to_csv("teams.csv")

    driver.quit()


get_teams()
get_americas()
get_emea()
get_pacific()
get_players()