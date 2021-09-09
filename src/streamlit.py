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
                 color_discrete_sequence=px.colors.sequential.Aggrnyl,

                 labels={'location': 'States',
                         'people_vaccinated_per_hundred': 'Percentage of People Vaccinated'}, height=400)

    with st.expander('People Vaccinated By State', expanded=True):
        # Add the date of the last raw of the file: the most recent one
        st.write("As of: ", df.iloc[-1:, :].date.to_string(index=False))
        st.plotly_chart(fig, use_container_width=True)


def newCasesOfVariantsTable():
    df = readInFile(
        "data/Formatted_CDC_Cases_of_Variants_of_Concern_in_the_United_States.csv")

    # Display the entire CSV file and total cases for each variant
    with st.expander("Total Cases of Variants", expanded=True):
        st.write(df)
        x = df.sum()
        st.write('B.1.1.7 Total: ', x.T.iloc[1],
                 'P.1 Total: ', x.T.iloc[2],
                 'B.1.351 Total: ', x.T.iloc[3]
                 )
        st.write("As of: 2021-04-21")
        st.markdown(
            "Do you want to know more about variants? [Click here](https://www.cdc.gov/coronavirus/2019-ncov/variants/variant.html?CDC_AA_refVal=https%3A%2F%2Fwww.cdc.gov%2Fcoronavirus%2F2019-ncov%2Ftransmission%2Fvariant.html)")


def newCasesOfVariantsCharts():
    df = readInFile(
        "data/Formatted_CDC_Cases_of_Variants_of_Concern_in_the_United_States.csv")

    select = st.sidebar.selectbox(
        'Select a graph to display the total number of new cases of variants per state', ['Bar plot', 'Pie chart'], key='1')

    if select == 'Pie chart':
        fig = px.pie(df, names='State', values='Total Cases')

    if select == 'Bar plot':
        fig = px.bar(df, x='State', y='Total Cases',
                     color_discrete_sequence=px.colors.sequential.Agsunset,
                     labels={'State': 'States', 'Total Cases': 'Total new Variants'}, height=400)

    fig.update_traces(textposition='inside')
    with st.expander('Total Number of New Cases of Variants per State', expanded=True):
        st.write("As of: 2021-04-21")
        st.plotly_chart(fig, use_container_width=True)


def typesOfVariantsCharts():
    df = readInFile(
        "data/Formatted_CDC_Cases_of_Variants_of_Concern_in_the_United_States.csv")

    select = st.sidebar.selectbox(
        'Select a variant to display state by state', ['P.1', 'B.1.351', 'B.1.1.7'], key='2')

    if select == 'P.1':
        fig = px.pie(df, names='State', values='P.1',
                     color_discrete_sequence=px.colors.sequential.Viridis)

    if select == 'B.1.351':
        fig = px.pie(df, names='State', values='B.1.351',
                     color_discrete_sequence=px.colors.sequential.Plotly3)

    if select == 'B.1.1.7':
        fig = px.pie(df, names='State', values='B.1.1.7',
                     color_discrete_sequence=px.colors.sequential.Cividis)

    fig.update_traces(textposition='inside')
    with st.expander('Selected Varaint State by State', expanded=True):
        st.write("As of: 2021-04-21")
        st.plotly_chart(fig, use_container_width=True)


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

    with st.expander("Total Number of New Cases per County", expanded=True):
        # Add the date of the last raw of the file: the most recent one
        st.write("As of: ", df.iloc[-1:, :].date.to_string(index=False))
        st.plotly_chart(fig, use_container_width=True)
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
                               color_continuous_scale="bluyl",
                               range_color=(0, 10000),
                               mapbox_style="carto-positron",
                               zoom=2.5, center={"lat": 37.0902, "lon": -95.7129},
                               opacity=0.5,
                               labels={'deaths': 'Deaths'}
                               )
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

    with st.expander("Total Number of New Deaths per County", expanded=True):
        # Add the date of the last raw of the file: the most recent one
        st.write("As of: ", df.iloc[-1:, :].date.to_string(index=False))
        st.plotly_chart(fig, use_container_width=True)
        st.markdown(
            "Do you want to know more about mortality from COVID-19? [Click here](https://www.cdc.gov/nchs/covid19/mortality-overview.htm)")


def deathsByAgeGroups():
    df = readInFile(
        "https://data.cdc.gov/resource/hk9y-quqm.csv")

    df = df.iloc[220:230]  # only cases with covid-19 reported as condition

    fig = px.pie(df, names='age_group', values='covid_19_deaths',
                 color_discrete_sequence=px.colors.sequential.Aggrnyl)
    fig.update_traces(textposition='inside')
    # Add the date of the last raw of the file: the most recent one
    date = df.iloc[-1:,
                   :].data_as_of.to_string(index=False).split('T')[0]

    with st.expander('COVID-19 Deaths by Age Groups in the US', expanded=True):
        st.write("As of: ", date)
        st.plotly_chart(fig, use_container_width=True)


def app():
    st.sidebar.title("Selector for variants")

    newCasesOfVariantsTable()
    typesOfVariantsCharts()
    newCasesOfVariantsCharts()
    newCasesPerCounty()
    newDeathsPerCounty()
    totalVaccines()
    deathsByAgeGroups()
