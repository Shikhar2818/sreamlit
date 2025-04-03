
import streamlit as st


from front import main as front_main
from music import main as music_main
from sport import main as sport_main
from calc import main as calc_main
from games import main as games_main

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Select a page:", ("Front", "Games","Music","Sport","Calculator",))

# Load the selected page
if page == "Front":
    front_main()
elif page == "Games":
    games_main()
elif page == "Music":
    music_main()
elif page == "Sport":
    sport_main()
elif page == "Calculator":
    calc_main()

