import streamlit as st
from GetInfo import *


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

    Report = get_match_report(selected_match, selected_season)

    col1, col2 = st.columns(2)

    with col1:
        
        try:
            st.image(r"src/Argentina/{}.png".format(Report[0].lower().replace(' ', '')), width=350)
        except:
            st.image(r'src/sinfoto.png',width=350)

        st.header(Report[0].upper())

    with col2:

        try:
            st.image(r"src/Argentina/{}.png".format(Report[1].lower().replace(' ', '')), width=350)
        except:
            st.image(r'src/sinfoto.png',width=350)
        st.header(Report[1].upper())

    
    
    

if __name__ == "__main__":
    web()