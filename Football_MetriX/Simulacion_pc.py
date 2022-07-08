import pandas as pd
import random
import os
import numpy as np

# Input: matches dataframe
# Output: matches dataframe including Probability columns, margins of bet houses
#         and reference to use the Metron
def matches_normalization(matches):
    
    matches['ProbH'] = ''
    matches['ProbD'] = ''
    matches['ProbA'] = ''
    matches['margin'] = ''
    matches['reference'] = ''

    matches.margin = ( 1/matches.OddH + 1/matches.OddD + 1/matches.OddA - 1 ) / 3
    matches.ProbH = 1/matches.OddH - matches.margin
    matches.ProbD = 1/matches.OddD - matches.margin
    matches.ProbA = 1/matches.OddA - matches.margin
    matches.reference = round(matches.ProbH,2)

    return matches


# Input: matches dataframe
# Output: matches dataframe filtered by specified season and division
def matches_per_season_and_division(season, division, matches):
    
    matches = matches[matches['Season'] == season]
    matches = matches[matches['Div'] == division]
    
    return matches
    

# Input: matches dataframe of a specific season and division
# Output: teams dataframe for a specific season and division
def teams_in_season(matches):
    
    teams = pd.DataFrame(matches)
    teams = matches.HomeTeam.unique()

    return teams


# Input: matches dataframe of a specific season and division
# Output: empty results table dataframe of a specific season and division
def create_table_in_season(matches):

    teams = []    
    teams = teams_in_season(matches)
    table = pd.DataFrame(teams, columns=['Teams'])

    table['Points'] = 0
    table['Wins'] = 0
    table['Draws'] = 0
    table['Losses'] = 0

    return table


# Input: empty results table dataframe and matches dataframe filtered by a specific season and division
# Output: results table df of one simulation of the specific season and division
def season_simulator(table, matches):
    
    for index, row in matches.iterrows():
    
        #Probability = np.random.random(1)[0]
        Probability = int.from_bytes(os.urandom(8), byteorder="big") / ((1 << 64) - 1)
        Result = ''
        Home = row[27]
        Draw = row[28] + Home
        Away = row[29] + Draw

        if Probability <= Home:
            Result = 'H'
        elif Probability <= Draw:
            Result = 'D'
        elif Probability <= Away:
            Result = 'A'

        Home = table[table['Teams'] == row[3]].index.tolist()
        Away = table[table['Teams'] == row[4]].index.tolist()

        if Result == 'H':
            
            table.at[Home[0], 'Wins'] += 1 
            table.at[Away[0], 'Losses'] += 1
            table.at[Home[0], 'Points'] += 3

        if Result == 'D':

            table.at[Home[0], 'Draws'] += 1
            table.at[Away[0], 'Draws'] += 1
            table.at[Home[0], 'Points'] += 1
            table.at[Away[0], 'Points'] += 1

        if Result == 'A':
            table.at[Home[0], 'Losses'] += 1
            table.at[Away[0], 'Wins'] += 1
            table.at[Away[0], 'Points'] += 3
        
    return table


# Input: unordered results table dataframe
# Output: results table dataframe with performance indicators sorted by performance
def final_performance(table):
    
    table['Performance'] = 0
    table['Matches'] = table.Wins + table.Draws + table.Losses
    table['Wins100'] = 0
    table['Draws100'] = 0
    table['Losses100'] = 0
    
    table.Performance = round(table.Points / (table.Matches * 3) * 100, 2)
    
    table.Wins100 = round(table.Wins / table.Matches * 100, 1)
    table.Draws100 = round(table.Draws / table.Matches * 100, 1)
    table.Losses100 = round(table.Losses / table.Matches * 100, 1)
    
    columns = ['Teams', 'Performance', 'Wins100', 'Draws100', 'Losses100', 'Points', 'Matches', 'Wins', 'Draws', 'Losses']
    table = table[columns]
    table = table.sort_values(by=['Performance'], ascending=False)
    table.index = np.arange(1, len(table) + 1)
        
    return table


# Input: matches dataframe filtered by a specific season and division
# Output: empty positions table

