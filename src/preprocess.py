import pandas as pd

def load_data(path):
    df=pd.read_csv(path)
    df['Gender']=df['Gender'].map({'male':0,'female':1,'Male':0,'Female':1})
    df=df.fillna(df.mean(numeric_only=True))
    return df
