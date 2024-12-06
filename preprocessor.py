import pandas as pd
df=pd.read_csv('athlete_events.csv')
athletes_df=pd.read_csv('athlete_events.csv')
region_df=pd.read_csv('noc_regions.csv')
def preprocess():
    global df,region_df
    #filter summer season only
    df=df[df["Season"]=="Summer"]
    df=df.merge(region_df,how="left",on="NOC")
    df.drop_duplicates(inplace=True)
    medal_dummies=(pd.get_dummies(df["Medal"])).astype(int)
    df=pd.concat([df,medal_dummies],axis=1)

    return df
