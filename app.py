import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

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
    st.title("Olympics in :blue[Numbers]")
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
        st.header("Host Cities")
        st.title(cities)
    with col3:
        st.header("Total Sports")
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
    fig1 = px.line(nations_over_time, x="Year", y="No.of Countries",markers=True)
    st.plotly_chart(fig1)
    st.markdown("--------------------------------------------------------------------------------")
    st.header("No.of events occurring over the Years")
    events_over_time = helper.events_played_overtime(df)
    fig2 = px.line(events_over_time, x="Year", y="No. of Events",markers=True)
    st.plotly_chart(fig2)
    st.markdown("--------------------------------------------------------------------------------")
    st.header("Athletes participation over the Years")
    athletes_participating_overtime = helper.athletes_participating_overtime(df)
    fig3 = px.line(athletes_participating_overtime, x="Year", y="Athletes",markers=True)
    st.plotly_chart(fig3)
    st.markdown("--------------------------------------------------------------------------------")
    st.header("Events overall representation(Every sports) Year to Sports")
    st.markdown(" #### Just found out! ")
    st.markdown("-  Cricket has only been played once in the history of the modern Olympics.")
    st.markdown("-  Taekwondo was recently added to the Olympics in 2000.")
    fig, ax = plt.subplots(figsize=(16, 16))
    x = df.drop_duplicates(["Year", "Sport", "Event"])
    heatmap_fig = sns.heatmap(
        x.pivot_table(index="Sport", columns="Year", values="Event", aggfunc="count").fillna(0).astype("int"),
        annot=True)
    st.pyplot(fig)

    st.markdown("----------")
    st.header("Most successful Athletes")
    sport_list = df["Sport"].unique().tolist()
    sport_list.sort()
    sport_list.insert(0, "Overall")
    selected_sport = st.selectbox("Select a sport", sport_list)
    y = helper.most_successful(df, selected_sport)
    st.table(y)


if user_menu == "Country-Wise-Analysis":
    st.header(":orange[Countries Performance] in Olympics")
    st.markdown("_________")
    country_list = df["region"].dropna().unique().tolist()
    country_list.sort()

    st.sidebar.title("Country")
    selected_country = st.sidebar.selectbox( "Select a :blue[country] :green[eg. USA]",country_list)
    plot_df=helper.country_vs_medal_graph(df, selected_country)
    fig4 = px.line(plot_df, x="Year", y="Medals",markers=True)
    st.title(selected_country+ " :blue[Medal tally] over the years")
    st.plotly_chart(fig4)
