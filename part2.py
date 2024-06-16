import pandas as pd

df = pd.read_csv('dz.csv')
gr = df.groupby('City')['Salary'].mean()
print(gr)
