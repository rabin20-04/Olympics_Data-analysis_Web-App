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
    if selected_year != "Overall" and selected_country != "Overall":
        st.header("Medal Tally of " + selected_country + " in the Year " + str(selected_year))
    elif selected_year != "Overall" and selected_country == "Overall":
        st.header("Overall Medal Tally in the year " + str(selected_year))
    elif selected_year == "Overall" and selected_country == "Overall":
        st.header("Overall Medal Tally")
    elif selected_year == "Overall" and selected_country != "Overall":
        st.header("Overall Performance of " + selected_country)

    st.table(medal_tally)


if user_menu =="Overall Analysis":
    editions=df["Year"].unique().shape[0]-1
    cities=df["City"].unique().shape[0]
    sports=df["Sports"].unique().shape[0]
    events=df["Event"].unique().shape[0]
    athletes=df["Name"].unique().shape[0]
    nations=df["region"].unique().shape[0]

