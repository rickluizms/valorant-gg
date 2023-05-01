import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver 
from selenium.webdriver.firefox.options import Options

#AMERICAS
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

    df.to_csv("datasets/team_stats-americas.csv")

    driver.quit() 

def americas_teams():
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

    teams = {}

    for i in range(0, 10):
        resposta = respostas[i].get_text(" ", strip = True)
        teams['team', i] = resposta

    df = pd.DataFrame(list(teams.items()))
    df_save = df[1]
    df_save.to_csv("datasets/teams_americas.csv")

    driver.quit()


def americas_players():
    # Get content
    url = "https://www.vlr.gg/event/stats/1189/champions-tour-2023-americas-league"
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

    df.to_csv("datasets/player_stats.csv")

    driver.quit() 


def americas_matches():
    # Get content
    url = "https://www.vlr.gg/event/matches/1189/champions-tour-2023-americas-league/?series_id=2315"
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

    teams = {}

    for i in range(0, 10):
        resposta = respostas[i].get_text(" ", strip = True)
        teams['team', i] = resposta

    df = pd.DataFrame(list(teams.items()))
    df_save = df[1]
    df_save.to_csv("datasets/matches.csv")

    driver.quit()



def americas_agents():