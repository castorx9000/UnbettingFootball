import numpy as np
from numpy.lib.function_base import asarray_chkfinite
import pandas as pd


if __name__ == "__main__":

    matches = pd.read_excel('D:\Dropbox\La Cima del Éxito\Futbol\\articulos\matches_2013-2021_All_UEFA_FORMAT.xlsx')
    matches_reference = pd.DataFrame()
    
    reference_list = matches['reference'].tolist()
    reference_list = list(set(reference_list))
    reference_list.sort(reverse=True)
    total = 0

    output = []

    home, draws, away = 0, 0, 0
    other = 0
    r_0_0, r_1_0, r_1_1, r_0_1 = 0, 0, 0, 0
    r_2_0, r_2_1, r_2_2, r_1_2, r_0_2 = 0, 0, 0, 0, 0
    r_3_0, r_3_1, r_3_2, r_3_3, r_2_3, r_1_3, r_0_3 = 0, 0, 0, 0, 0, 0, 0
    r_4_0, r_4_1, r_4_2, r_4_3, r_4_4, r_3_4, r_2_4, r_1_4, r_0_4 = 0, 0, 0, 0, 0, 0, 0, 0, 0
    r_5_0, r_5_1, r_5_2, r_5_3, r_5_4, r_5_5, r_4_5, r_3_5, r_2_5, r_1_5, r_0_5 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    r_6_0, r_6_1, r_6_2, r_6_3, r_6_4, r_6_5, r_6_6, r_5_6, r_4_6, r_3_6, r_2_6, r_1_6, r_0_6 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    r_7_0, r_0_7, r_7_1, r_1_7, r_8_0, r_0_8 = 0, 0, 0, 0, 0, 0
    m0goals, m1goal, m2goals, m3goals, m4goals, m5goals, m6goals, m7goals, m8goals, mmoregoals = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    
    for reference in reference_list:

        matches_reference = matches[matches['reference'] == reference]
        total = len(matches_reference)
        print(reference, total)

        r_8_0 = len(matches_reference[(matches_reference['FTHG'] == 8) & (matches_reference['FTAG'] == 0)])
        r_0_8 = len(matches_reference[(matches_reference['FTHG'] == 0) & (matches_reference['FTAG'] == 8)])
        r_7_0 = len(matches_reference[(matches_reference['FTHG'] == 7) & (matches_reference['FTAG'] == 0)])
        r_0_7 = len(matches_reference[(matches_reference['FTHG'] == 0) & (matches_reference['FTAG'] == 7)])
        r_7_1 = len(matches_reference[(matches_reference['FTHG'] == 7) & (matches_reference['FTAG'] == 1)])
        r_1_7 = len(matches_reference[(matches_reference['FTHG'] == 1) & (matches_reference['FTAG'] == 7)])

        r_0_6 = len(matches_reference[(matches_reference['FTHG'] == 0) & (matches_reference['FTAG'] == 6)])
        r_1_6 = len(matches_reference[(matches_reference['FTHG'] == 1) & (matches_reference['FTAG'] == 6)])
        r_2_6 = len(matches_reference[(matches_reference['FTHG'] == 2) & (matches_reference['FTAG'] == 6)])
        r_3_6 = len(matches_reference[(matches_reference['FTHG'] == 3) & (matches_reference['FTAG'] == 6)])
        r_4_6 = len(matches_reference[(matches_reference['FTHG'] == 4) & (matches_reference['FTAG'] == 6)])
        r_5_6 = len(matches_reference[(matches_reference['FTHG'] == 5) & (matches_reference['FTAG'] == 6)])
        r_6_6 = len(matches_reference[(matches_reference['FTHG'] == 6) & (matches_reference['FTAG'] == 6)])
        r_6_5 = len(matches_reference[(matches_reference['FTHG'] == 6) & (matches_reference['FTAG'] == 5)])
        r_6_4 = len(matches_reference[(matches_reference['FTHG'] == 6) & (matches_reference['FTAG'] == 4)])
        r_6_3 = len(matches_reference[(matches_reference['FTHG'] == 6) & (matches_reference['FTAG'] == 3)])
        r_6_2 = len(matches_reference[(matches_reference['FTHG'] == 6) & (matches_reference['FTAG'] == 2)])
        r_6_1 = len(matches_reference[(matches_reference['FTHG'] == 6) & (matches_reference['FTAG'] == 1)])
        r_6_0 = len(matches_reference[(matches_reference['FTHG'] == 6) & (matches_reference['FTAG'] == 0)])

        r_0_5 = len(matches_reference[(matches_reference['FTHG'] == 0) & (matches_reference['FTAG'] == 5)])
        r_1_5 = len(matches_reference[(matches_reference['FTHG'] == 1) & (matches_reference['FTAG'] == 5)])
        r_2_5 = len(matches_reference[(matches_reference['FTHG'] == 2) & (matches_reference['FTAG'] == 5)])
        r_3_5 = len(matches_reference[(matches_reference['FTHG'] == 3) & (matches_reference['FTAG'] == 5)])
        r_4_5 = len(matches_reference[(matches_reference['FTHG'] == 4) & (matches_reference['FTAG'] == 5)])
        r_5_5 = len(matches_reference[(matches_reference['FTHG'] == 5) & (matches_reference['FTAG'] == 5)])
        r_5_4 = len(matches_reference[(matches_reference['FTHG'] == 5) & (matches_reference['FTAG'] == 4)])
        r_5_3 = len(matches_reference[(matches_reference['FTHG'] == 5) & (matches_reference['FTAG'] == 3)])
        r_5_2 = len(matches_reference[(matches_reference['FTHG'] == 5) & (matches_reference['FTAG'] == 2)])
        r_5_1 = len(matches_reference[(matches_reference['FTHG'] == 5) & (matches_reference['FTAG'] == 1)])
        r_5_0 = len(matches_reference[(matches_reference['FTHG'] == 5) & (matches_reference['FTAG'] == 0)])

        r_0_4 = len(matches_reference[(matches_reference['FTHG'] == 0) & (matches_reference['FTAG'] == 4)])
        r_1_4 = len(matches_reference[(matches_reference['FTHG'] == 1) & (matches_reference['FTAG'] == 4)])
        r_2_4 = len(matches_reference[(matches_reference['FTHG'] == 2) & (matches_reference['FTAG'] == 4)])
        r_3_4 = len(matches_reference[(matches_reference['FTHG'] == 3) & (matches_reference['FTAG'] == 4)])
        r_4_4 = len(matches_reference[(matches_reference['FTHG'] == 4) & (matches_reference['FTAG'] == 4)])
        r_4_3 = len(matches_reference[(matches_reference['FTHG'] == 4) & (matches_reference['FTAG'] == 3)])
        r_4_2 = len(matches_reference[(matches_reference['FTHG'] == 4) & (matches_reference['FTAG'] == 2)])
        r_4_1 = len(matches_reference[(matches_reference['FTHG'] == 4) & (matches_reference['FTAG'] == 1)])
        r_4_0 = len(matches_reference[(matches_reference['FTHG'] == 4) & (matches_reference['FTAG'] == 0)])
        
        r_0_3 = len(matches_reference[(matches_reference['FTHG'] == 0) & (matches_reference['FTAG'] == 3)])
        r_1_3 = len(matches_reference[(matches_reference['FTHG'] == 1) & (matches_reference['FTAG'] == 3)])
        r_2_3 = len(matches_reference[(matches_reference['FTHG'] == 2) & (matches_reference['FTAG'] == 3)])
        r_3_3 = len(matches_reference[(matches_reference['FTHG'] == 3) & (matches_reference['FTAG'] == 3)])
        r_3_2 = len(matches_reference[(matches_reference['FTHG'] == 3) & (matches_reference['FTAG'] == 2)])
        r_3_1 = len(matches_reference[(matches_reference['FTHG'] == 3) & (matches_reference['FTAG'] == 1)])
        r_3_0 = len(matches_reference[(matches_reference['FTHG'] == 3) & (matches_reference['FTAG'] == 0)])

        r_0_2 = len(matches_reference[(matches_reference['FTHG'] == 0) & (matches_reference['FTAG'] == 2)])
        r_1_2 = len(matches_reference[(matches_reference['FTHG'] == 1) & (matches_reference['FTAG'] == 2)])
        r_2_2 = len(matches_reference[(matches_reference['FTHG'] == 2) & (matches_reference['FTAG'] == 2)])
        r_2_1 = len(matches_reference[(matches_reference['FTHG'] == 2) & (matches_reference['FTAG'] == 1)])
        r_2_0 = len(matches_reference[(matches_reference['FTHG'] == 2) & (matches_reference['FTAG'] == 0)])

        r_0_1 = len(matches_reference[(matches_reference['FTHG'] == 0) & (matches_reference['FTAG'] == 1)])
        r_1_1 = len(matches_reference[(matches_reference['FTHG'] == 1) & (matches_reference['FTAG'] == 1)])
        r_1_0 = len(matches_reference[(matches_reference['FTHG'] == 1) & (matches_reference['FTAG'] == 0)])

        r_0_0 = len(matches_reference[(matches_reference['FTHG'] == 0) & (matches_reference['FTAG'] == 0)])

        home = len(matches_reference[(matches_reference['FTHG'] > matches_reference['FTAG'])])
        draws = len(matches_reference[(matches_reference['FTHG'] == matches_reference['FTAG'])])
        away = len(matches_reference[(matches_reference['FTHG'] < matches_reference['FTAG'])])

        results_distribution = [r_0_0, r_1_0, r_1_1, r_0_1, r_2_0, r_2_1, r_2_2, r_1_2, r_0_2, r_3_0, r_3_1, r_3_2, r_3_3, r_2_3, r_1_3, r_0_3, r_4_0, r_4_1, r_4_2, r_4_3, r_4_4, r_3_4, r_2_4, r_1_4, r_0_4, r_5_0, r_5_1, r_5_2, r_5_3, r_5_4, r_5_5, r_4_5, r_3_5, r_2_5, r_1_5, r_0_5, r_6_0, r_6_1, r_6_2, r_6_3, r_6_4, r_6_5, r_6_6, r_5_6, r_4_6, r_3_6, r_2_6, r_1_6, r_0_6]
        
        other = total - sum(results_distribution)
        observed = sum(results_distribution)
        m0goals = r_0_0
        m1goal = r_1_0 + r_0_1
        m2goals = r_1_1 + r_2_0 + r_0_2
        m3goals = r_3_0 + r_2_1 + r_1_2 + r_0_3
        m4goals = r_4_0 + r_3_1 + r_2_2 + r_1_3 + r_0_4
        m5goals = r_5_0 + r_4_1 + r_3_2 + r_2_3 + r_1_4 + r_0_5
        m6goals = r_6_0 + r_5_1 + r_4_2 + r_3_3 + r_2_4 + r_1_5 + r_0_6
        m7goals = r_7_0 + r_6_1 + r_5_2 + r_4_3 + r_3_4 + r_2_5 + r_1_6 + r_0_7
        m8goals = r_8_0 + r_7_1 + r_6_2 + r_5_3 + r_4_4 + r_3_5 + r_2_6 + r_1_7 + r_0_8
        moregoals = total - m0goals - m1goal - m2goals - m3goals - m4goals - m5goals - m6goals - m7goals - m8goals


        results = [
            reference, total, home, draws, away,
            r_0_0, 
            r_1_0, r_1_1, r_0_1, 
            r_2_0, r_2_1, r_2_2, r_1_2, r_0_2, 
            r_3_0, r_3_1, r_3_2, r_3_3, r_2_3, r_1_3, r_0_3, 
            r_4_0, r_4_1, r_4_2, r_4_3, r_4_4, r_3_4, r_2_4, r_1_4, r_0_4, 
            r_5_0, r_5_1, r_5_2, r_5_3, r_5_4, r_5_5, r_4_5, r_3_5, r_2_5, r_1_5, r_0_5,
            r_6_0, r_6_1, r_6_2, r_6_3, r_6_4, r_6_5, r_6_6, r_5_6, r_4_6, r_3_6, r_2_6, r_1_6, r_0_6,
            observed, other,
            m0goals, m1goal, m2goals, m3goals, m4goals, m5goals, m6goals, m7goals, m8goals, moregoals
        ]

        output.append(results)
        
        #print(f'Total: {len(matches_reference)}, Home: {home}, Draw: {draws}, Away: {away}, Check: {home+draws+away}')
        
    final_results = pd.DataFrame(output, columns=['Reference','Matches','Home','Draws','Away',
            'r_0_0', 
            'r_1_0', 'r_1_1', 'r_0_1', 
            'r_2_0', 'r_2_1', 'r_2_2', 'r_1_2', 'r_0_2', 
            'r_3_0', 'r_3_1', 'r_3_2', 'r_3_3', 'r_2_3', 'r_1_3', 'r_0_3', 
            'r_4_0', 'r_4_1', 'r_4_2', 'r_4_3', 'r_4_4', 'r_3_4', 'r_2_4', 'r_1_4', 'r_0_4', 
            'r_5_0', 'r_5_1', 'r_5_2', 'r_5_3', 'r_5_4', 'r_5_5', 'r_4_5', 'r_3_5', 'r_2_5', 'r_1_5', 'r_0_5',
            'r_6_0', 'r_6_1', 'r_6_2', 'r_6_3', 'r_6_4', 'r_6_5', 'r_6_6', 'r_5_6', 'r_4_6', 'r_3_6', 'r_2_6', 'r_1_6', 'r_0_6',
            'observed','other',
            'm0goals', 'm1goal', 'm2goals', 'm3goals', 'm4goals', 'm5goals', 'm6goals', 'm7goals', 'm8goals','moregoals'])

    final_results.loc['Total'] = final_results.sum()

    final_results.to_excel(f'D:\Dropbox\La Cima del Éxito\Futbol\\articulos\matches_distribution_2013-2021_All_UEFA.xlsx',encoding='utf-8',index=True)
    