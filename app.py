import streamlit as st
from multiapp import MultiApp
from src import home, dashboard, qa

app = MultiApp()

app.add_app("Home", home.app)
app.add_app("Dashboard", dashboard.app)
app.add_app("COVAQA", qa.app)
app.run()