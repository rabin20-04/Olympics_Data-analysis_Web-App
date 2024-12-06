import streamlit as st
import pandas as pd
df=pd.read_csv('athlete_events.csv')
athletes_df=pd.read_csv('athlete_events.csv')
region_df=pd.read_csv('noc_regions.csv')
import preprocessor,helper

df=preprocessor.preprocess(df,region_df)

user_menu=st.sidebar.radio(
    "Select an option",
    ("Medal Tally","Overall Analysis","Country-Wise-Analysis","Athlete-Wise-Analysis"))
# --------

if user_menu=="Medal Tally":
    st.header("Medal Tally")
    years,country=helper.country_year_list(df)
    selected_year=st.sidebar.selectbox("Select Year",years)
    selected_country=st.sidebar.selectbox("Select Country",country)
    medal_tally=helper.medal_tally(df)
    st.dataframe(medal_tally)