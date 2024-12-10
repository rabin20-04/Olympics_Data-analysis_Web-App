import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def fetch_medal_tally(df, country, year):
    medal_df = df.drop_duplicates(subset=["Team", "NOC", "Year", "Sport", "Event", "Medal"])

    flag = 0  # for overall year of specific country
    if country == "Overall" and year == "Overall":
        temp_df = medal_df
    if country != "Overall" and year == "Overall":
        flag = 1
        temp_df = medal_df[medal_df["region"] == country]
    if country == "Overall" and year != "Overall":
        temp_df = medal_df[medal_df["Year"] == int(year)]
    if country != "Overall" and year != "Overall":
        temp_df = medal_df[(medal_df["Year"] == int(year)) & (medal_df["region"] == country)]

    if flag == 1:
        x = temp_df.groupby("Year").sum()[["Gold", "Bronze", "Silver"]].sort_values("Year").reset_index()

    else:
        x = temp_df.groupby("region").sum()[["Gold", "Bronze", "Silver"]].sort_values("Gold",
                                                                                      ascending=False).reset_index()

    x["Total"] = (x["Gold"] + x["Silver"] + x["Bronze"])
    x["Total"] = x["Total"].astype("str")

    x["Gold"] = x["Gold"].astype("str")
    x["Silver"] = x["Silver"].astype("str")
    x["Bronze"] = x["Bronze"].astype("str")
    if "Year" in x.columns:
        x["Year"] = x["Year"].astype("str")

    return x


def medal_tally(df):
    medal_tally = df.drop_duplicates(subset=['Team', 'NOC', 'Year', 'Sport', 'Event', 'Medal'])
    medal_tally = medal_tally.groupby("region").sum()[["Gold", "Bronze", "Silver"]].sort_values("Gold", ascending=False)
    medal_tally = medal_tally.reset_index()  # because noc appears in new row alone and other medals above
    medal_tally["Total"] = medal_tally["Gold"] + medal_tally["Silver"] + medal_tally["Bronze"]
    medal_tally["Gold"] = medal_tally["Gold"].astype("int")
    medal_tally["Silver"] = medal_tally["Silver"].astype("int")
    medal_tally["Bronze"] = medal_tally["Bronze"].astype("int")

    return medal_tally


def country_year_list(df):
    year_list = df["Year"].unique().tolist()
    year_list.sort()

    year_list.insert(0, "Overall")
    countries_list = np.unique(df["region"].dropna().values).tolist()
    countries_list.sort()
    countries_list.insert(0, "Overall")
    return year_list, countries_list


def participating_nation_overtime(df):
    unique_df1 = df.drop_duplicates(["Year", "region"])

    nation_over_time = unique_df1["Year"].value_counts().reset_index()

    nation_over_time.columns = ["Year", "No.of Countries"]

    # Sort the DataFrame by 'Year' (the actual column, not 'index')
    nation_over_time = nation_over_time.sort_values(by="Year")

    return nation_over_time


def events_played_overtime(df):
    unique_df2 = df.drop_duplicates(["Year", "Event"])

    events_over_time = unique_df2["Year"].value_counts().reset_index()

    events_over_time.columns = ["Year", "No. of Events"]

    # Sort the DataFrame by 'Year' (the actual column, not 'index')
    events_over_time = events_over_time.sort_values(by="Year")

    return events_over_time
def athletes_participating_overtime(df):
    unique_df3 = df.drop_duplicates(["Year", "Name"])

    athletes_participating_over_time = unique_df3["Year"].value_counts().reset_index()

    athletes_participating_over_time.columns = ["Year", "Athletes"]

    # Sort the DataFrame by 'Year' (the actual column, not 'index')
    athletes_participating_over_time = athletes_participating_over_time.sort_values(by="Year")

    return athletes_participating_over_time

def events_overall_representation(df):
    unique_df4 = df.drop_duplicates(["Year","Sport","Event"])

    events_overall_representation = (unique_df4.pivot_table(index="Sport",columns="Year",values="Event",aggfunc="count").fillna(0).astype("int"))



    return events_overall_representation