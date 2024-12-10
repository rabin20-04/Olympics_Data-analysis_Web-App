import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns

df = pd.read_csv('athlete_events.csv')
athletes_df = pd.read_csv('athlete_events.csv')
region_df = pd.read_csv('noc_regions.csv')
import preprocessor, helper

st.sidebar.title("Olympics Data Analysis")
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

if user_menu == "Overall Analysis":
    st.title("TOP STATISTICS")
    editions = df["Year"].unique().shape[0] - 1
    cities = df["City"].unique().shape[0]
    sports = df["Sport"].unique().shape[0]
    events = df["Event"].unique().shape[0]
    athletes = df["Name"].unique().shape[0]
    nations = df["region"].unique().shape[0]

    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Editions")
        st.title(editions)
    with col2:
        st.header("Cities")
        st.title(cities)
    with col3:
        st.header("Sports")
        st.title(sports)

    col5, col7, col6 = st.columns(3)

    with col5:
        st.header("Events")
        st.title(events)
    with col7:
        st.header("Nations")
        st.title(nations)
    with col6:
        st.header("Athletes")
        st.title(athletes)
    st.markdown("--------------------------------------------------------------------------------")
    st.header("Participation of the countries over the Years")
    nations_over_time = helper.participating_nation_overtime(df)
    fig1 = px.line(nations_over_time, x="Year", y="No.of Countries")
    st.plotly_chart(fig1)
    st.markdown("--------------------------------------------------------------------------------")
    st.header("No.of events occurring over the Years")
    events_over_time = helper.events_played_overtime(df)
    fig2 = px.line(events_over_time, x="Year", y="No. of Events")
    st.plotly_chart(fig2)
    st.markdown("--------------------------------------------------------------------------------")
    st.header("Athletes participation over the Years")
    athletes_participating_overtime = helper.athletes_participating_overtime(df)
    fig3 = px.line(athletes_participating_overtime, x="Year", y="Athletes")
    st.plotly_chart(fig3)
    st.markdown("--------------------------------------------------------------------------------")
    st.header("Events overall representation over the Years")
    overtime = helper.events_overall_representation(df)
    fig3 = sns.heatmap(overtime,annot=True)
    st.plotly_chart(fig3)
