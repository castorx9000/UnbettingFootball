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

    # Removing matches with incomplete data
    df_matches = df_matches[df_matches['Referee'] != 'unknown'] 
    df_matches = df_matches[df_matches['OddH'] != 'unknown']
    df_matches = df_matches[df_matches['OddD'] != 'unknown']
    df_matches = df_matches[df_matches['OddA'] != 'unknown']

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
    
    performance = 0
    h_obPts, a_obPts, obPts = 0, 0, 0
    h_exPts, a_exPts, exPts = 0, 0, 0
    obPPM, exPPM = 0, 0
    h_obPPM, h_exPPM = 0, 0
    a_obPPM, a_exPPM = 0, 0
    h_obWins, a_obWins, obWins = 0, 0, 0
    h_obDraws, a_obDraws, obDraws = 0, 0, 0
    h_obLosses, a_obLosses, obLosses = 0, 0, 0
    h_exWins, a_exWins, exWins = 0, 0, 0
    h_exDraws, a_exDraws, exDraws = 0, 0, 0
    h_exLosses, a_exLosses, exLosses = 0, 0, 0
    winsP100, drawsP100, lossesP100 = 0, 0, 0
    h_winsP100, h_drawsP100, h_lossesP100 = 0, 0, 0
    a_winsP100, a_drawsP100, a_lossesP100 = 0, 0, 0
    obSGPM, obCGPM, h_obSGPM, h_obCGPM, a_obSGPM, a_obCGPM = 0, 0, 0, 0, 0, 0
    exSGPM, exCGPM, h_exSGPM, h_exCGPM, a_exSGPM, a_exCGPM = 0, 0, 0, 0, 0, 0
    h_obSG, a_obSG, obSG = 0, 0, 0
    h_obCG, a_obCG, obCG = 0, 0, 0
    h_exSG, a_exSG, exSG = 0, 0, 0
    h_exCG, a_exCG, exCG = 0, 0, 0
    SGP100, CGP100, h_SGP100, h_CGP100, a_SGP100, a_CGP100 = 0, 0, 0, 0, 0, 0
    h_played, a_played, played = 0, 0, 0

    escenario_list = [i for i  in metron['Escenario']]
    auxiliar = pd.DataFrame()

    results = []

    for index, row in matches.iterrows():
    
        if math.isnan(row['ProbH']) or math.isnan(row['ProbD']) or math.isnan(row['ProbA']):
                continue
    
        if row['Referee'] == referee:
            
            # Collecting data of Home team
            h_exPts += 3 * row['ProbH'] + 1 * row['ProbD']
            h_exWins += row['ProbH']
            h_exDraws += row['ProbD']
            h_exLosses += row['ProbA']
            h_obSG += row['FTHG']
            h_obCG += row['FTAG']
            h_played += 1

            # Collecting Expected values of Home team from Metron
            reference = row['reference']
            reference = find_index(reference, escenario_list)

            auxiliar = metron.loc[metron['Escenario'] == reference]
            h_exSG += auxiliar['FTHG'].values[0]
            h_exCG += auxiliar['FTAG'].values[0]
            
            # Collecting data of points collected by both teams
            if row['FTR'] == 'H':
                h_obPts += 3
                h_obWins += 1
                a_obLosses += 1
            if row['FTR'] == 'D':
                h_obPts += 1
                h_obDraws += 1
                a_obPts += 1
                a_obDraws += 1
            if row['FTR'] == 'A':
                h_obLosses += 1
                a_obPts += 3
                a_obWins += 1
        
            # Collecting data of Away team
            a_exPts += 3 * row['ProbA'] + 1 * row['ProbD']
            a_exWins += row['ProbA']
            a_exDraws += row['ProbD']
            a_exLosses += row['ProbH']
            a_obSG += row['FTAG']
            a_obCG += row['FTHG']
            a_played += 1

            # Collecting Expected values of Away team from Metron
            reference = row['reference']
            reference = find_index(reference, escenario_list)

            auxiliar = metron.loc[metron['Escenario'] == reference]
            a_exSG += auxiliar['FTAG'].values[0]
            a_exCG += auxiliar['FTHG'].values[0]
            

    obWins = h_obWins + a_obWins
    obDraws = h_obDraws + a_obDraws
    obLosses = h_obLosses + a_obLosses

    exWins = h_exWins + a_exWins
    exDraws = h_exDraws + a_exDraws
    exLosses = h_exLosses + a_exLosses

    obPts = h_obPts + a_obPts
    exPts = h_exPts + a_exPts

    obSG = h_obSG + a_obSG
    obCG = h_obCG + a_obCG

    exSG = h_exSG + a_exSG
    exCG = h_exCG + a_exCG

    played = h_played + a_played

    try:
        obPPM = obPts / played
        exPPM = exPts / played
        h_obPPM = h_obPts / h_played
        h_exPPM = h_exPts / h_played
        a_obPPM = a_obPts / a_played
        a_exPPM = a_exPts / a_played
        obSGPM = obSG / played
        obCGPM = obCG / played
        h_obSGPM = h_obSG / h_played
        h_obCGPM = h_obCG / h_played
        a_obSGPM = a_obSG / a_played
        a_obCGPM = a_obCG / a_played
        exSGPM = exSG / played
        exCGPM = exCG / played
        h_exSGPM = h_exSG / h_played
        h_exCGPM = h_exCG / h_played
        a_exSGPM = a_exSG / a_played
        a_exCGPM = a_exCG / a_played
    except ZeroDivisionError:
        obPPM = 0
        exPPM = 0
        h_obPPM = 0
        h_exPPM = 0
        a_obPPM = 0
        a_exPPM = 0
        obSGPM = 0
        obCGPM = 0
        h_obSGPM = 0
        h_obCGPM = 0
        a_obSGPM = 0
        a_obCGPM = 0
        exSGPM = 0
        exCGPM = 0
        h_exSGPM = 0
        h_exCGPM = 0
        a_exSGPM = 0
        a_exCGPM = 0
    
    try: 
        performance = obPts / exPts
        performance_h = h_obPts / h_exPts
        performance_a = a_obPts / a_exPts
        p_SG = obSG / exSG
        p_CG = obCG / exCG
        p_h_SG = h_obSG / h_exSG
        p_h_CG = h_obCG / h_exCG
        p_a_SG = a_obSG / a_exSG
        p_a_CG = a_obCG / a_exCG
    except ZeroDivisionError:
        performance = 0
        performance_h = 0
        performance_a = 0
        p_SG = 0
        p_CG = 0
        p_h_SG = 0
        p_h_CG = 0
        p_a_SG = 0
        p_a_CG = 0

    try:
        winsP100 = obWins*100 / exWins
        drawsP100 = obDraws*100 / exDraws
        lossesP100 = obLosses*100 / exLosses
        h_winsP100 = h_obWins*100 / h_exWins
        h_drawsP100 = h_obDraws*100 / h_exDraws
        h_lossesP100 = h_obLosses*100 / h_exLosses
        a_winsP100 = a_obWins*100 / a_exWins
        a_drawsP100 = a_obDraws*100 / a_exDraws
        a_lossesP100 = a_obLosses*100 / a_exLosses
        SGP100 = obSG*100 / exSG
        CGP100 = obCG*100 / exCG
        h_SGP100 = h_obSG*100 / h_exSG
        h_CGP100 = h_obCG*100 / h_exCG
        a_SGP100 = a_obSG*100 / a_exSG
        a_CGP100 = a_obCG*100 / a_exCG
    except ZeroDivisionError:
        winsP100 = 0
        drawsP100 = 0
        lossesP100 = 0
        h_winsP100 = 0
        h_drawsP100 = 0
        h_lossesP100 = 0
        a_winsP100 = 0
        a_drawsP100 = 0
        a_lossesP100 = 0

    results = [
        referee,played, h_played, a_played, performance, performance_h, performance_a,
        winsP100, drawsP100, lossesP100,
        h_winsP100, h_drawsP100, h_lossesP100,
        a_winsP100, a_drawsP100, a_lossesP100,
        obWins, exWins, obDraws, exDraws, obLosses, exLosses, 
        h_obWins, h_exWins, h_obDraws, h_exDraws, h_obLosses, h_exLosses,
        a_obWins, a_exWins, a_obDraws, a_exDraws, a_obLosses, a_exLosses,
        obPPM, exPPM, h_obPPM, h_exPPM, a_obPPM, a_exPPM,
        obPts, exPts, h_obPts, h_exPts, a_obPts, a_exPts,
        p_SG,p_CG,p_h_SG,p_h_CG,p_a_SG,p_a_CG,
        obSG, obCG,
        exSG, exCG,
        obSGPM, obCGPM, h_obSGPM, h_obCGPM, a_obSGPM, a_obCGPM,
        exSGPM, exCGPM, h_exSGPM, h_exCGPM, a_exSGPM, a_exCGPM,
        h_obSG, h_obCG,
        h_exSG, h_exCG,
        a_obSG, a_obCG,
        a_exSG, a_exCG,
        SGP100, CGP100, h_SGP100, h_CGP100, a_SGP100, a_CGP100
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

    control_counter = 0

    for referee in referees_list:

        control_counter += 1
        if control_counter > 10:
            break
        referees_results.append(referee_profile(df_matches, metron, referee))

    df_referees = pd.DataFrame(referees_results, columns=['Referee','Matches','H_Matches','A_Matches','Performance','H_Performance','A_Performance','Wins%','Draws%','Losses%','H_Wins%','H_Draws%','H_Losses%','A_Wins%','A_Draws%','A_Losses%','obWins','exWins','obDraws','exDraws','obLosses','exLosses','H_obWins','H_exWins','H_obDraws','H_exDraws','H_obLosses','H_exLosses','A_obWins','A_exWins','A_obDraws','A_exDraws','A_obLosses','A_exLosses','obPPM','exPPM','h_obPPM','h_exPPM','a_obPPM','a_exPPM','obPts','exPts','h_obPts','h_exPts','a_obPts','a_exPts','p_SG','p_CG','p_h_SG','p_h_CG','p_a_SG','p_a_CG','obSG','obCG','exSG','exCG','obSGPM','obCGPM','h_obSGPM','h_obCGPM','a_obSGPM','a_obCGPM','exSGPM','exCGPM','h_exSGPM','h_exCGPM','a_exSGPM','a_exCGPM','h_obSG','h_obCG','h_exSG','h_exCG','a_obSG','a_obCG','a_exSG','a_exCG','SG%','CG%','h_SG%','h_CG%','a_SG%','a_CG%'])

    return df_referees


if __name__ == "__main__":

    # Loading the long term reference Metron
    metron = pd.read_excel('reference_system_means.xlsx')
    metron = metron[['Escenario','FTHG','FTAG','HTHG','HTAG','HS','AS','HST','AST','HF','AF','HY','AY','HR','AR']]

    # Loading the DF of european league matches from 2000-2001 to 2020-2021
    df_matches = pd.read_csv('D:\Dropbox\La Cima del Éxito\Futbol\Ligas_csv\df_Leagues.csv')
    #seasons_list = ['2000-2001','2001-2002','2002-2003','2003-2004','2004-2005','2005-2006','2006-2007','2007-2008','2008-2009','2009-2010','2010-2011','2011-2012','2012-2013','2013-2014','2014-2015','2015-2016','2016-2017','2017-2018','2018-2019','2019-2020','2020-2021']
    
    referees_profiles = referees_performance(df_matches, metron)
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