from nis import match
import numpy as np
import pandas as pd
import math


def coaches_list_creator():

    coaches_df = pd.read_csv('Coaches/Coaches_list.csv')
    coaches_list = []
    coaches_df.columns=['Coach']
    coaches_list = coaches_df['Coach'].tolist()

    return coaches_list


def add_reference_column(matches):

    matches['reference'] = ''
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
    
    escenario_list = metron.loc[:,'Escenario'].values.tolist()
    metron.index = escenario_list
    reference_list = matches['reference'].values.tolist()
    expected_values = []

    for element in reference_list:
        
        if element <= 0.08:
            element = 0.08
        
        if element >= 0.92:
            element = 0.92

        expected_values.append(metron.loc[element,:].values.tolist())
        
    expected_values = pd.DataFrame(expected_values, columns = ['reference','OddH','OddD','OddA','ProbH','ProbD','ProbA','xPtsH','xPtsA','xGoals','xFTHG','xFTAG','xHTHG','xHTAG','xHS','xAS','xHST','xAST','xHSM','xASM','xHF','xAF','xHY','xAY','xHR','xAR'])
    expected_values = expected_values[['reference','xPtsH','xPtsA','xGoals','xFTHG','xFTAG','xHTHG','xHTAG','xHS','xAS','xHST','xAST','xHSM','xASM','xHF','xAF','xHY','xAY','xHR','xAR']]
    matches = pd.merge(matches, expected_values, on='reference')

    matches.drop_duplicates(inplace=True)
    
    return matches


