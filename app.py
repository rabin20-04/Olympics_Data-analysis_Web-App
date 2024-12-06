import streamlit as st
import pandas as pd

df = pd.read_csv('athlete_events.csv')
athletes_df = pd.read_csv('athlete_events.csv')
region_df = pd.read_csv('noc_regions.csv')
import preprocessor, helper

st.sidebar.header("Olympics Data Analysis")
df = preprocessor.preprocess(df, region_df)

user_menu = st.sidebar.radio(
    "Select an option",
    ("Medal Tally", "Overall Analysis", "Country-Wise-Analysis", "Athlete-Wise-Analysis"))

# --------

if user_menu == "Medal Tally":
    st.sidebar.header("Medal Tally")
    years, country = helper.country_year_list(df)
    selected_year = st.sidebar.selectbox("Select Year", years)
    selected_country = st.sidebar.selectbox("Select Country", country)
    medal_tally = helper.fetch_medal_tally(df, selected_country, selected_year)
    st.dataframe(medal_tally)
