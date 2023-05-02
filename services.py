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

        df.to_csv(f"datasets/{region}-score.csv")


        #ELEMENT2 - GET PLAYERS

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
        driver = webdriver.Firefox()

        driver.get(url)
        time.sleep(1)

        element = driver.find_element("css selector", ".col")
        html_content = element.get_attribute('outerHTML')

        # Parser HTML content
        soup = BeautifulSoup(html_content, 'html.parser')


        atributes = {'class': 'match-item-vs'}
        respostas = soup.find_all("div", attrs=atributes)


        matches = {}

        if region == "emea":
            num = 45
        else:
            num = 55

        for i in range(0, num):
            resposta = respostas[i].get_text(" ", strip = True)
            matches['matches', i] = resposta

        df = pd.DataFrame(list(matches.items()))
        df_save = df[1]
        df_save.to_csv("datasets/"+region+"-matches.csv")
        
        driver.quit()
        return
    
    def get_agents(region):
        # Get content
        url = getUrl.get.agentsUrl(region)
        driver = webdriver.Firefox()

        driver.get(url)
        time.sleep(1)

        element = driver.find_element("css selector", ".mod-pr-global")
        html_content = element.get_attribute('outerHTML')

        # Parser HTML content
        soup = BeautifulSoup(html_content, 'html.parser')
        table = soup.find(name='table')

        
        # Make a dataframe
        df_full = pd.read_html(str(table))[0]

        df = df_full[['Map', '#', 'ATK WIN', 'DEF WIN', 'Unnamed: 5', 'Unnamed: 6', 'Unnamed: 7', 'Unnamed: 8', 'Unnamed: 9',
                      'Unnamed: 10', 'Unnamed: 11', 'Unnamed: 12', 'Unnamed: 13', 'Unnamed: 14', 'Unnamed: 15', 'Unnamed: 16',
                      'Unnamed: 17', 'Unnamed: 18', 'Unnamed: 19', 'Unnamed: 20', 'Unnamed: 21', 'Unnamed: 22', 'Unnamed: 23',
                      'Unnamed: 24',
                    ]]
        
        agents = []

        for i in range (0, 20):

            images_content = soup.findAll('img')[i]
            images = images_content.get("src")
            slice_img = images[21:-4]
            
            agents.append(slice_img)
            
        df.columns = [['pos', 's','Map', '#', 'ATK WIN', 'DEF WIN',f'{agents[0]}', f'{agents[1]}', f'{agents[2]}', f'{agents[3]}', 
                    f'{agents[4]}', f'{agents[5]}', f'{agents[6]}', f'{agents[7]}', f'{agents[9]}', f'{agents[10]}', f'{agents[11]}',
                    f'{agents[12]}', f'{agents[13]}', f'{agents[14]}', f'{agents[15]}', f'{agents[16]}', f'{agents[17]}', f'{agents[18]}'
                    f'{agents[19]}']]

        df.to_csv(f"datasets/{region}-agents.csv")
        
        driver.quit()
        return  
    
