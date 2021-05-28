import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import pydeck as pdk
from pycountry_convert import country_alpha2_to_country_name, country_name_to_country_alpha3

# SETTING PAGE CONFIG TO WIDE MODE
#st.beta_set_page_config(layout="wide")

# LOADING DATA
# DATE_TIME = "date/time"
# DATA_URL = (
#     "http://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz"
# )

@st.cache(persist=True)
# def load_data(nrows):
#     data = pd.read_csv(DATA_URL, nrows=nrows)
#     lowercase = lambda x: str(x).lower()
#     data.rename(lowercase, axis="columns", inplace=True)
#     data[DATE_TIME] = pd.to_datetime(data[DATE_TIME])
#     return data

# data = load_data(100000)
# 'data', data
# hour = 13
# data = data[data[DATE_TIME].dt.hour == hour]
# 'by hour', data

# LOAD DATA
# DATA_URL = (
#     "https://covid19.who.int/WHO-COVID-19-global-data.csv"
# )


data = pd.read_csv(DATA_URL)
# data = data[data["Country_code"] == "AF"]
# Country Code 'XA' is not recognized by pycountry convert so I'm removing it
# data = data[data['Country_code'] != 'XA']
# data = data[data['Country_code'] != 'XK']
# data['Country_code'] = data['Country_code'].apply(lambda x: country_name_to_country_alpha3(country_alpha2_to_country_name(x)))
# country = 'Afghanistan'
# c_code= 'AF'
# data = data[data["Country_code"] == c_code]

'## Data from country:', data

# LOAD DATA
# DATA_URL = (
#     "https://data.cdc.gov/api/views/saz5-9hgg/rows.csv"
# )
# @st.cache(persist=True)
# def load_data():
#     data = pd.read_csv(DATA_URL)
#     return data

# data = load_data()
# data

