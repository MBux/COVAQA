import streamlit as st
from multiapp import MultiApp
from src import home, dashboard, qa, streamlit
from src import api_data

app = MultiApp()

app.add_app("Home", home.app)
app.add_app("Dashboard", streamlit.app)
app.add_app("COVAQA", qa.app)
app.run()
