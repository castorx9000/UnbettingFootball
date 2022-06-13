from typing import final
import numpy as np
import matplotlib as plt
import math
import pandas as pd

def format_matches(matches, metron):

    matches = change_odds_to_probabilities(matches)
    matches = insert_escenarios(matches, metron)
    return matches


def change_odds_to_probabilities(matches):

    escenario_list = []

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

    escenario_list = matches['reference'].values.tolist()

    auxiliar_list = []

    for escenario in escenario_list:

        escenario *= 100
        escenario = int(escenario)

        if escenario % 2 == 1:
            escenario -= 1
        if escenario <= 0.08:
            escenario = 0
        
        auxiliar_list.append(round(escenario,0) / 100)
    
    matches['reference'] = auxiliar_list

    return matches


def insert_escenarios(matches, metron):

    escenario_list = metron.loc[:,'reference'].values.tolist()
    metron.index = escenario_list
    reference_list = matches['reference'].values.tolist()
    expected_values = []

    for element in reference_list:
        
        if element <= 0.08:
            element = 0.08
        
        if element >= 0.92:
            element = 0.92

        expected_values.append(metron.loc[element,:].values.tolist())

    expected_values = pd.DataFrame(expected_values, columns = ['reference','OddH','OddD','OddA','ProbH','ProbD','ProbA','xPHome','xPAway','xGoals','xFTHG','xFTAG','xHTHG','xHTAG','xHS','xAS','xHST','xAST','xHSM','xASM','xHF','xAF','xHY','xAY','xHR','xAR'])
    expected_values = expected_values[['reference','xFTHG','xFTAG','xHTHG','xHTAG','xHS','xAS','xHST','xAST','xHF','xAF','xHY','xAY','xHR','xAR']]
    print(matches)
    matches = pd.merge(matches, expected_values, on='reference')

    matches.drop_duplicates(inplace=True)
    
    return matches

    
