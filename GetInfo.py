import pandas as pd
from mplsoccer import VerticalPitch, Pitch
from statsbombpy import sb
import ssl
from ArgentineSoccerData import ArgentineSoccer
import re



ssl._create_default_https_context = ssl._create_unverified_context

asd = ArgentineSoccer()
df = pd.concat([sb.competitions(), asd.seasons()], join='outer', ignore_index=True)


def get_competitions():
    
    competitions = list(df.competition_name)
    return competitions 

def get_seasons(selected_comp):

    return list(df[df['competition_name'] == selected_comp]['season_name'])

def get_matches(selected_season, selected_comp):
    
    if 'Argentin' in selected_comp:
        result = asd.matches(selected_season)
    else:
        df = sb.competitions()
        df = df[(df['season_name'] == selected_season) & (df['competition_name'] == selected_comp)][['competition_id', 'season_id']]
        result = sb.matches(df.values[0][0], df.values[0][1])

    return result 
    
def get_matchreport(selected_comp, selected_match, matches_df):

    regex = {"date": r"^(.*?)\s\|",
    "local_team": r"\|\s(.*?)\s-\s",

    date = re.search(regex['date'], selected_match).group(1)
    local_team = re.search(regex['local_team'], selected_match).group(1)

    if 'Argentin' in selected_comp:
        
        matches_df[(matches_df['match_date'] == date) & (matches_df['home_team'] == local_team)]['Informe del partido']