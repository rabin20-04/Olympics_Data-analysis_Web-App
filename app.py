import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.figure_factory as ff

st.set_page_config(layout="wide")
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
    st.markdown(
        " #### :violet[Table presents various Medal achievements of selected Nation]  "
    )
    st.markdown(
        "-   :blue[ Total :orange[Gold Medals] , Siver Medals and Bronze Medals won in the Olympics so far!]"
    )
    st.sidebar.header(":violet[Medal Tally]")
    years, country = helper.country_year_list(df)
    selected_year = st.sidebar.selectbox("Select Year", years)
    selected_country = st.sidebar.selectbox("Select Country", country)

    medal_tally = helper.fetch_medal_tally(df, selected_country, selected_year)
    if selected_year != "Overall" and selected_country != "Overall":
        st.header(
            "Medal Tally of " + selected_country + " in the Year " + str(selected_year)
        )
    elif selected_year != "Overall" and selected_country == "Overall":
        st.header("Overall Medal Tally in the year " + str(selected_year))
    elif selected_year == "Overall" and selected_country == "Overall":
        st.header("Overall Medal Tally")
        st.markdown(
            "-  :grey[eg. USA has won a total of :orange[1,035 gold medals], 708 silver medals, and 802 bronze medals, with a total of 2,545 medals. and Russia has won a total of :orange[592 gold medals], 487 silver medals, and 498 bronze medals, with a total of 1,577 medals.]"
        )

    elif selected_year == "Overall" and selected_country != "Overall":
        st.header("Overall Performance of " + selected_country)

    st.table(medal_tally)
    st.markdown('<hr style="border: 1px dashed #555555;">', unsafe_allow_html=True)