def create_table(matches, teams_list, division):
    
    output = []

    for team in teams_list:

        auxiliar_df = matches

        Totals = 0
        rPoints = 0
        Games = 0
        Points, xPoints, GoalDiff, xGoalDiff = 0, 0, 0, 0
        rWins, rDraws, rLosses = 0, 0, 0
        Wins, Draws, Losses = 0, 0, 0
        xWins, xDraws, xLosses = 0, 0, 0
        rHWins, rHDraws, rHLosses = 0, 0, 0
        HWins, HDraws, HLosses = 0, 0, 0
        xHWins, xHDraws, xHLosses = 0, 0, 0
        rAWins, rADraws, rALosses = 0, 0, 0
        AWins, ADraws, ALosses = 0, 0, 0
        xAWins, xADraws, xALosses = 0, 0, 0
        GoalsF_Diff, GoalsA_Diff = 0, 0
        rGoalsF, rGoalsA = 0, 0
        rHGoalsF, rHGoalsA = 0, 0
        rAGoalsF, rAGoalsA = 0, 0
        GoalsF, xGoalsF, GoalsA, xGoalsA = 0, 0, 0, 0
        HGoalsF, xHGoalsF, HGoalsA, xHGoalsA = 0, 0, 0, 0
        AGoalsF, xAGoalsF, AGoalsA, xAGoalsA = 0, 0, 0, 0
        SHGoalsF, xSHGoalsF, SHGoalsA, xSHGoalsA = 0, 0, 0, 0 
        HTGoalsF, xHTGoalsF, HTGoalsA, xHTGoalsA = 0, 0, 0, 0
        rShotsF, rShotsA, rShotsTF, rShotsTA = 0, 0, 0, 0
        ShotsF, xShotsF, ShotsA, xShotsA = 0, 0, 0, 0
        ShotsTF, xShotsTF, ShotsTA, xShotsTA = 0, 0, 0, 0
        rFouls, rFoulsA = 0, 0
        Fouls, xFouls, FoulsA, xFoulsA = 0, 0, 0, 0
        rYCard, rYCardA, rRCard, rRCardA = 0, 0, 0, 0
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
        HGoalsF += Totals['FTHG']
        xHGoalsF += Totals['xFTHG']
        HGoalsA += Totals['FTAG']
        xHGoalsA += Totals['xFTAG']
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

        HWins += Record.count('H')
        HDraws += Record.count('D')
        HLosses += Record. count('A')

        xHWins += Totals['ProbH']
        xHDraws += Totals['ProbD']
        xHLosses += Totals['ProbA']
        
        auxiliar_df = matches[matches['AwayTeam'] == team]
        Totals = auxiliar_df.sum(axis = 0, skipna=True)
        
        GoalsF += Totals['FTAG']
        xGoalsF += Totals['xFTAG']
        GoalsA += Totals['FTHG']
        xGoalsA += Totals['xFTHG']
        AGoalsF += Totals['FTAG']
        xAGoalsF += Totals['xFTAG']
        AGoalsA += Totals['FTHG']
        xAGoalsA += Totals['xFTHG']
        HTGoalsF += Totals['HTAG']
        xHTGoalsF += Totals['xHTAG']
        HTGoalsA += Totals['HTHG']
        xHTGoalsA += Totals['xHTHG']
        SHGoalsF = GoalsF - HTGoalsF
        xSHGoalsF = xGoalsF - xHTGoalsF
        SHGoalsA = HTGoalsA - GoalsA
        xSHGoalsA = xHTGoalsA - xGoalsA
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

        AWins += Record.count('A')
        ADraws += Record.count('D')
        ALosses += Record. count('H')

        xAWins += Totals['ProbA']
        xADraws += Totals['ProbD']
        xALosses += Totals['ProbH']

        rWins = Wins / xWins
        rDraws = Draws / xDraws
        rLosses = Losses / xLosses

        rHWins = HWins / xHWins
        rHDraws = HDraws / xHDraws
        rHLosses = HLosses / xHLosses

        rAWins = AWins / xAWins
        rADraws = ADraws / xADraws
        rALosses = ALosses / xALosses

        Games = Wins + Draws + Losses

        Points = Wins * 3 + Draws
        xPoints = xWins * 3 + xDraws
        rPoints = Points / xPoints

        rGoalsF = GoalsF / xGoalsF
        rGoalsA = GoalsA / xGoalsA

        rHGoalsF = HGoalsF / xHGoalsF
        rHGoalsA = HGoalsA / xHGoalsA

        rAGoalsF = AGoalsF / xAGoalsF
        rAGoalsA = AGoalsA / xAGoalsA

        GoalDiff = GoalsF - GoalsA
        xGoalDiff = xGoalsF - xGoalsA
        
        GoalsF_Diff = GoalsF - xGoalsF
        GoalsA_Diff = xGoalsA - GoalsA

        rShotsF = ShotsF / xShotsF
        rShotsA = ShotsA / xShotsA
        rShotsTF = ShotsTF / xShotsTF
        rShotsTA = ShotsTA / xShotsTA

        rFouls = Fouls / xFouls
        rFoulsA = FoulsA / xFoulsA
        rYCard = YCard / xYCard
        rYCardA = YCardA / xYCardA
        rRCard = RCard / xRCard
        rRCardA = RCardA / xRCardA
        
        list = [
            team, division,
            rPoints, Points, xPoints,
            Games, rWins, rDraws, rLosses,
            Wins, Draws, Losses, xWins, xDraws, xLosses,
            GoalDiff, xGoalDiff, rGoalsF, rGoalsA, GoalsF, xGoalsF, GoalsA, xGoalsA,
            SHGoalsF, xSHGoalsF, SHGoalsA, xSHGoalsA,
            HTGoalsF, xHTGoalsF, HTGoalsA, xHTGoalsA,
            ShotsF, xShotsF, ShotsA, xShotsA,
            ShotsTF, xShotsTF, ShotsTA, xShotsTA,
            Fouls, xFouls, FoulsA, xFoulsA,
            YCard, xYCard, YCardA, xYCardA,
            RCard, xRCard, RCardA, xRCardA,
            GoalsF_Diff, GoalsA_Diff, 
            rShotsF, rShotsA, rShotsTF, rShotsTA,
            rFouls, rFoulsA, 
            rYCard, rYCardA, rRCard, rRCardA,
            rHWins, rHDraws, rHLosses,
            HWins, HDraws, HLosses,
            xHWins, xHDraws, xHLosses,
            rAWins, rADraws, rALosses,
            AWins, ADraws, ALosses,
            xAWins, xADraws, xALosses,
            rHGoalsF, rHGoalsA,
            rAGoalsF, rAGoalsA,
            HGoalsF, xHGoalsF, HGoalsA, xHGoalsA,
            AGoalsF, xAGoalsF, AGoalsA, xAGoalsA

            ]

        output.append(list)

    final_table = pd.DataFrame(output, columns=['Club','Division','rPoints','Points','xPoints','Matches','rWins','rDraws','rLosses','Wins', 'Draws', 'Losses', 'xWins', 'xDraws', 'xLosses','GoalDiff', 'xGoalDiff','rGoalsF','rGoalsA', 'GoalsF', 'xGoalsF', 'GoalsA', 'xGoalsA','SHGoalsF','xSHGoalsF','SHGoalsA','xSHGoalsA','HTGoalsF', 'xHTGoalsF', 'HTGoalsA', 'xHTGoalsA','ShotsF', 'xShotsF', 'ShotsA', 'xShotsA','ShotsTF', 'xShotsTF', 'ShotsTA', 'xShotsTA','Fouls', 'xFouls', 'FoulsA', 'xFoulsA','YCard', 'xYCard', 'YCardA', 'xYCardA','RCard', 'xRCard', 'RCardA', 'xRCardA', 'GoalsF_Diff', 'GoalsA_Diff', 'rShotsF', 'rShotsA', 'rShotsTF', 'rShotsTA', 'rFouls', 'rFoulsA', 'rYCard', 'rYCardA', 'rRCard', 'rRCardA','rHWins','rHDraws','rHLosses','HWins','HDraws','HLosses','xHWins','xHDraws','xHLosses','rAWins','rADraws','rALosses','AWins','ADraws','ALosses','xAWins','xADraws','xALosses','rHGoalsF','rHGoalsA','rAGoalsF','rAGoalsA','HGoalsF','xHGoalsF','HGoalsA','xHGoalsA','AGoalsF','xAGoalsF','AGoalsA','xAGoalsA'])
    final_table = final_table[['Club','Division','rPoints','Points','xPoints','Matches','rWins','rDraws','rLosses','Wins','Draws','Losses','xWins','xDraws','xLosses','GoalDiff','xGoalDiff','GoalsF_Diff','GoalsA_Diff','rGoalsF','rGoalsA','GoalsF','xGoalsF','GoalsA','xGoalsA','SHGoalsF','xSHGoalsF','SHGoalsA','xSHGoalsA','HTGoalsF','xHTGoalsF','HTGoalsA','xHTGoalsA','rShotsF','ShotsF','xShotsF','rShotsA','ShotsA','xShotsA','rShotsTF','ShotsTF','xShotsTF','rShotsTA','ShotsTA','xShotsTA','rFouls','Fouls','xFouls','rFoulsA','FoulsA','xFoulsA','rYCard','YCard','xYCard','rYCardA','YCardA','xYCardA','rRCard','RCard','xRCard','rRCardA','RCardA','xRCardA','rHWins','rHDraws','rHLosses','HWins','HDraws','HLosses','xHWins','xHDraws','xHLosses','rAWins','rADraws','rALosses','AWins','ADraws','ALosses','xAWins','xADraws','xALosses','rHGoalsF','rHGoalsA','rAGoalsF','rAGoalsA','HGoalsF','xHGoalsF','HGoalsA','xHGoalsA','AGoalsF','xAGoalsF','AGoalsA','xAGoalsA']]

    return final_table
              

