import pandas as pd
from mplsoccer import VerticalPitch, Pitch
import matplotlib.pyplot as plt
from statsbombpy import sb
import ssl
import re
import requests
from bs4 import BeautifulSoup



ssl._create_default_https_context = ssl._create_unverified_context


def get_competitions(years=False):
    
    competiciones = list(sb.competitions().competition_name.drop_duplicates())
    arg_data = pd.read_html("https://fbref.com/es/comps/21/historia/Temporadas-de-Primera-Division")[0] 
    competiciones.append(arg_data["Nombre de la competición"][0])
    
    return competiciones

def get_seasons(competition):

    if competition == "Argentine Primera División":
        df = pd.read_html("https://fbref.com/es/comps/21/historia/Temporadas-de-Primera-Division")[0]
        result = list(df.Temporada)
        
    else:
       
        df = sb.competitions()[sb.competitions()['competition_name'] == competition][['country_name','competition_name', 'season_name']]
        result = list(df.season_name)

    return result

def GetMatchesURL_Arg(URL_PartidosArg, df):
    
    Data = requests.get(URL_PartidosArg)
    soup = BeautifulSoup(Data.text, 'html.parser')
    enlaces = []
    for enlace in soup.find_all('td', {'data-stat': 'match_report'}):
        try:
            enlaces.append('https://fbref.com/' + enlace.a['href'])
        except:
            pass
        
    return enlaces[:df.index.max()+1]
    
    
    

def get_arg_matches(selected_season, TipoDataframe=False):

    
    URL_PartidosArg = f'https://fbref.com/es/comps/21/{selected_season}/horario/Marcadores-y-partidos-de-{selected_season}-Primera-Division'
    matches = pd.read_html(URL_PartidosArg)[0].dropna(subset=['Local'])
    matches['Informe del partido'] = GetMatchesURL_Arg(URL_PartidosArg, matches)

    if TipoDataframe:
        return matches
    else:
        matches = matches[['Fecha', 'Local', 'Visitante']].values.tolist()
        return [match[0] + ' | ' + match[1] + ' - ' + match[2] for match in matches]


def get_matches(selected_competition , selected_season):
    
    if selected_competition == 'Argentine Primera División':
        result = get_arg_matches(selected_season)
        
    else:
        
        df = sb.competitions()
        df = df[(df['competition_name'] == selected_competition) & (df['season_name'] == selected_season)]
        competition_id = df.competition_id.item()
        season_id = df.season_id.item()
        matches = sb.matches(competition_id, season_id)[['match_date', 'home_team','away_team','competition_stage']].sort_values('match_date', ascending=False).values.tolist()
        result = [match[0] + ' | ' + match[1] + ' - ' + match[2] + ' ' + match[3] for match in matches]
        
    return result
    
def get_match_report(selected_match, selected_season):

    RegexPatterns = {'Fecha': r"^(.*?)\s\|", 'Local': r"\|\s(.*?)\s-\s", 'Visitante': r"- (.*)$"}
    
    EquipoLocal = re.search(RegexPatterns['Local'], selected_match).group(1)
    EquipoVisitante = re.search(RegexPatterns['Visitante'], selected_match).group(1)
    Fecha = re.search(RegexPatterns['Fecha'], selected_match).group(1)
    
    df = get_arg_matches(selected_season, TipoDataframe=True)
    return [EquipoLocal, EquipoVisitante]
