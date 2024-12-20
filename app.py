import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.figure_factory as ff

athletes_df = pd.read_csv("csv_files/athlete_events.csv")
df = athletes_df
region_df = pd.read_csv("csv_files/noc_regions.csv")
import preprocessor, helper

df = preprocessor.preprocess(df, region_df)


st.sidebar.image("others/Olympic_Rings.svg", caption=None, width=100)
st.sidebar.title("Olympics Data Analysis")



user_menu = st.sidebar.radio(
    ":grey[Select an option]",
    (
        "Medal Tally",
        "Overall Analysis",
        "Country-Wise-Analysis",
        "Athlete-Wise-Analysis",
    ),
)

if user_menu == "Medal Tally":
    st.sidebar.header(":violet[Medal Tally]")
    years, country = helper.country_year_list(df)
    selected_year = st.sidebar.selectbox("Select Year", years)
    selected_country = st.sidebar.selectbox("Select Country", country)
    st.sidebar.markdown(
        ":grey[Table presents the various :orange[Medal] achievements of selected Nation]"
    )
    medal_tally = helper.fetch_medal_tally(df, selected_country, selected_year)
    if selected_year != "Overall" and selected_country != "Overall":
        st.header(
            "Medal Tally of " + selected_country + " in the Year " + str(selected_year)
        )
    elif selected_year != "Overall" and selected_country == "Overall":
        st.header("Overall Medal Tally in the year " + str(selected_year))
    elif selected_year == "Overall" and selected_country == "Overall":
        st.header("Overall Medal Tally")
    elif selected_year == "Overall" and selected_country != "Overall":
        st.header("Overall Performance of " + selected_country)

    st.table(medal_tally)
    st.markdown('<hr style="border: 1px dashed #555555;">', unsafe_allow_html=True)
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

    st.markdown('<hr style="border: 1px solid #555555;">', unsafe_allow_html=True)

    st.subheader("Participation of the :violet[Countries] in Olympics over the Years")
    nations_over_time = helper.participating_nation_overtime(df)
    fig1 = px.line(nations_over_time, x="Year", y="No.of Countries", markers=True)
    st.plotly_chart(fig1)
    st.markdown(
        ":grey[ Chart illustrates the total number of countries taking part in the Olympics :blue[ Every Year]]"
    )

    st.markdown('<hr style="border: 1px solid #555555;">', unsafe_allow_html=True)

    st.header("No.of :orange[Events] occurring over the Years")
    events_over_time = helper.events_played_overtime(df)
    fig2 = px.line(events_over_time, x="Year", y="No. of Events", markers=True)
    st.plotly_chart(fig2)
    st.markdown(
        ":grey[Chart describes numbers of events played in :blue[Olympics] each Year]"
    )
    st.markdown('<hr style="border: 1px solid #555555;">', unsafe_allow_html=True)
    st.header("Athletes participation over the Years")
    athletes_participating_overtime = helper.athletes_participating_overtime(df)
    fig3 = px.line(
        athletes_participating_overtime, x="Year", y="Athletes", markers=True
    )
    st.plotly_chart(fig3)
    st.markdown(
        ":grey[Chart describes the number of :orange[Athletes] participating each year]"
    )
    st.markdown('<hr style="border: 1px solid #555555;">', unsafe_allow_html=True)
    st.header("Events overall :blue[Representation]")

    fig, ax = plt.subplots(figsize=(16, 16))
    x = df.drop_duplicates(["Year", "Sport", "Event"])
    heatmap_fig = sns.heatmap(
        x.pivot_table(index="Sport", columns="Year", values="Event", aggfunc="count")
        .fillna(0)
        .astype("int"),
        annot=True,
    )
    st.pyplot(fig)
    st.markdown(
        ":grey[Chart describes how the :orange[number of events per sport] has changed over time.]"
    )
    st.markdown(":grey[Some :violet[interesting] data!]")
    st.markdown(
        "- :grey[:green[Cricket] has been played only once in the history of the modern Olympics.]"
    )
    st.markdown(
        "- :grey[Taekwondo was :green[recently] added to the Olympics in 2000.]"
    )

    st.markdown('<hr style="border: 1px solid #555555;">', unsafe_allow_html=True)
    st.header("Most :blue[successful] Athletes")
    sport_list = df["Sport"].unique().tolist()
    sport_list.sort()
    sport_list.insert(0, "Overall")
    selected_sport = st.selectbox("Select a sport :grey[eg. try Athletics]", sport_list)
    y = helper.most_successful(df, selected_sport)
    st.table(y)
    st.markdown('<hr style="border: 1px dashed #555555;">', unsafe_allow_html=True)