def teams_performance(matches, metron, divisions_list):
    
    final_table = pd.DataFrame()
    matches_with_format = pd.DataFrame()

    for division in divisions_list:


        matches_division = matches[matches['Div'] == division]
        matches_division = format_matches(matches_division, metron)

        teams_list = matches_division['HomeTeam'].tolist()
        teams_list = list(set(teams_list))

        final_table = final_table.append(create_table(matches_division, teams_list, division), ignore_index=True)

        print(division, len(matches_division), len(final_table))
        matches_with_format = matches_with_format.append(matches_division)
        
    final_table.to_excel(f'Liga_MX_2020-2022.xlsx',encoding='utf-8',index=True)
    #matches_with_format.to_excel(f'Prueba_nuevas_Variables.xlsx',encoding='utf-8',index=True)

    return True


if __name__ == '__main__':

    metron = pd.read_excel('metron.xlsx')
    matches = pd.read_excel('LigaMX_2020-2022_regular_season.xlsx')
    
    teams_list = matches['HomeTeam'].tolist()
    teams_list = list(set(teams_list))

    divisions_list = matches['Div'].tolist()
    divisions_list = list(set(divisions_list))

    teams_performance(matches, metron, divisions_list)
    #matches = format_matches(matches, metron)
    #matches.to_excel(f'D:\Dropbox\La Cima del Éxito\Futbol\\articulos\matches_2013-2021_All_UEFA_FORMAT.xlsx',encoding='utf-8',index=True)

    #date = '11-12-2021'
    #season = '2013-2021'
    #competition = 'All_UEFA'

    #matches = format_matches(matches, metron)
    
    #final_table = create_table(matches, teams_list)
    #final_table.to_csv(f'D:\Dropbox\La Cima del Éxito\Futbol\\articulos\{season}_{competition}_{date}.csv',encoding='utf-8',index=True)