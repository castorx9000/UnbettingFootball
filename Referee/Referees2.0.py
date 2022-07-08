from os import remove
import numpy as np
import pandas as pd
import math


def remove_matches_without_referees(df_matches):

    # Identifying incomplete data filling cell as 'unknown'
    df_matches['Referee'].fillna('unknown', inplace=True)
    df_matches['OddH'].fillna('unknown', inplace=True)
    df_matches['OddD'].fillna('unknown', inplace=True)
    df_matches['OddA'].fillna('unknown', inplace=True)
    df_matches['HF'].fillna('unknown', inplace=True)
    df_matches['AF'].fillna('unknown', inplace=True)
    df_matches['HY'].fillna('unknown', inplace=True)
    df_matches['AY'].fillna('unknown', inplace=True)
    df_matches['HR'].fillna('unknown', inplace=True)
    df_matches['AR'].fillna('unknown', inplace=True)

    # Removing matches with incomplete data
    df_matches = df_matches[df_matches['Referee'] != 'unknown'] 
    df_matches = df_matches[df_matches['OddH'] != 'unknown']
    df_matches = df_matches[df_matches['OddD'] != 'unknown']
    df_matches = df_matches[df_matches['OddA'] != 'unknown']
    df_matches = df_matches[df_matches['HF'] != 'unknown'] 
    df_matches = df_matches[df_matches['AF'] != 'unknown']
    df_matches = df_matches[df_matches['HY'] != 'unknown']
    df_matches = df_matches[df_matches['AY'] != 'unknown']
    df_matches = df_matches[df_matches['HR'] != 'unknown']
    df_matches = df_matches[df_matches['AR'] != 'unknown']

    # Removing registers with Odds = 0
    df_matches = df_matches[df_matches['OddH'] != 0]
    df_matches = df_matches[df_matches['OddD'] != 0]
    df_matches = df_matches[df_matches['OddA'] != 0]
    
    return df_matches


def get_referees_list(df_matches):

    referees = []
    referees = df_matches['Referee'].tolist()
    referees = list(set(referees))

    return referees


def get_matches_of_referee(df_matches, referee):

    df_matches = df_matches[df_matches['Referee'] == referee]

    return df_matches


def get_referees_with_at_least_30_matches(df_matches, referees):

    df = pd.DataFrame()
    referees_with_at_least_30_matches = []

    for referee in referees:

        df = get_matches_of_referee(df_matches, referee)
        if len(df) >= 30:
            referees_with_at_least_30_matches.append(referee)

    return referees_with_at_least_30_matches


# Function to change odds to probabilities in a set of matches
def change_odds_to_probabilities(df_matches):

    df_matches['ProbH'] = ''
    df_matches['ProbD'] = ''
    df_matches['ProbA'] = ''
    df_matches['margin'] = ''
    df_matches['reference'] = ''

    df_matches.margin = ( 1/df_matches.OddH + 1/df_matches.OddD + 1/df_matches.OddA - 1 ) / 3
    df_matches.ProbH = 1/df_matches.OddH - df_matches.margin
    df_matches.ProbD = 1/df_matches.OddD - df_matches.margin
    df_matches.ProbA = 1/df_matches.OddA - df_matches.margin

    df_matches.reference = round(df_matches.ProbH.astype(float),2)

    return df_matches


# Function to find the expected values in Metron given a reference used as index
def find_index(reference, escenario_list):
    index = 0
    reference = reference * 100
    result = 0
    
    if reference == 50:
        index = 21
    if reference > 50:
        index = find_index_before_half(reference)
    if reference < 50:
        index = find_index_after_half(reference)
    
    if reference < 8:
        result = escenario_list[-1]
    else:
        result = escenario_list[index]

    return result


# Auxiliar Function to find the expected values    
def find_index_before_half(reference):
    index = 21
    escenario = 52
    flag = True

    while flag:
        if reference < escenario:
            flag = False
        else:
            escenario += 2
            index -= 1

    return index