if user_menu == "Overall Analysis":
    st.markdown(
        "### :violet[This page provides an insightful analysis of Olympic countries, their participation, the popularity of sports and events, and the success of athletes.]"
    )
    st.sidebar.markdown(
        '<hr style="border: 2px solid #555555;">', unsafe_allow_html=True
    )

    st.sidebar.markdown(
        "- **:orange[An analysis of Olympic countries, participation, sports popularity, events, and athlete success.]**"
    )

    st.markdown('<hr style="border: 1px solid #555555;">', unsafe_allow_html=True)

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
    st.markdown(
        "- :grey[**Editions** represents total no. of times Olympics have successfully happened till 2018.]"
    )
    st.markdown(
        "- :grey[**Host Cities** refers to the total number of cities where the Olympics have been hosted.]"
    )
    st.markdown(
        "- :grey[**Total Sports** indicates the total number of sports included in the Olympics.]"
    )
    st.markdown(
        "- :grey[**Events** represents the number of events held during the Olympics.]"
    )
    st.markdown(
        "- :grey[**Nations** refers to the number of nations that have participated in the Olympics.]"
    )
    st.markdown(
        "- :grey[**Athletes** indicates the total number of athletes who have competed in the Olympics.]"
    )
    st.markdown('<hr style="border: 1px solid #555555;">', unsafe_allow_html=True)

    st.subheader("Participation of the :violet[Countries] in Olympics over the Years")
    nations_over_time = helper.participating_nation_overtime(df)
    fig1 = px.line(nations_over_time, x="Year", y="No.of Countries", markers=True)
    st.plotly_chart(fig1)
    st.markdown(
        "- :grey[ Chart illustrates the total number of countries taking part in the Olympics :blue[ Every Year]]"
    )
    st.markdown(":violet[**Highlights:**]")
    st.markdown("- :grey[**1916 Olympics** were canceled due to World War I.]")
    st.markdown(
        "- :grey[**1940 and 1944 Olympics** were canceled due to World War II.]"
    )
    st.markdown(
        "- :grey[**1980 Moscow Olympics** saw a U.S.-led boycott during the Cold War.]"
    )
    st.markdown(
        "- :grey[**1984 Los Angeles Olympics** faced a counter-boycott from the Soviet bloc.]"
    )
    st.markdown("- :grey[**1948 London Olympics** were the first after World War II.]")
    st.markdown(
        "- :grey[**Post-2000**, Olympic participation has steadily increased globally.]"
    )

    st.markdown('<hr style="border: 1px solid #555555;">', unsafe_allow_html=True)

    st.header("No.of :orange[Events] occurring over the Years")
    events_over_time = helper.events_played_overtime(df)
    fig2 = px.line(events_over_time, x="Year", y="No. of Events", markers=True)
    st.plotly_chart(fig2)
    st.markdown(
        ":grey[Chart describes numbers of events played in :blue[Olympics] each Year]"
    )
    st.markdown(":violet[**Highlights:**]")
    st.markdown(
        "- :grey[**1904 to 1906**: The number of events decreased due to limited international participation and several events being restricted to American athletes in 1904.]"
    )

    st.markdown(
        "- :grey[**1908**: The number of events increased as sports like figure skating and cycling were included, reflecting growing international involvement.]"
    )
    st.markdown(
        "- :grey[**1912**: The Stockholm Olympics saw the introduction of modern pentathlon and tennis as part of the growing diversity of Olympic sports.]"
    )
    st.markdown(
        "- :grey[**1920 to 1924**: The number of events fell due to political and financial challenges, and some sports like polo and rugby were removed.]"
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
    st.markdown(":violet[**Highlights:**]")
    st.markdown(
        "- :grey[**1900-1904**: Athlete participation was low, with many events dominated by local American athletes and limited international involvement.]"
    )
    st.markdown(
        "- :grey[**1928-1932**: Athlete participation decreased due to the global economic downturn and the effects of the Great Depression, limiting international involvement.]"
    )
    st.markdown(
        "- :grey[**1932-1936**: Athlete participation grew as the global situation improved and 1936 Berlin Olympics saw **:blue[the highest number of athletes up to that point.]**]"
    )
    st.markdown(
        "- :grey[**1952-1956**: Athlete participation slightly decreased  due to factors like political tensions during the Cold War, logistical challenges for athletes affecting participation.]"
    )
    st.markdown(
        "- :grey[**1972-1980**: Athlete participation decreased due to the 1980 boycott, limiting the number of nations and athletes involved.]"
    )
    st.markdown(
        "- :grey[**Post-1980**: Athlete participation continued to rise, with more nations joining and professional athletes competing.]"
    )

    st.markdown('<hr style="border: 1px solid #555555;">', unsafe_allow_html=True)
    st.header("Events overall :blue[Representation]")

    st.markdown(
        ":grey[Chart describes how the :orange[number of events per sport] has changed over time.]"
    )
    fig, ax = plt.subplots(figsize=(16, 16))
    x = df.drop_duplicates(["Year", "Sport", "Event"])
    heatmap_fig = sns.heatmap(
        x.pivot_table(index="Sport", columns="Year", values="Event", aggfunc="count")
        .fillna(0)
        .astype("int"),
        annot=True,
    )
    st.pyplot(fig)
    st.markdown(":grey[Some :violet[interesting] data!]")
    st.markdown(
        "- :grey[:green[Cricket] has been played only once in the history of the modern Olympics.]"
    )
    st.markdown(
        "- :grey[Taekwondo was :green[recently] added to the Olympics in 2000.]"
    )
    st.markdown(
        "- :grey[**:orange[Athletics] in 1896**: Only 12 events were held, with a continuous rise in the number of events, reaching 33 in **1948** and eventually 47 events by **2016**.]"
    )
    st.markdown(
        "- :grey[**:orange[Shooting] in 1896**: Had 5 events, followed by a slight reduction to 0 in **1904**. The number of events increased again in **1920**, then decreased to zero in **1928**. Since then, the number of shooting events has been steadily increasing, reaching 15 events by **2016**.]"
    )

    st.markdown('<hr style="border: 1px solid #555555;">', unsafe_allow_html=True)
    st.header("Top :blue[Successful] Athletes in Their Field")

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

    default_country = "USA"
    if default_country in country_list:
        default_index = country_list.index(default_country)
    else:
        default_index = 3
    st.sidebar.markdown('<hr style="border: 2px solid grey;">', unsafe_allow_html=True)
    st.sidebar.title("Country")
    selected_country = st.sidebar.selectbox(
        "Select a :blue[Country] ", country_list, index=default_index
    )

    plot_df = helper.country_vs_medal_graph(df, selected_country)

    if plot_df.empty:
        st.error(selected_country + ":grey[ has not :red[won] medals so far !] ")
    else:
        fig4 = px.line(plot_df, x="Year", y="Medals", markers=True)
        st.header(f"{selected_country} :blue[Medal Tally Over Time]")
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