def create_table_by_positions(matches):
    
    teams = []
    teams = teams_in_season(matches)
    table = pd.DataFrame(teams, columns=['Teams'])

    table['1'] = 0
    table['2'] = 0
    table['3'] = 0
    table['4'] = 0
    table['5'] = 0
    table['6'] = 0
    table['7'] = 0
    table['8'] = 0
    table['9'] = 0
    table['10'] = 0
    table['11'] = 0
    table['12'] = 0
    table['13'] = 0
    table['14'] = 0
    table['15'] = 0
    table['16'] = 0
    table['17'] = 0
    table['18'] = 0
    table['19'] = 0
    table['20'] = 0
    #table['21'] = 0
    #table['22'] = 0
    #table['23'] = 0
    #table['24'] = 0

    table.index = np.arange(1, len(table) + 1)

    return table


# Input: table by position df and accumulated table by positions
# Output: updated table by position dataframe
# PENDIENTE: esta tabla debe ajustarse al número de equipos en la liga
def performance_by_position(table, table_by_positions):

    team = []
    position = []
    table = table.sort_values(by=['Points'], ascending=False)
    table.index = np.arange(1, len(table) + 1)
    
    for index, row in table.iterrows():
        team = table[table['Teams'] == row[0]].index.tolist()
        position = table_by_positions[table_by_positions['Teams'] == row[0]].index.tolist()
        table_by_positions.at[position[0], f'{team[0]}'] += 1

    return table_by_positions

# Input: results table with accumulated results of all iterations
#        results table with accumulated results until the previous iteration
# Output: empty results table used as auxilar to produce the returned table
def current_season(table_current, table_previous, table_empty):
    
    table = table_empty.copy()
    team = []
    points_previous = 0
    points_current = 0
    wins_previous = 0
    wins_current = 0
    draws_previous = 0
    draws_current = 0
    losses_previous = 0
    losses_current = 0
    
    #table = table.sort_values(by=['Points'], ascending=False)
    table.index = np.arange(1, len(table) + 1)
    table_previous.index = np.arange(1, len(table) + 1)
    table_current.index = np.arange(1, len(table) + 1)

    for index, row in table.iterrows():
        team = table[table['Teams'] == row[0]].index.tolist()
        points_previous = table_previous.at[team[0], 'Points']
        points_current = table_current.at[team[0], 'Points']
        
        wins_previous = table_previous.at[team[0], 'Wins']
        wins_current = table_current.at[team[0], 'Wins']
        
        draws_previous = table_previous.at[team[0], 'Draws']
        draws_current = table_current.at[team[0], 'Draws']

        losses_previous = table_previous.at[team[0], 'Losses']
        losses_current = table_current.at[team[0], 'Losses']
        
        table.at[team[0], 'Points'] = points_current - points_previous
        table.at[team[0], 'Wins'] = wins_current - wins_previous
        table.at[team[0], 'Draws'] = draws_current - draws_previous
        table.at[team[0], 'Losses'] = losses_current - losses_previous

    return table


# Input: number of iterations to simulate of a specific season, division and matches
# Output: TUPLE [0] final accumulated results after all simulations
#               [1] final table of accumulated positions after all simulations
def simulator_multiple_seasons(simulations_number, season, division, matches):

    matches = matches_normalization(matches)
    matches = matches_per_season_and_division(season, division, matches)
    
    # Builds table used to accumulate results (through all iterations)
    table = create_table_in_season(matches)
    
    # table used to gather results of only the current season (one iteration)
    table_current_season = table.copy()

    # table used to reset the previous table after each iteration
    table_previous = table.copy()

    # table used to find the current table using the las season simulation
    # by substracting the accumulated results table from the previous iteration
    # from the current accumulated results table
    table_empty = table.copy()

    # Builds table used to accumulate positions at the end of each season
    table_by_positions = create_table_by_positions(matches)

    while simulations_number > 0:

        table_previous = table.copy()
        table = season_simulator(table, matches)
        table_current_season = current_season(table, table_previous, table_empty)
        table_by_positions = performance_by_position(table_current_season, table_by_positions)

        simulations_number -= 1

    table = final_performance(table)

    return table, table_by_positions


if __name__ == "__main__":
    
    matches = pd.read_excel('df_Leagues_2021-2022.xlsx')
    season = '2021-2022'
    division = 'MX1F'
    iterations = 5000

    final_table = simulator_multiple_seasons(iterations, season, division, matches)

    print(final_table[0])
    print(final_table[1])

    final_table[1].to_csv(f'{season}_{division}_position_{iterations}_iterations.csv', index=False)
    final_table[0].to_csv(f'\\season-2021-2022\{season}_{division}_performance_{iterations}_iterations.csv')