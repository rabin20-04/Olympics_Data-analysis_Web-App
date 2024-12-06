import pandas as pd
def preprocess(df,region_df):
    # global df,region_df
    #filter summer season only
    df=df[df["Season"]=="Summer"]
    df=df.merge(region_df,how="left",on="NOC")
    df.drop_duplicates(inplace=True)
    medal_dummies=(pd.get_dummies(df["Medal"])).astype(int)
    df=pd.concat([df,medal_dummies],axis=1)

    return df
