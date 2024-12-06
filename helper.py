def medal_tally(df):
    medal_tally=df.drop_duplicates(subset=['Team','NOC','Year','Sport','Event','Medal'])
    medal_tally=medal_tally.groupby("region").sum()[["Gold","Bronze","Silver"]].sort_values("Gold",ascending=False)
    medal_tally=medal_tally.reset_index().reset_index() # because noc appears in new row alone and other medals above
    medal_tally["Total"]=medal_tally["Gold"]+medal_tally["Silver"]+medal_tally["Bronze"]
    medal_tally["Gold"]=medal_tally["Gold"].astype("int")
    medal_tally["Silver"]=medal_tally["Silver"].astype("int")
    medal_tally["Bronze"]=medal_tally["Bronze"].astype("int")
    return medal_tally