import pandas as pd
df=pd.read_csv('https://www.football-data.co.uk/mmz4281/2324/SC0.csv')
#df=pd.read_csv('first.csv')
new=len(df)
print(f'Total entries in this file are: {new}')

df=df.rename(columns={'FTR': 'LAk','FTHG':'MAHAR'})
print(df[:174])
