import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

excel_file_1 = 'muestra.xlsx'

df_muestra = pd.read_excel(excel_file_1, sheet_name='Muestra2015-2019')

#print(df_muestra.head(10)) #prints first ten rows
#print(df_muestra.tail(10)) #prints last ten rows
#print(df_muestra.columns) #prints columns
#print(type(df_muestra.columns[0])) #prints type of df columns --> str
#print(df_muestra['HomeTeam']) #prints column 'HomeTeam' content
#print(df_muestra['HomeTeam'][0:5]) #prints first 5 rows of column 'HomeTeam' content
#print(df_muestra[['HomeTeam','AwayTeam']][0:5]) #prints first 5 rows of columns listed content

df = df_muestra[['Season','Div','Date','HomeTeam','AwayTeam','FTHG','FTAG','FTR','B365H','B365D','B365A']][0:10] #OJO si una columna no existe, marca error
print(df) 
#print(df_muestra.iloc[0:3]) #prints rows 0 until row 3
#print(df_muestra.iloc[2,3]) #prints row 2 column 3 --> Alcorcon

#To Iterate through rows:
#for index, row in df.iterrows():
    #print(f'Timestamp del partido: {row[2]}, date: {row[2].year}, day of year: {row[2].day}')
    #print(f'{row[9]}, {type(row[9])}')
    #print(index, row['B365H'], row['B365D'],row['B365A'])

print(df.loc[df['HomeTeam'] == 'Real Madrid'])
print(df.loc[df['Div'] == 'SP1'])
print(df.loc[df['FTR'] == 'D'])