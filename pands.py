#importing pandas library to read the csv or online 
import pandas as pd
#reading the online data and then saving it into a reading variable
reading=pd.read_html('https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes')

#if u want to read from your own file 
df=pd.read_csv('test.txt',sep=' ',header=None,names=['first name','last name'])

print(df)

#finding the length of tables in html docs at specific url
checking=len(reading)
print(checking)

red=reading[1]

print(red)