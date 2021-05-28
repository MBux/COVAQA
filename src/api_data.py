import pandas as pd
import numpy as np
import plotly
import requests
import io

STATES = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado",
          "Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois",
          "Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland",
          "Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana",
          "Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York",
          "North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania",
          "Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah",
          "Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]


def get_vax_by_state():
    url = 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/us_state_vaccinations.csv'
    response = requests.get(url).content
    vaxdata = pd.read_csv(io.StringIO(response.decode('utf-8')))
    vaxdata.date = pd.to_datetime(vaxdata.date)
    recent = vaxdata.date.max()
    query = "date == '{}' and location in {}".format(recent, STATES)
    first = vaxdata.query(query)
    return first
