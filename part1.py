import pandas as pd

df = pd.read_csv('netflix_full.csv')

print(df.head())
print(df.info())
print(df.describe())