def profile_builder(coaches_list, metron):

    coach_df = pd.DataFrame()
    auxiliar_df = pd. DataFrame()
    teams_list = []
    
    output = []
    coach_output = []

    for coach in coaches_list:

        coach_df = pd.read_excel(f'Coaches/{coach}')
        
        coach_df = add_reference_column(coach_df)
        coach_df = insert_escenarios(coach_df, metron)
        
        coach_df['Date'] = pd.to_datetime(coach_df['Date'])
        coach_df = coach_df.sort_values(by='Date')

        rPoints, Points, xPoints = 0, 0, 0
        rPointsH, PointsH, xPointsH = 0, 0, 0
        rPointsA, PointsA, xPointsA = 0, 0, 0
        Totals, rWins, Wins, xWins, rDraws, Draws, xDraws, rLosses, Losses, xLosses = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        rWinsH, WinsH, xWinsH, rDrawsH, DrawsH, xDrawsH, rLossesH, LossesH, xLossesH = 0, 0, 0, 0, 0, 0, 0 , 0, 0
        rWinsA, WinsA, xWinsA, rDrawsA, DrawsA, xDrawsA, rLossesA, LossesA, xLossesA = 0, 0, 0, 0, 0, 0, 0 , 0, 0
        matches, matchesH, matchesA = 0, 0, 0
        rGSc, GSc, xGSc, rGAg, GAg, xGAg, GDf, xGDf = 0, 0, 0, 0, 0, 0, 0, 0
        rGScA, rGAgA, GScA, GAgA, xGScA, xGAgA = 0, 0, 0, 0, 0, 0
        rGScH, GScH, xGScH, rGAgH, GAgH, xGAgH, GDfH, xGDfH, GDfA, xGDfA = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

        teams_list = list(set(coach_df['Team'].tolist()))
        
        for team in teams_list:

            auxiliar_df = coach_df[coach_df['HomeTeam'] == team]
            Totals = auxiliar_df.sum(axis=0, skipna=True, numeric_only=None)
            Record = Totals['FTR']

            WinsH += Record.count('H')
            xWinsH += Totals['ProbH']
            DrawsH += Record.count('D')
            xDrawsH += Totals['ProbD']
            LossesH += Record.count('A')
            xLossesH += Totals['ProbA']

            GScH += Totals['FTHG']   
            xGScH += Totals['xFTHG']
            GAgH += Totals['FTAG']
            xGAgH += Totals['xFTAG']

            auxiliar_df = coach_df[coach_df['AwayTeam'] == team]
            Totals = auxiliar_df.sum(axis=0, skipna=True, numeric_only=None)

            WinsA += Totals['FTR'].count('A')
            xWinsA += Totals['ProbA']
            DrawsA += Totals['FTR'].count('D')
            xDrawsA += Totals['ProbD']
            LossesA += Totals['FTR'].count('H')
            xLossesA += Totals['ProbH']

            GScA += Totals['FTAG']
            xGScA += Totals['xFTAG']
            GAgA += Totals['FTHG']
            xGAgA += Totals['xFTHG']

        PointsH = WinsH*3 + DrawsH
        xPointsH = xWinsH*3 + xDrawsH
        PointsA = WinsA*3 + DrawsA
        xPointsA = xWinsA*3 + xDrawsA

        Points = PointsH + PointsA
        xPoints = xPointsH + xPointsA
        Wins = WinsH + WinsA
        xWins = xWinsH + xWinsA
        Draws = DrawsH + DrawsA
        xDraws = xDrawsH + xDrawsA
        Losses = LossesH + LossesA
        xLosses = xLossesH + xLossesA

        GSc = GScH + GScA
        xGSc = xGScH + xGScA
        GAg = GAgH + GAgA
        xGAg = xGAgH + xGAgA

        GDf = GSc - GAg
        xGDf = xGSc - xGAg
        GDfH = GScH - GAgH
        xGDfH = xGScH - xGAgH
        GDfA = GScA - GAgA
        xGDfA = xGScA- xGAgA

        rPoints = Points / xPoints
        rPointsH = PointsH / xPointsH
        rPointsA = PointsA / xPointsA
        rWins = Wins / xWins
        rWinsH = WinsH / xWinsH
        rWinsA = WinsA / xWinsA
        rDraws = Draws / xDraws
        rDrawsH = DrawsH / xDrawsH
        rDrawsA = DrawsA / xDrawsA
        rLosses = Losses / xLosses
        rLossesH = LossesH / xLossesH
        rLossesA = LossesA / xLossesA
            
        rGSc = GSc / xGSc
        rGAg = GAg / xGAg
        rGScH = GScH / xGScH
        rGAgH = GAgH / xGAgH
        rGScA = GScA / xGScA
        rGAgA = GAgA / xGAgA

        matches = Wins + Draws + Losses
        matchesH = WinsH + DrawsH + LossesH
        matchesA = WinsA + DrawsA + LossesA

        coach = coach.replace('.xlsx','')
        
        coach_output = [
                coach, matches, matchesH, matchesA,
                rPoints, Points, xPoints,
                rPointsH, PointsH, xPointsH,
                rPointsA, PointsA, xPointsA,
                rWins, Wins, xWins, rDraws, Draws, xDraws, rLosses, Losses, xLosses,
                rWinsH, WinsH, xWinsH, rDrawsH, DrawsH, xDrawsH, rLossesH, LossesH, xLossesH,
                rWinsA, WinsA, xWinsA, rDrawsA, DrawsA, xDrawsA, rLossesA, LossesA, xLossesA,
                rGSc, GSc, xGSc, rGAg, GAg, xGAg, GDf, xGDf,
                rGScH, GScH, xGScH, rGAgH, GAgH, xGAgH, 
                rGScA, rGAgA, GScA, GAgA, xGScA, xGAgA,
                GDfH, xGDfH, GDfA, xGDfA
            ]

        output.append(coach_output)

        coaches_results_df = pd.DataFrame(output, columns=[
            'Coach', 'matches', 'matchesH', 'matchesA',
            'rPoints','Points','xPoints','rPointsH','PointsH','xPointsH','rPointsA','PointsA','xPointsA',
            'rWins','Wins', 'xWins', 'rDraws', 'Draws', 'xDraws', 'rLosses', 'Losses', 'xLosses', 
            'rWinsH', 'WinsH', 'xWinsH', 'rDrawsH', 'DrawsH', 'xDrawsH', 'rLossesH', 'LossesH', 'xLossesH', 
            'rWinsA', 'WinsA', 'xWinsA', 'rDrawsA', 'DrawsA', 'xDrawsA', 'rLossesA', 'LossesA', 'xLossesA', 
            'rGSc', 'GSc', 'xGSc', 'rGAg', 'GAg', 'xGAg', 'GDf', 'xGDf',
            'rGScH', 'GScH', 'xGScH', 'rGAgH', 'GAgH', 'xGAgH', 
            'rGScA', 'rGAgA', 'GScA', 'GAgA', 'xGScA', 'xGAgA', 
            'GDfH', 'xGDfH', 'GDfA', 'xGDfA'])

        print(coaches_results_df)
    coaches_results_df.to_excel(f'Coaches_xValues/coaches_results.xlsx', index=False, sheet_name='coaches_summary')


if __name__ == '__main__':

    metron = pd.read_excel('metron.xlsx')

    coaches_list = coaches_list_creator()

    profile_builder(coaches_list, metron)