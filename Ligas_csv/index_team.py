from numpy.lib.twodim_base import mask_indices
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os 
import math
from pandas.core.frame import DataFrame


# Function to substract the dataframes using as parameters a club and a season
def cut_dataframe(df_matches, club, season):

    df_matches = df_matches[(df_matches['HomeTeam'] == club) | (df_matches['AwayTeam'] == club)]
    df_matches = df_matches[df_matches['Season'] == season]

    return df_matches


# Function to change odds to probabilities in a set of matches
def change_odds_to_probabilities(matches):

    matches['ProbH'] = ''
    matches['ProbD'] = ''
    matches['ProbA'] = ''
    matches['OddH_or_D'] = ''
    matches['OddD_or_A'] = ''
    matches['OddH_or_A'] = ''
    matches['H_or_D'] = ''
    matches['D_or_A'] = ''
    matches['H_or_A'] = ''
    matches['margin'] = ''
    matches['reference'] = ''

    matches.margin = ( 1/matches.OddH + 1/matches.OddD + 1/matches.OddA - 1 ) / 3
    matches.ProbH = 1/matches.OddH - matches.margin
    matches.ProbD = 1/matches.OddD - matches.margin
    matches.ProbA = 1/matches.OddA - matches.margin
    matches.reference = round(matches.ProbH,2)
    matches.H_or_D = (matches.ProbH * matches.ProbD)/(matches.ProbH + matches.ProbD)
    matches.D_or_A = (matches.ProbD * matches.ProbA)/(matches.ProbD + matches.ProbA)
    matches.H_or_A = (matches.ProbH * matches.ProbA)/(matches.ProbH + matches.ProbA)
    matches.OddH_or_D = (matches.OddH * matches.OddD)/(matches.OddH + matches.OddD)
    matches.OddD_or_A = (matches.OddD * matches.OddA)/(matches.OddD + matches.OddA)
    matches.OddH_or_A = (matches.OddH * matches.OddA)/(matches.OddH + matches.OddA)

    return matches


# Function that calculates the result of betting in every match
def bets(df_matches, club, bet):

    outcomeH = 0
    outcomeH_or_D = 0
    results = []

    df_matches['betH'] = ''
    df_matches['betD'] = ''
    df_matches['betA'] = ''
    df_matches['betH_or_D'] = ''
    df_matches['betD_or_A'] = ''
    df_matches['betH_or_A'] = ''

    # Here is where the Red Flags must be
    # PRIMERA BANDERA: incluir el Double Chance si la probabilidad de victoria baja de X porcentaje. Puedo hacer una simulación
    # Monte Carlo variando X.
    df_matches.loc[(df_matches['HomeTeam'] == club) & (df_matches['FTR'] == 'H'), 'betH'] = df_matches['OddH'] * bet - bet
    df_matches.loc[(df_matches['HomeTeam'] == club) & (df_matches['FTR'] != 'H'), 'betH'] = - bet
    df_matches.loc[df_matches['HomeTeam'] != club, 'betH'] = 0 
    df_matches.loc[(df_matches['HomeTeam'] == club) & (df_matches['FTR'] != 'A') , 'betH_or_D'] = df_matches['OddH_or_D'] * bet - bet
    df_matches.loc[(df_matches['HomeTeam'] == club) & (df_matches['FTR'] == 'A') , 'betH_or_D'] = - bet
    df_matches.loc[df_matches['HomeTeam'] != club, 'betH_or_D'] = 0
    df_matches.dropna()

    results = df_matches['betH'].tolist()
    results = [item for item in results if not (math.isnan(item))]
    outcomeH = sum(results)

    results = df_matches['betH_or_D'].tolist()
    results = [item for item in results if not (math.isnan(item))]
    outcomeH_or_D = sum(results)

    return (outcomeH, outcomeH_or_D)


# 
def bet_index_team(df_matches, seasons_list, club, bet):

    df_matches_club_per_season = pd.DataFrame()
    df_matches = change_odds_to_probabilities(df_matches)
    outcome = []
    outcomeH = []
    outcomeH_or_D = []

    for season in seasons_list:

        df_matches_club_per_season = cut_dataframe(df_matches, club, season)
        outcome = bets(df_matches_club_per_season, club, bet)
        outcomeH.append(outcome[0])
        outcomeH_or_D.append(outcome[1])

    return (outcomeH, outcomeH_or_D)
        

# 
def bet_index_teams_from_list(df_matches, seasons_list, clubs_list, bet):

    results = []
    resultsH = []
    resultsH_or_D = []

    for club in clubs_list:

        results = bet_index_team(df_matches, seasons_list, club, bet)
        resultsH.append(results[0])
        resultsH_or_D.append(results[1])

    return (resultsH, resultsH_or_D)


if __name__ == "__main__":

    df_matches = pd.read_csv('D:\Dropbox\La Cima del Éxito\Futbol\Ligas_csv\df_Leagues.csv')
    df_matches_club_per_season = pd.DataFrame()
    seasons_list = ['2000-2001','2001-2002','2002-2003','2003-2004','2004-2005','2005-2006','2006-2007','2007-2008','2008-2009','2009-2010','2010-2011','2011-2012','2012-2013','2013-2014','2014-2015','2015-2016','2016-2017','2017-2018','2018-2019','2019-2020','2020-2021']
    seasons_list_2010_2021 = ['2010-2011','2011-2012','2012-2013','2013-2014','2014-2015','2015-2016','2016-2017','2017-2018','2018-2019','2019-2020','2020-2021']
    clubs_list = ['Man City','Man United','Liverpool','Chelsea','Tottenham','Arsenal','Ajax','Feyenoord','PSV Eindhoven','Juventus','Roma','Atalanta','Lazio','Milan','Inter','Celtic','Rangers','Porto','Benfica','Sp Lisbon','Paris SG','Olympiakos','Bayern Munich','Dortmund','Wolfsburg','Galatasaray','Fenerbahce','Club Brugge','Anderlecht','Ath Madrid','Sociedad','Valencia','Betis','Villarreal','Real Madrid','Barcelona','Sevilla']
    clubs_list2 = ['Man City','Man United','Liverpool','Chelsea','Tottenham','Arsenal']

    club = 'PSV Eindhoven'
    season = '2019-2020'
    bet = 100 

    # Tuple [0] -> outcome H in 1X2
    # Tuple [1] -> outcome H or D in 1X2
    result = bet_index_teams_from_list(df_matches,seasons_list,clubs_list,bet)

    df_results_H = pd.DataFrame(result[0], index=clubs_list, columns=seasons_list)
    df_results_H_or_D = pd.DataFrame(result[1], index=clubs_list, columns=seasons_list)
    
    print(df_results_H)
    print(df_results_H_or_D)

    #df_results = df_results.T

    #print(df_results)

    df_results_H_or_D.to_csv('D:\Dropbox\La Cima del Éxito\Futbol\Ligas_csv\\teams_bets.csv',encoding='utf-8',index=True)

    #result = bet_index_team(df_matches, seasons_list, club, bet)
    #print(result)
    #print(sum(bet_index_team(df_matches, seasons_list, club, bet)))
    
    #df_matches = change_odds_to_probabilities(df_matches)
    #df_matches_club_per_season = cut_dataframe(df_matches, club, seasons_list[13])
    #print(bets(df_matches_club_per_season, club, bet))


    #print(df_matches_club_per_season)
    #df_matches_club_per_season.to_csv('D:\Dropbox\La Cima del Éxito\Futbol\Ligas_csv\df_bets_test.csv',encoding='utf-8',index=False)