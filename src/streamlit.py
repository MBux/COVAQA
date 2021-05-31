# Reference

# https: // www.analyticsvidhya.com/blog/2021/02 building-a-covid-19-dashboard-using-streamlit-and-python/

# https: // analyticsindiamag.com/a-beginners-guide-to-streamlit-convert-python-code-into-an-app/

# https://plotly.com/python/mapbox-county-choropleth/#data-indexed-by-id


import json
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from urllib.request import urlopen
from src import api_data


def readInFile(data):
    try:
        df = st.cache(pd.read_csv)(
            data)
    except Exception:
        raise Exception("File or directory `{}` not found.".format(data))
    return df


def totalVaccines():
    df = api_data.get_vax_by_state()
    fig = px.bar(df, x='location', y='people_vaccinated',
                 labels={'location': 'States',
                         'people_vaccinated': 'People Vaccinated'},
                 height=400)
    st.header('People Vaccinated By State', )
    st.plotly_chart(fig)


def displayStatesVariables(df):
    # Create a filed for selecting multiple States
    states = st.sidebar.multiselect(
        "Enter states for which you would like to see the data", df['State'].unique())

    # Create a field for Entering variable to compare
    var = st.sidebar.multiselect("Enter the Fields", df.columns)

    # Display selected variables per states
    selectedStates = df[(df['State'].isin(states))]
    statesData = selectedStates[var]
    isCheck = st.sidebar.checkbox("Display the data of selected States")
    if isCheck:
        st.write(statesData)


def newCasesOfVariantsTable(df):
    new_df = df[df.columns.difference(['filter'])]
    new_df = pd.DataFrame(new_df[new_df.columns[::-1]])
    # display the entire CSV file
    with st.beta_expander("Display Total Cases of Variants"):
        st.write(new_df)


def newCasesOfVariantsCharts(df):
    select = st.sidebar.selectbox(
        'Select a graph to display the total number of new cases of variants per state', ['Bar plot', 'Pie chart'], key='1')
    isCheck = st.sidebar.checkbox("Display")

    if isCheck:
        st.header("Total Number of New Cases of Variants per State")

        if select == 'Pie chart':
            fig = px.pie(df, names='State', values='Cases')
            st.plotly_chart(fig)

        if select == 'Bar plot':
            fig = px.bar(df, x='State', y='Cases', labels={'State': 'States',
                                                           'Cases': 'Total new Variants'},
                         height=400)
            st.plotly_chart(fig)


def newCasesPerCounty():
    # Load a GeoJSON file containing the geometry information for US counties
    with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
        counties = json.load(response)

    # Load the most recent data (30 days) for every county:
    # Format:
    # date, county, state, fips, cases, deaths
    # 2020-01-21, Snohomish, Washington, 53061, 1, 0
    df = pd.read_csv("https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties-recent.csv",
                     dtype={"fips": str})

    fig = px.choropleth_mapbox(df, geojson=counties, locations='fips', hover_name='county', color='cases',
                               color_continuous_scale="sunsetdark",
                               range_color=(0, 10000),
                               mapbox_style="carto-positron",
                               zoom=2.5, center={"lat": 37.0902, "lon": -95.7129},
                               opacity=0.5,
                               labels={'cases': 'Cases'}
                               )
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

    with st.beta_expander("Total Number of New Cases per County"):
        # Add the date of the last raw of the file: the most recent one
        st.write("As of: ", df.iloc[-1:, :].date.to_string(index=False))
        st.plotly_chart(fig)


def newDeathsPerCounty():
    # Load a GeoJSON file containing the geometry information for US counties
    with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
        counties = json.load(response)

    # Load the most recent data (30 days) for every county:
    # Format:
    # date, county, state, fips, cases, deaths
    # 2020-01-21, Snohomish, Washington, 53061, 1, 0
    df = pd.read_csv("https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties-recent.csv",
                     dtype={"fips": str})

    fig = px.choropleth_mapbox(df, geojson=counties, locations='fips', hover_name='county', color='deaths',
                               color_continuous_scale="sunsetdark",
                               range_color=(0, 10000),
                               mapbox_style="carto-positron",
                               zoom=2.5, center={"lat": 37.0902, "lon": -95.7129},
                               opacity=0.5,
                               labels={'deaths': 'Deaths'}
                               )
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

    with st.beta_expander("Total Number of New Deaths per County"):
        # Add the date of the last raw of the file: the most recent one
        st.write("As of: ", df.iloc[-1:, :].date.to_string(index=False))
        st.plotly_chart(fig)


# def main():
#     dataset = "data/CDC_Cases_of_Variants_of_Concern_in_the_United_States.csv"

#     # Titles for main page and sidebars
#     st.title("COVAQA")
#     st.markdown('Dashboard for COVID-19 Information')
#     st.sidebar.title("Visualization Selector")

#     df = readInFile(dataset)

#     displayTotalCases(df)
#     displayData(df)
#     displayStatesVariables(df)
#     displayTotalVaccines()
#     totalNewCasesPerCounty()


# if __name__ == "__main__":
#     main()


def app():
    dataset = "data/CDC_Cases_of_Variants_of_Concern_in_the_United_States.csv"

    # Titles for main page and sidebars
    st.title("COVAQA - Dashboard")
    st.markdown('Dashboard for COVID-19 Information')
    st.sidebar.title("Visualization Selector")

    df = readInFile(dataset)

    newCasesOfVariantsTable(df)
    newCasesPerCounty()
    newDeathsPerCounty()
    # displayStatesVariables(df)
    totalVaccines()
    newCasesOfVariantsCharts(df)
