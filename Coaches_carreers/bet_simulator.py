import numpy as np
import pandas as pd
import datetime as datetime


def cut_league_matches(league,start,end,league_matches):

    df_matches = pd.DataFrame()
    df_matches = league_matches[league_matches['Div'] == league]
    #df_matches = league_matches.loc[league_matches['Div'] == league]
    #df_matches['Date'] = pd.to_datetime(df_matches['Date'])
    #df_matches.sort_values(by=['Date'])


    return df_matches

if __name__ == '__main__':

    league = 'E0'
    start = ''
    end = ''
    league_matches = pd.read_excel('df_Leagues.xlsx')

    league_matches = cut_league_matches(league,start,end,league_matches)
    league_matches.to_csv('matches.csv')