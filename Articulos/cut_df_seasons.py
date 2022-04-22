#import numpy as np
import pandas as pd


if __name__ == '__main__':

    league = 'SP2'
    league_name = 'LaLiga_2'
    period = '2000-2021'
    league_matches = pd.read_csv('D:\Dropbox\La Cima del Éxito\Futbol\\articulos\df_leagues.csv')
    
    league_matches = league_matches[['Season','Div','Date','HomeTeam','AwayTeam','FTHG','FTAG','FTR','HTHG','HTAG','HTR','HS','AS','HST','AST','HF','AF','HY','AY','HR','AR','OddH','OddD','OddA']]
    league_matches = league_matches[league_matches['Div'] == league]
    league_matches.dropna(how='any', inplace=True)
    
    league_matches.to_excel(f'D:\Dropbox\La Cima del Éxito\Futbol\\articulos\matches_{period}_{league_name}.xlsx',encoding='utf-8',index=True)