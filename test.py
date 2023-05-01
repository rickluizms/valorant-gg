import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver 
from selenium.webdriver.firefox.options import Options
import getUrl

class scrap():

    def __init__(self):
        self.score
        self.teams
        self.players
        self.matches
        self.agents


    def get_overview(region):
        #ELEMENT01
        # Get content
        url = getUrl.get.overviewUrl(region)
        option = Options()
        option.add_argument("--headless=new")
        driver = webdriver.Firefox()

        driver.switchTo(url)
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

        df.to_csv(f"datasets/{region}-score.csv")



        #ELEMENT2

        element2 = driver.find_element("xpath", "//div[@class='event-teams-container']")
        html_content2 = element2.get_attribute('outerHTML')

        # Parser HTML content
        soup2 = BeautifulSoup(html_content2, 'html.parser')


        atributes = {'class': 'wf-card event-team'}
        respostas2 = soup2.find_all("div", attrs=atributes)

        teams2 = {}

        for i in range(0, 10):
            resposta2 = respostas2[i].get_text(" ", strip = True)
            teams2['team', i] = resposta2

        df = pd.DataFrame(list(teams2.items()))
        df_save = df[1]
        df_save.to_csv("datasets/"+region+"-teams.csv")

        driver.quit()  
        return
    
    def get_stats(region):
        # Get content
        url = getUrl.get.statsUrl(region)
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

        df.to_csv("datasets/"+region+"-players-stats.csv")

        driver.quit()
        return
    
    def get_matches(region):
        # Get content
        url = getUrl.get.matchesUrl(region)
        option = Options()
        option.add_argument("--headless=new")
        driver = webdriver.Firefox()

        # Make a dataframe
        df_full = pd.read_html(str(table))[0]
        df = df_full[[]]
        df.columns = []

        df.to_csv("datasets/"+region+"-matches.csv")

        #driver.quit()
        return
    
    def get_agents(region):
        # Get content
        url = getUrl.get.agentsUrl(region)
        option = Options()
        option.add_argument("--headless=new")
        driver = webdriver.Firefox()

        # Make a dataframe
        df_full = pd.read_html(str(table))[0]
        df = df_full[[]]
        df.columns = []

        df.to_csv("datasets/"+region+"-agents.csv")

        #driver.quit()
        return
    
    def exit_web(region):
        driver.quit()
