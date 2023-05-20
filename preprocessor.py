import pandas as pd

df = pd.read_csv('athlete_events.csv')
region_df = pd.read_csv('noc_regions.csv')

def preprocess():
    global df,region_df

    df_summer = df[df['Season']=='Summer']

    df_summer = df_summer.merge(region_df,on='NOC',how='left')

    df_summer.drop_duplicates(inplace=True)

    df_summer = pd.concat([df_summer,pd.get_dummies(df_summer['Medal'])],axis=1)

    return df_summer