# Auxiliar Function to find the expected values
def find_index_after_half(reference):
    index = 22
    escenario = 48
    flag = True

    while flag:
        if reference >= escenario:
            flag = False
        else:
            escenario -= 2
            index += 1

    return index


# Function to calculate a club's profile in a set of matches
def referee_profile(matches, metron, referee):
    
    escenario_list = [i for i  in metron['Escenario']]
    auxiliar = pd.DataFrame()
    results = []

    games = 0
    
    h_obWins, h_obDraws, h_obLosses = 0, 0, 0
    a_obWins, a_obDraws, a_obLosses = 0, 0, 0
    h_obSG, a_obSG = 0, 0
    obSG = 0

    h_obFouls, a_obFouls = 0, 0
    h_obYC, h_obRC, h_obYC, h_obRC = 0, 0, 0, 0
    a_obYC, a_obRC, a_obYC, a_obRC = 0, 0, 0, 0
    obFouls, obYC, obRC = 0, 0, 0

    h_exWins, h_exDraws, h_exLosses = 0, 0, 0
    a_exWins, a_exDraws, a_exLosses = 0, 0, 0
    h_exSG, a_exSG = 0, 0
    exSG = 0

    h_exFouls, a_exFouls = 0, 0
    h_exYC, h_exRC, h_exYC, h_exRC = 0, 0, 0, 0
    a_exYC, a_exRC, a_exYC, a_exRC = 0, 0, 0, 0
    exFouls, exYC, exRC = 0, 0, 0

    for index, row in matches.iterrows():
    
        if math.isnan(row['ProbH']) or math.isnan(row['ProbD']) or math.isnan(row['ProbA']):
                continue
    
        if row['Referee'] == referee:
            
            games += 1

            # Collecting expected values of Home team
            h_exWins += row['ProbH']
            h_exDraws += row['ProbD']
            h_exLosses += row['ProbA']
            h_obSG += row['FTHG']
            h_obFouls += row['HF']
            h_obYC += row['HY']
            h_obRC += row['HR']

            # Collecting Expected values of Home team from Metron
            reference = row['reference']
            reference = find_index(reference, escenario_list)

            auxiliar = metron.loc[metron['Escenario'] == reference]
            h_exSG += auxiliar['FTHG'].values[0]
            h_exFouls += auxiliar['HF'].values[0]
            h_exYC += auxiliar['HY'].values[0]
            h_exRC += auxiliar['HR'].values[0]
            
            # Collecting data of redord of both teams
            if row['FTR'] == 'H':
                h_obWins += 1
                a_obLosses += 1
            if row['FTR'] == 'D':
                h_obDraws += 1
                a_obDraws += 1
            if row['FTR'] == 'A':
                h_obLosses += 1
                a_obWins += 1
        
            # Collecting Expected Values of Away team
            a_exWins += row['ProbH']
            a_exDraws += row['ProbD']
            a_exLosses += row['ProbA']
            a_obSG += row['FTAG']
            a_obFouls += row['AF']
            a_obYC += row['AY']
            a_obRC += row['AR']
            
            # Collecting Expected Values of Away team from Metron
            reference = row['reference']
            reference = find_index(reference, escenario_list)

            auxiliar = metron.loc[metron['Escenario'] == reference]
            a_exSG += auxiliar['FTAG'].values[0]
            a_exFouls += auxiliar['AF'].values[0]
            a_exYC += auxiliar['AY'].values[0]
            a_exRC += auxiliar['AR'].values[0]

    obSG = h_obSG + a_obSG
    exSG = h_exSG + a_exSG
    obFouls = h_obFouls + a_obFouls
    exFouls = h_exFouls + a_exFouls
    obYC = h_obYC + a_obYC
    exYC = h_exYC + a_exYC
    obRC = h_obRC + a_obRC
    exRC = h_exRC + a_exRC

    results = [
        referee, games, 
        h_obWins, h_obDraws, h_obLosses, a_obWins, a_obDraws, a_obLosses, 
        h_obSG, a_obSG, obSG,
        h_exWins, h_exDraws, h_exLosses, a_exWins, a_exDraws, a_exLosses, 
        h_exSG, a_exSG, exSG,
        obFouls, exFouls, h_obFouls, h_exFouls, a_obFouls, a_exFouls, 
        obYC, exYC, obRC, exRC, h_obYC, h_exYC, a_obYC, a_exYC, h_obRC, h_exRC, a_obRC, a_exRC
        ]
        
    return results


