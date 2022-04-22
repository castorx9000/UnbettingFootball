from typing import final
import numpy as np
import matplotlib as plt
import math
import pandas as pd


def create_table(matches, teams_list):
    
    print(teams_list)

    output = []

    for team in teams_list:

        auxiliar_df = matches

        Totals = 0
        Points, xPoints, GoalDiff, xGoalDiff = 0, 0, 0, 0
        Wins, Draws, Losses = 0, 0, 0
        xWins, xDraws, xLosses = 0, 0, 0
        GoalsF, xGoalsF, GoalsA, xGoalsA = 0, 0, 0, 0
        HTGoalsF, xHTGoalsF, HTGoalsA, xHTGoalsA = 0, 0, 0, 0
        ShotsF, xShotsF, ShotsA, xShotsA = 0, 0, 0, 0
        ShotsTF, xShotsTF, ShotsTA, xShotsTA = 0, 0, 0, 0
        Fouls, xFouls, FoulsA, xFoulsA = 0, 0, 0, 0
        YCard, xYCard, YCardA, xYCardA = 0, 0, 0, 0
        RCard, xRCard, RCardA, xRCardA = 0, 0, 0, 0

        auxiliar_df = matches[matches['HomeTeam'] == team]
        Totals = auxiliar_df.sum(axis = 0, skipna=True)
        
        GoalsF += Totals['FTHG']
        xGoalsF += Totals['xFTHG']
        GoalsA += Totals['FTAG']
        xGoalsA += Totals['xFTAG']
        HTGoalsF += Totals['HTHG']
        xHTGoalsF += Totals['xHTHG']
        HTGoalsA += Totals['HTAG']
        xHTGoalsA += Totals['xHTAG']
        ShotsF += Totals['HS']
        xShotsF += Totals['xHS']
        ShotsA += Totals['AS']
        xShotsA += Totals['xAS']
        ShotsTF += Totals['HST']
        xShotsTF += Totals['xHST']
        ShotsTA += Totals['AST']
        xShotsTA += Totals['xAST']
        Fouls += Totals['HF']
        xFouls += Totals['xHF']
        FoulsA += Totals['AF']
        xFoulsA += Totals['xAF']
        YCard += Totals['HY']
        xYCard += Totals['xHY']
        YCardA += Totals['AY']
        xYCardA += Totals['xAY']
        RCard += Totals['HR']
        xRCard += Totals['xHR']
        RCardA += Totals['AR']
        xRCardA += Totals['xAR']

        Record = Totals['FTR']

        Wins += Record.count('H')
        Draws += Record.count('D')
        Losses += Record.count('A')

        xWins += Totals['ProbH']
        xDraws += Totals['ProbD']
        xLosses += Totals['ProbA']
        
        auxiliar_df = matches[matches['AwayTeam'] == team]
        Totals = auxiliar_df.sum(axis = 0, skipna=True)
        
        GoalsF += Totals['FTAG']
        xGoalsF += Totals['xFTAG']
        GoalsA += Totals['FTHG']
        xGoalsA += Totals['xFTHG']
        HTGoalsF += Totals['HTAG']
        xHTGoalsF += Totals['xHTAG']
        HTGoalsA += Totals['HTHG']
        xHTGoalsA += Totals['xHTHG']
        ShotsF += Totals['AS']
        xShotsF += Totals['xAS']
        ShotsA += Totals['HS']
        xShotsA += Totals['xHS']
        ShotsTF += Totals['AST']
        xShotsTF += Totals['xAST']
        ShotsTA += Totals['HST']
        xShotsTA += Totals['xHST']
        Fouls += Totals['AF']
        xFouls += Totals['xAF']
        FoulsA += Totals['HF']
        xFoulsA += Totals['xHF']
        YCard += Totals['AY']
        xYCard += Totals['xAY']
        YCardA += Totals['HY']
        xYCardA += Totals['xHY']
        RCard += Totals['AR']
        xRCard += Totals['xAR']
        RCardA += Totals['HR']
        xRCardA += Totals['xHR']

        Record = Totals['FTR']

        Wins += Record.count('A')
        Draws += Record.count('D')
        Losses += Record.count('H')

        xWins += Totals['ProbA']
        xDraws += Totals['ProbD']
        xLosses += Totals['ProbH']

        Points = Wins * 3 + Draws
        xPoints = xWins * 3 + xDraws

        GoalDiff = GoalsF - GoalsA
        xGoalDiff = xGoalsF - xGoalsA
        
        list = [
            team,
            Points, xPoints,
            Wins, Draws, Losses, xWins, xDraws, xLosses,
            GoalDiff, xGoalDiff, GoalsF, xGoalsF, GoalsA, xGoalsA,
            HTGoalsF, xHTGoalsF, HTGoalsA, xHTGoalsA,
            ShotsF, xShotsF, ShotsA, xShotsA,
            ShotsTF, xShotsTF, ShotsTA, xShotsTA,
            Fouls, xFouls, FoulsA, xFoulsA,
            YCard, xYCard, YCardA, xYCardA,
            RCard, xRCard, RCardA, xRCardA
            ]

        output.append(list)

    final_table = pd.DataFrame(output, columns=['team','Points', 'xPoints','Wins', 'Draws', 'Losses', 'xWins', 'xDraws', 'xLosses','GoalDiff', 'xGoalDiff', 'GoalsF', 'xGoalsF', 'GoalsA', 'xGoalsA','HTGoalsF', 'xHTGoalsF', 'HTGoalsA', 'xHTGoalsA','ShotsF', 'xShotsF', 'ShotsA', 'xShotsA','ShotsTF', 'xShotsTF', 'ShotsTA', 'xShotsTA','Fouls', 'xFouls', 'FoulsA', 'xFoulsA','YCard', 'xYCard', 'YCardA', 'xYCardA','RCard', 'xRCard', 'RCardA', 'xRCardA'])
    
    return final_table
              

if __name__ == '__main__':

    metron =pd.read_excel('D:\Dropbox\La Cima del Éxito\Futbol\\reference_system_means.xlsx')
    matches = pd.read_excel('D:\Dropbox\La Cima del Éxito\Futbol\\articulos\WCQ 2022 07 11 2021\WCQ2022_CONMEBOL.xlsx')
    teams_list = matches['HomeTeam'].tolist()
    teams_list = list(set(teams_list))
    date = '18-11-2021'

    final_table = create_table(matches, teams_list)
    final_table.to_csv(f'D:\Dropbox\La Cima del Éxito\Futbol\\articulos\WCQ 2022 07 11 2021\WCQ2022_CONMEBOL_{date}.csv',encoding='utf-8',index=True)