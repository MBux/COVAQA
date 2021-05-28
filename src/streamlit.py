# Reference

# https: // www.analyticsvidhya.com/blog/2021/02 building-a-covid-19-dashboard-using-streamlit-and-python/

# https: // analyticsindiamag.com/a-beginners-guide-to-streamlit-convert-python-code-into-an-app/


import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt


def readInFile(data):
    # load the data file
    # TODO When possible apply it to use an API
    # TODO change your own directory
    try:
        df = st.cache(pd.read_csv)(
            data)
    except Exception:
        raise Exception("File or directory `{}` not found.".format(data))
    return df


def displayTotalCases(df):
    # display the entire CSV file
    is_check = st.checkbox("Display total cases of Variance of Concern")
    if is_check:
        st.write(df)


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


def displayData(df):
    select = st.sidebar.selectbox(
        'Select a graph to display total number of cases per state', ['Bar plot', 'Pie chart'], key='1')
    isCheck = st.sidebar.checkbox("Display")

    if isCheck:
        st.title("Total number of cases per State")

        if select == 'Pie chart':
            fig = px.pie(
                df, values=df['Cases'][:], names=df['State'][:], title='')
            st.plotly_chart(fig)

        if select == 'Bar plot':
            fig = go.Figure(data=[
                go.Bar(name='State', x=df['State'][:], y=df['Cases'][:])])
            st.plotly_chart(fig)


def main():
    dataset = "../datasets/Cases of Variants of Concern in the United States.csv"

    # Titles for main page and sidebars
    st.title("COVAQA")
    st.markdown('Dashboard for COVID-19 Information')
    st.sidebar.title("Visualization Selector")

    df = readInFile(dataset)

    displayTotalCases(df)
    displayData(df)
    displayStatesVariables(df)


if __name__ == "__main__":
    main()
