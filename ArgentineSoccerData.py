import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

class ArgentineSoccer:

    def seasons(self):
        df = pd.read_html("https://fbref.com/es/comps/21/historia/Temporadas-de-Primera-Division")[0]
        df.rename(columns={'Nombre de la competición': 'competition_name', 'Temporada':'season_name'}, inplace=True)
        return df
    
    def matches (self, season):

        URL_PartidosArg = f'https://fbref.com/es/comps/21/{season}/horario/Marcadores-y-partidos-de-{season}-Primera-Division'
        matches = pd.read_html(URL_PartidosArg)[0].dropna(subset=['Local']).reset_index()

        #Agregando links a informes

        Data = requests.get(URL_PartidosArg)
        soup = BeautifulSoup(Data.text, 'html.parser')
        enlaces = []
        for enlace in soup.find_all('td', {'data-stat': 'match_report'}):
            try:
                enlaces.append('https://fbref.com/' + enlace.a['href'])
            except:
                pass
                
        matches['Informe del partido'] = enlaces[:matches.index.max()+1]
        matches.rename(columns={'Fecha':'match_date', 'Local':'home_team', 'Visitante':'away_team'}, inplace=True)

        return matches

    def get_matchreport(matches_df):

        URL = matches_df[(matches_df['match_date'] == date) & (matches_df['home_team'] == local_team)]['Informe del partido']
        