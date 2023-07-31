import streamlit as st
from GetInfo import *


def display_seasons():
    
    competitions_seasons = get_seasons(competition_selected)
    
    st.selectbox(
        'Elige la temporada',
        competition_seasons
    )

def web():
    st.title('Fubol⚽')
    st.subheader('Estadisticas y graficos de futbol')
    
    competiciones = get_competitions()
    
    selected_comp = st.selectbox(
        'Elige la competicion',
        competiciones,
        key='selected_comp'
    )
    
    if selected_comp in competiciones:
        st.write('En efecto este condicional funciona')
        
        competition_seasons = get_seasons(selected_comp)
        season = st.selectbox(
            'Elige la temporada',
            competition_seasons,
            key='season'
        )
    
    
    
    


if __name__ == "__main__":
    web()