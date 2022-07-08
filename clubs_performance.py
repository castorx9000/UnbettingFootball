import pandas as pd
import numpy as np
import matplotlib as plt
import math
import datetime


# Function to convert string to datetime
def convert_string_to_datetime(date_time):
    
    format = '%b %d %Y %I:%M%p' # the format
    datetime_str = datetime.datetime.strptime(date_time, format)

    return datetime_str 


# Function to create a subset of matches given conditions: season, date_start, date_end and league
def selecting_matches(matches, season, date_start, date_end, league):

    date_start = convert_string_to_datetime(date_start)
    date_end = convert_string_to_datetime(date_end)

    matches = matches[matches['Season'] == season]
    matches = matches[matches['League'] == league]
    matches = matches[matches['Date (GMT 0)'] > date_start]
    matches = matches[matches['Date (GMT 0)'] < date_end]

    return matches


# Function to create a list of clubs in a set of matches
def create_list_of_clubs(matches):

    temporary_list = []
    list_of_clubs = []
    temporary_list = matches['Home'].tolist()

    [list_of_clubs.append(x) for x in temporary_list if x not in  list_of_clubs]

    return list_of_clubs


# Function to count to number of matches of every club in a list in a set of matches
def validate_number_of_matches(matches, list_of_clubs):

    index_home = []
    home_games = matches.groupby('Home').count()
    index_home = home_games.index.values.tolist()
    home_games = home_games['Season'].tolist()
    
    index_away = []
    away_games = matches.groupby('Away').count()
    index_away = away_games.index.values.tolist()
    away_games = away_games['Season'].tolist()

    if index_away == index_home:

        total_games = len(index_home) - 1

        for i in range(len(index_home)):

            if home_games[i] + away_games[i] != total_games:
                return False
        
        else:
            return True


# Function to change odds to probabilities in a set of matches
def change_odds_to_probabilities(matches):

    matches['ProbH'] = ''
    matches['ProbD'] = ''
    matches['ProbA'] = ''
    matches['margin'] = ''
    matches['reference'] = ''

    matches.margin = ( 1/matches.B365H + 1/matches.B365D + 1/matches.B365A - 1 ) / 3
    matches.ProbH = 1/matches.B365H - matches.margin
    matches.ProbD = 1/matches.B365D - matches.margin
    matches.ProbA = 1/matches.B365A - matches.margin
    matches.reference = round(matches.ProbH,2)

    return matches


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
def club_profile(matches, metron, club):
    
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
    
        # NOTA: aquí faltará también añadir las excepciones de partidos sin datos como faltas, tarjetas, etcétera
        if math.isnan(row['ProbH']) or math.isnan(row['ProbD']) or math.isnan(row['ProbA']):
                continue
    
        if row['Home'] == club:
            
            h_exPts += 3 * row['ProbH'] + 1 * row['ProbD']
            h_exWins += row['ProbH']
            h_exDraws += row['ProbD']
            h_exLosses += row['ProbA']
            h_obSG += row['FTHG']
            h_obCG += row['FTAG']
            h_played += 1

            reference = row['reference']
            reference = find_index(reference, escenario_list)

            auxiliar = metron.loc[metron['Escenario'] == reference]
            h_exSG += auxiliar['FTHG'].values[0]
            h_exCG += auxiliar['FTAG'].values[0]
            
            if row['FTR'] == 'H':
                h_obPts += 3
                h_obWins += 1
            if row['FTR'] == 'D':
                h_obPts += 1
                h_obDraws += 1
            if row['FTR'] == 'A':
                h_obLosses += 1
        
        if row['Away'] == club:
            
            a_exPts += 3 * row['ProbA'] + 1 * row['ProbD']
            a_exWins += row['ProbA']
            a_exDraws += row['ProbD']
            a_exLosses += row['ProbH']
            a_obSG += row['FTAG']
            a_obCG += row['FTHG']
            a_played += 1

            reference = row['reference']
            reference = find_index(reference, escenario_list)

            auxiliar = metron.loc[metron['Escenario'] == reference]
            a_exSG += auxiliar['FTAG'].values[0]
            a_exCG += auxiliar['FTHG'].values[0]
            
            if row['FTR'] == 'A':
                a_obPts += 3
                a_obWins += 1
            if row['FTR'] == 'D':
                a_obPts += 1
                a_obDraws += 1
            if row['FTR'] == 'H':
                a_obLosses += 1

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
        club,played, h_played, a_played, performance, performance_h, performance_a,
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


# Function to create a table for a list of clubs from a dataframe of matches
def create_table(matches, metron):

    clubs_results = []
    list_of_clubs = create_list_of_clubs(matches)

    for club in list_of_clubs:
        
        clubs_results.append(club_profile(matches, metron, club))
    
    clubs_df = pd.DataFrame(clubs_results, columns=['Club','Matches','H_Matches','A_Matches','Performance','H_Performance','A_Performance','Wins%','Draws%','Losses%','H_Wins%','H_Draws%','H_Losses%','A_Wins%','A_Draws%','A_Losses%','obWins','exWins','obDraws','exDraws','obLosses','exLosses','H_obWins','H_exWins','H_obDraws','H_exDraws','H_obLosses','H_exLosses','A_obWins','A_exWins','A_obDraws','A_exDraws','A_obLosses','A_exLosses','obPPM','exPPM','h_obPPM','h_exPPM','a_obPPM','a_exPPM','obPts','exPts','h_obPts','h_exPts','a_obPts','a_exPts','p_SG','p_CG','p_h_SG','p_h_CG','p_a_SG','p_a_CG','obSG','obCG','exSG','exCG','obSGPM','obCGPM','h_obSGPM','h_obCGPM','a_obSGPM','a_obCGPM','exSGPM','exCGPM','h_exSGPM','h_exCGPM','a_exSGPM','a_exCGPM','h_obSG','h_obCG','h_exSG','h_exCG','a_obSG','a_obCG','a_exSG','a_exCG','SG%','CG%','h_SG%','h_CG%','a_SG%','a_CG%'])
    
    return clubs_df

if __name__ == "__main__":
    
    matches = pd.read_excel('Matches_2000_2021.xlsx')
    matches = matches[['Season', 'Date (GMT 0)', 'League','Home','DT_Home','Away','DT_Away','FTHG','FTAG','FTR','HTH','HTA','HTR','SHH','SHA','SHR','B365H','B365D','B365A']]

    metron = pd.read_excel('reference_system_means.xlsx')
    metron = metron[['Escenario','FTHG','FTAG','HTHG','HTAG','HS','AS','HST','AST','HF','AF','HY','AY','HR','AR']]

    season = '2020/2021'
    season_for_file = '2020-2021'
    league = 'Championship'
    date_start = 'Jun 1 2020 1:00AM'
    date_end = 'Jun 1 2021 1:00AM'
    tournament = 'agosto-mayo'

    matches = selecting_matches(matches, season, date_start, date_end, league)
    matches = change_odds_to_probabilities(matches)
    table = create_table(matches, metron)
    print(table)
    table.to_excel(f'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_performances\{league}_{season_for_file}_03-06-2021.xlsx', sheet_name=f'{league}_{season_for_file}')