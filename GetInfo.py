import pandas as pd
from mplsoccer import VerticalPitch, Pitch
import matplotlib.pyplot as plt
from statsbombpy import sb

def get_competitions():
    competiciones = list(sb.competitions().competition_name.drop_duplicates())
    for competicion in competiciones:
        oldest = sb.competitions()[sb.competitions()['competition_name'] == competicion].season_name.min()
        newest = sb.competitions()[sb.competitions()['competition_name'] == competicion].season_name.max()
        if oldest != newest:
            competiciones[(competiciones.index(competicion))] = competiciones[ (competiciones.index(competicion)) ] + " "+ str(oldest) + "-" + str(newest)
        else:
            competiciones[(competiciones.index(competicion))] = competiciones[ (competiciones.index(competicion)) ] + " "+ str(oldest)
    return competiciones

def get_seasons(competition):

    df = sb.competitions()[sb.competitions()['competition_name'] == competition][['country_name','competition_name', 'season_name']]
    return list(df.apply(lambda row: row['country_name']+ ' - '+row['competition_name'] + ' - '+ row['season_name'], axis=1))
