# References

# https: // www.analyticsvidhya.com/blog/2021/02 building-a-covid-19-dashboard-using-streamlit-and-python/

# https: // analyticsindiamag.com/a-beginners-guide-to-streamlit-convert-python-code-into-an-app/

# https://plotly.com/python/mapbox-county-choropleth/#data-indexed-by-id


import json
import streamlit as st
import pandas as pd
import plotly.express as px
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
    fig = px.bar(df, x='location', y='people_vaccinated_per_hundred',
                 labels={'location': 'States',
                         'people_vaccinated_per_hundred': 'Percentage of People Vaccinated'},
                 height=400)
    st.header('People Vaccinated By State', )
    st.plotly_chart(fig)


def newCasesOfVariantsTable():
    df = readInFile(
        "data/Formatted_CDC_Cases_of_Variants_of_Concern_in_the_United_States.csv")

    # Display the entire CSV file and total cases for each variant
    with st.beta_expander("Display Total Cases of Variants"):
        st.write(df)
        x = df.sum()
        st.write('B.1.1.7 Total: ', x.T.iloc[1],
                 'P.1 Total: ', x.T.iloc[2],
                 'B.1.351 Total: ', x.T.iloc[3]
                 )
        st.markdown(
            "Do you want to know more about variants? [Click here](https://www.cdc.gov/coronavirus/2019-ncov/variants/variant.html?CDC_AA_refVal=https%3A%2F%2Fwww.cdc.gov%2Fcoronavirus%2F2019-ncov%2Ftransmission%2Fvariant.html)")


def newCasesOfVariantsCharts():
    df = readInFile(
        "data/Formatted_CDC_Cases_of_Variants_of_Concern_in_the_United_States.csv")

    select = st.sidebar.selectbox(
        'Select a graph to display the total number of new cases of variants per state', ['Bar plot', 'Pie chart'], key='1')
    isCheck = st.sidebar.checkbox("Display", key='1')

    if isCheck:
        st.header("Total Number of New Cases of Variants per State")

        if select == 'Pie chart':
            fig = px.pie(df, names='State', values='Total Cases')

        if select == 'Bar plot':
            fig = px.bar(df, x='State', y='Total Cases',
                         labels={'State': 'States', 'Total Cases': 'Total new Variants'}, height=400)

        fig.update_traces(textposition='inside')
        st.plotly_chart(fig)


def typesOfVariantsCharts():
    df = readInFile(
        "data/Formatted_CDC_Cases_of_Variants_of_Concern_in_the_United_States.csv")

    select = st.sidebar.selectbox(
        'Select a variant to display state by state', ['P.1', 'B.1.351', 'B.1.1.7'], key='2')
    isCheck = st.sidebar.checkbox("Display", key='2')

    if isCheck:
        if select == 'P.1':
            st.header("P.1 Variant in the US")
            fig = px.pie(df, names='State', values='P.1')

        if select == 'B.1.351':
            st.header("B.1.351 Variant in the US")
            fig = px.pie(df, names='State', values='B.1.351')

        if select == 'B.1.1.7':
            st.header("B.1.1.7 Variant in the US")
            fig = px.pie(df, names='State', values='B.1.1.7')

        fig.update_traces(textposition='inside')
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
        st.markdown(
            "Do you want to know more about how the virus spread? [Click here](https://www.cdc.gov/coronavirus/2019-ncov/prevent-getting-sick/how-covid-spreads.html)")


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
        st.markdown(
            "Do you want to know more about mortality from COVID-19? [Click here](https://www.cdc.gov/nchs/covid19/mortality-overview.htm)")


def deathsByAgeGroups():
    df = readInFile(
        "https://data.cdc.gov/resource/hk9y-quqm.csv")

    st.header("COVID-19 Deaths by Age Groups in the US")
    fig = px.pie(df, names='age_group', values='covid_19_deaths')
    fig.update_traces(textposition='inside')
    # Add the date of the last raw of the file: the most recent one
    date = df.iloc[-1:,
                   :].data_as_of.to_string(index=False).split('T')[0]

    st.write("As of: ", date)
    st.plotly_chart(fig)


def app():
    # Titles for dashboard page and sidebar
    st.title("COVAQA - Dashboard")
    st.markdown('Dashboard for COVID-19 Information')
    st.sidebar.title("Visualization Selector")

    newCasesOfVariantsTable()
    newCasesPerCounty()
    newDeathsPerCounty()
    totalVaccines()
    deathsByAgeGroups()
    newCasesOfVariantsCharts()
    typesOfVariantsCharts()