if user_menu == "Country-Wise-Analysis":
    st.header(":orange[Countries Performance] in Olympics")
    st.markdown('<hr style="border: 1px solid #555555;">', unsafe_allow_html=True)
    country_list = df["region"].dropna().unique().tolist()
    country_list.sort()
    st.sidebar.markdown('<hr style="border: 2px solid grey;">', unsafe_allow_html=True)
    st.sidebar.title("Country")
    selected_country = st.sidebar.selectbox(
        "Select a :blue[Country] :grey[eg. try USA]", country_list
    )
    plot_df = helper.country_vs_medal_graph(df, selected_country)
    fig4 = px.line(plot_df, x="Year", y="Medals", markers=True)
    st.header(selected_country + " :blue[Medal tally] over the years")
    st.plotly_chart(fig4)
    st.markdown(
        "- :grey[Chart represents the :violet[total] medals won, including gold, silver, and bronze, won in a :violet[specific year].]"
    )

    st.markdown('<hr style="border: 1px solid #555555;">', unsafe_allow_html=True)
    country_plot_df = helper.country_heatmap(df, selected_country)

    if country_plot_df.empty:
        st.error(selected_country + ":grey[ has not :red[won] medals so far !] ")
    else:
        st.header(selected_country + " Excels in following :blue[Sports]")
        fig, ax = plt.subplots(figsize=(14, 14))
        ax = sns.heatmap(country_plot_df, annot=True)
        st.pyplot(fig)
    st.markdown(
        ":grey[Chart illustrates a country's performance in various :violet[sports].]"
    )
    st.markdown('<hr style="border: 1px solid #555555;">', unsafe_allow_html=True)
    st.title("Top :blue[10] athletes of " + selected_country)
    top_country_wise = helper.most_successful_country_wise(df, selected_country)
    if not top_country_wise.empty:
        st.table(top_country_wise)
    else:
        st.write(selected_country + ":red[ has not won medals so far !] ")
    st.markdown('<hr style="border: 1px dashed #555555;">', unsafe_allow_html=True)

