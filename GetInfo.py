import pandas as pd
from mplsoccer import VerticalPitch, Pitch
import matplotlib.pyplot as plt
from statsbombpy import sb
import ssl


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

def get_matches(selected_competition , selected_season):
    
    if selected_competition == 'Argentine Primera División':
        
        pass
    else:
        
        df = sb.competitions()
        df = df[(df['competition_name'] == selected_competition) & (df['season_name'] == selected_season)]
        competition_id = df.competition_id.item()
        season_id = df.season_id.item()
        matches = sb.matches(competition_id, season_id)[['match_date', 'home_team','away_team','competition_stage']].sort_values('match_date', ascending=False).values.tolist()
        
    return [match[0] + ' | ' + match[1] + '-' + match[2] + ' ' + match[3] for match in matches]
    
