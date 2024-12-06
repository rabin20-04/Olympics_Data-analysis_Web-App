import numpy as np
def medal_tally(df):
    medal_tally=df.drop_duplicates(subset=['Team','NOC','Year','Sport','Event','Medal'])
    medal_tally=medal_tally.groupby("region").sum()[["Gold","Bronze","Silver"]].sort_values("Gold",ascending=False)
    medal_tally=medal_tally.reset_index().reset_index() # because noc appears in new row alone and other medals above
    medal_tally["Total"]=medal_tally["Gold"]+medal_tally["Silver"]+medal_tally["Bronze"]
    medal_tally["Gold"]=medal_tally["Gold"].astype("int")
    medal_tally["Silver"]=medal_tally["Silver"].astype("int")
    medal_tally["Bronze"]=medal_tally["Bronze"].astype("int")
    return medal_tally

def country_year_list(df):
    year_list=df["Year"].unique().tolist()
    year_list.sort()
    year_list.insert(0,"Overall")

    countries_list=np.unique(df["region"].dropna().values).tolist()
    countries_list.sort()
    countries_list.insert(0,"Overall")
    return year_list,countries_list