if user_menu == "Athlete-Wise-Analysis":
    st.header("Distribution of :green[Age] Among Medalists")
    athletes_df = df.drop_duplicates(subset=["Name", "region"])
    x1 = athletes_df["Age"].dropna()
    x2 = athletes_df[athletes_df["Medal"] == "Gold"]["Age"].dropna()
    x3 = athletes_df[athletes_df["Medal"] == "Silver"]["Age"].dropna()
    x4 = athletes_df[athletes_df["Medal"] == "Bronze"]["Age"].dropna()
    fig_athlete_wise = ff.create_distplot(
        [x1, x2, x3, x4],
        ["Overall Age", "Gold Medalist", "Silver Medalist", "Bronze Medalist"],
        show_hist=False,
        show_rug=False,
    )
    fig_athlete_wise.update_layout(
        autosize=False,
        width=1000,
        height=600,
        xaxis_title="Age",
    )
    st.plotly_chart(fig_athlete_wise)

    st.markdown(
        "- :grey[Chart illustrates the probability of winning a :violet[specific medal at specific ages].]"
    )
    st.markdown('<hr style="border: 1px solid #555555;">', unsafe_allow_html=True)
    st.header("Distribution of :blue[Age] in Sports (:orange[Gold Medalist])")
    sport_list = [
        "Basketball",
        "Judo",
        "Football",
        "Tug-Of-War",
        "Speed Skating",
        "Cross Country Skiing",
        "Athletics",
        "Ice Hockey",
        "Swimming",
        "Badminton",
        "Sailing",
        "Biathlon",
        "Gymnastics",
        "Art Competitions",
        "Alpine Skiing",
        "Handball",
        "Weightlifting",
        "Wrestling",
        "Luge",
        "Water Polo",
        "Hockey",
        "Rowing",
        "Bobsleigh",
        "Fencing",
        "Equestrianism",
        "Shooting",
        "Boxing",
        "Taekwondo",
        "Cycling",
        "Diving",
        "Canoeing",
        "Tennis",
        "Modern Pentathlon",
        "Figure Skating",
        "Golf",
        "Softball",
        "Archery",
        "Volleyball",
        "Synchronized Swimming",
        "Table Tennis",
        "Nordic Combined",
        "Baseball",
        "Rhythmic Gymnastics",
        "Freestyle Skiing",
    ]
    x = []
    name = []

    for item in sport_list:
        temp_sport_df = athletes_df[athletes_df["Sport"] == item]

        age_data = temp_sport_df[temp_sport_df["Medal"] == "Gold"]["Age"].dropna()

        if not age_data.empty and len(age_data) > 1:
            x.append(age_data)
            name.append(item)

    if x:
        fig_sport_wise = ff.create_distplot(x, name, show_hist=False, show_rug=False)
        fig_sport_wise.update_layout(
            autosize=False,
            width=1000,
            height=600,
            xaxis_title="Age",
        )
        st.plotly_chart(fig_sport_wise)
    else:
        st.write("No valid data available for the distribution plot.")

    # st.markdown("---")
    # st.header("Most successful Athletes")
    # sport_list = df["Sport"].unique().tolist()
    # sport_list.sort()
    # sport_list.insert(0, "Overall")
    # selected_sport = st.select_box("Select a sport", sport_list)
    # temp_df =  selected_sport = helper.height_vs_weight(df, selected_sport)
    # fig,ax=plt.subplots()
    # ax=sns.scatterplot(temp_df["Weight"],temp_df["Height"],hue=temp_df["Medal"],style=temp_df["Sex"],s=100)
    # st.pyplot(fig)
    st.markdown(
        "- :grey[Chart roughly indicates which :violet[age is optimal] for winning a gold medal in that sport.]"
    )

    st.markdown('<hr style="border: 1px solid #555555;">', unsafe_allow_html=True)
    st.header("Distribution of :blue[Height] and :blue[Weight] in Sports")
    sport_list = df["Sport"].unique().tolist()
    sport_list.sort()
    sport_list.insert(0, "Overall")
    selected_sport = st.selectbox("Select a sport", sport_list)
    st.markdown('<hr style="border: 1px solid #555555;">', unsafe_allow_html=True)
    temp_df = helper.height_vs_weight(df, selected_sport)
    fig, ax = plt.subplots()
    ax = sns.scatterplot(
        data=temp_df, x="Weight", y="Height", hue="Medal", style="Sex", s=60
    )
    st.pyplot(fig)
    st.markdown(
        "- :grey[ chart roughly suggests the ideal height and weight for ] "
        + selected_sport
        + " :grey[ that can help win  medal in the sport.] "
    )

    st.markdown('<hr style="border: 1px solid #555555;">', unsafe_allow_html=True)

    st.header("Men :green[Vs] Women participation on :blue[Sports]")

    sex_df_data = helper.gender_distribution_plot(df)
    sex_df_fig = px.line(
        sex_df_data,
        x="Year",
        y=["Male", "Female"],
        markers=True,
    )
    sex_df_fig.update_layout(
        autosize=False,
        width=1000,
        height=600,
        xaxis_title="Year",
        yaxis_title="No. of Participants",
    )

    st.plotly_chart(sex_df_fig)
    st.markdown('<hr style="border: 1px dashed #555555;">', unsafe_allow_html=True)
