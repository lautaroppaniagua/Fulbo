import pandas as pd
from mplsoccer import VerticalPitch, Pitch
from statsbombpy import sb
import ssl
import ArgentineSoccerData as asd



ssl._create_default_https_context = ssl._create_unverified_context

df = pd.concat([sb.competitions(), asd.seasons()], join='outer', ignore_index=True)


def get_competitions():
    
    competitions = list(df.competition_name)
    return competitions 

def get_seasons(selected_comp):

    return list(df[df['competition_name'] == selected_comp]['season_name'])

def get_matches(selected_season, selected_comp)
    
    if 'Argentin' in selected_comp:
        df = asd.matches(selected_season)
    else:
        df = sb.competitions()
        df[(df['season_name'] == selected_season) & (df['competition_name'] == selected_comp)][['competition_id', 'season_id']]
    