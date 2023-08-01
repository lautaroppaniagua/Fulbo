import streamlit as st
from GetInfo import *
import ssl


ssl._create_default_https_context = ssl._create_unverified_context


def web():
    st.title('Fulbo⚽')
    st.subheader('Estadisticas y graficos de futbol')
    
    competiciones = get_competitions()
    
    selected_comp = st.selectbox(
        'Elige la competicion',
        competiciones,
        key='selected_comp'
    )
    
    seasons = get_seasons(selected_comp)
    
    selected_season = st.selectbox(
        "Elige la temporada",
        seasons,
        key="selected_season"
    )
    
    matches = get_matches(selected_comp, selected_season)
    
    selected_match = st.selectbox(
        'Elige el partido',
        matches,
        key='selected_match'
    )

if __name__ == "__main__":
    web()