# Root function
def referees_performance(df_matches, metron):

    referees_list = []
    referees_results = []

    df_matches = remove_matches_without_referees(df_matches)
    referees_list = get_referees_list(df_matches)
    referees_list = get_referees_with_at_least_30_matches(df_matches, referees_list)
    df_matches = change_odds_to_probabilities(df_matches)

    for referee in referees_list:

        referees_results.append(referee_profile(df_matches, metron, referee))

    df_referees = pd.DataFrame(referees_results, columns=['Referee','Matches','h_obWins','h_obDraws','h_obLosses','a_obWins','a_obDraws','a_obLosses','h_obSG','a_obSG','obSG','h_exWins','h_exDraws','h_exLosses','a_exWins','a_exDraws','a_exLosses','h_exSG','a_exSG','exSG','obFouls', 'exFouls', 'h_obFouls', 'h_exFouls', 'a_obFouls', 'a_exFouls', 'obYC', 'exYC', 'obRC', 'exRC','h_obYC', 'h_exYC', 'a_obYC', 'a_exYC', 'h_obRC', 'h_exRC', 'a_obRC', 'a_exRC'])
    df_referees = df_referees[['Referee','Matches','h_obWins','h_exWins','h_obDraws','h_exDraws','h_obLosses','h_exLosses','a_obWins','a_exWins','a_obDraws','a_exDraws','a_obLosses','a_exLosses','h_obSG','h_exSG','a_obSG','a_exSG','obSG','exSG','obFouls', 'exFouls', 'h_obFouls', 'h_exFouls', 'a_obFouls', 'a_exFouls', 'obYC', 'exYC', 'obRC', 'exRC','h_obYC', 'h_exYC', 'a_obYC', 'a_exYC', 'h_obRC', 'h_exRC', 'a_obRC', 'a_exRC']]

    return df_referees


if __name__ == "__main__":

    # Loading the long term reference Metron
    metron = pd.read_excel('reference_system_means.xlsx')
    metron = metron[['Escenario','FTHG','FTAG','HTHG','HTAG','HS','AS','HST','AST','HF','AF','HY','AY','HR','AR']]

    # Loading the DF of european league matches from 2000-2001 to 2020-2021
    df_matches = pd.read_csv('D:\Dropbox\La Cima del Éxito\Futbol\Ligas_csv\df_Leagues.csv')
    
    referees_profiles = referees_performance(df_matches, metron)
    print(referees_profiles)
    referees_profiles.to_csv('D:\Dropbox\La Cima del Éxito\Futbol\Referee\Referees_profiles.csv',encoding='utf-8',index=True)
    
    
    #df_test = pd.DataFrame()
    #list_test = []
    #referee_test = 'Dallas, H.'
    
    #referee_list_test = ['P Quinn', 'C Thompson', 'Volker Wezel ', 'Styles, R', 'Albrecht, H', 'Kilburn, M', 'M A Harris', 'S Creighton', 'Wezel, V', 'Pugh, D.', 'Eddie Ilderton', 'Trevor Jones', 'Jürgen Jansen']
    
    #df_test = remove_matches_without_referees(df_matches)
    #referees_list = get_referees_list(df_test)
    #list_test = get_referees_with_at_least_30_matches(df_test, referees_list)

    #list_test = get_referees_list(df_test)
    #list_test = get_referees_with_at_least_30_matches(df_test,referee_list_test)
    #df_test = get_matches_of_referee(df_test, list_test[1])
    
    #df_test.to_csv('D:\Dropbox\La Cima del Éxito\Futbol\Referee\Referees.csv',encoding='utf-8',index=True)

    #print(df_test)
    #print(list_test)
    #print(len(list_test))
    #print(len(list_test))