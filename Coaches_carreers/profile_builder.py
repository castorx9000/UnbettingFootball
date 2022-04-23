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
    
    for coach in coaches_list:

        coach_df = pd.read_excel(f'Coaches/{coach}')
        
        coach_df = add_reference_column(coach_df)
        coach_df = insert_escenarios(coach_df, metron)
        
        coach_df['Date'] = pd.to_datetime(coach_df['Date'])
        coach_df = coach_df.sort_values(by='Date')
        
        coach_df.to_excel(f'Coaches_xValues/{coach}')


if __name__ == '__main__':

    metron = pd.read_excel('metron.xlsx')

    coaches_list = coaches_list_creator()

    profile_builder(coaches_list, metron)