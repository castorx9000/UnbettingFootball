import pandas as pd
import numpy as np
import matplotlib as plt
import math

# coaches_df = pd.read_excel('coachs_profiles_19-03-2021.xlsx')
# coaches_df = coaches_df[['Name','Matches','Performance']]
# coaches_df = coaches_df.sort_values('Matches', ascending=False)
# index_max = coaches_df.loc[coaches_df['Matches'].idxmax()]
# coach = coaches_df.iloc[5]
# number_bins = index_max[1]//30

lista_DTs = ['Massimiliano Allegri','Zinedine Zidane','Jurguen Klopp','Thomas Tuchel','Diego Simeone','Jose Mourinho','Josep Guardiola','Gabriel Caballero', 'Alfonso Sosa', 'Rafael Puente Jr.', 'Paulo Pezzolano', 'Robert Dante Siboldi', 'Antonio Mohamed', 'Juan Reynoso', 'Miguel Gonzalez', 'Victor Manuel Vucetich', 'Guillermo Almada', 'Luis Fernando Tena', 'Ricardo Ferreti', 'Miguel Herrera', 'Gustavo Quinteros', 'Pablo Guede', 'Guillermo Vazquez', 'Jose Manuel de la Torre', 'Ignacio Ambriz', 'Omar Flores', 'Leandro Cufre', 'Jesus Rodriguez / Jose Maria Cruzalta', 'Martin Palermo', 'Oscar Pareja', 'Luis Garcia', 'Enrique Lopez Zarza', 'Gustavo Matosas', 'Diego Alonso', 'Tomas Boy', 'Pedro Caixinha', 'Enrique Meza', 'Esteve Padilla', 'Jose Luis Sanchez Sola', 'Javier Torrente', 'Jose Luis Gonzalez China', 'Francisco Palencia', 'Bruno Marioni', 'Ruben Duarte', 'Alberto Coyote', 'Salvador Reyes de la Pena', 'Jose Saturnino Cardozo', 'Angel Guillermo Hoyos', 'Jose Luis Real', 'Gaston Obledo', 'Roberto Hernandez', 'Hernan Cristante', 'David Patino', 'Pako Ayestaran', 'Franky Oviedo', 'Jorge Martinez Merino', 'Hugo Guillermo Chavez', 'Diego Cocca', 'Juvenal Olmos', 'Marcelo Michel Leano', 'Gustavo Diaz', 'Gerardo Espinoza', 'Matias Almeyda', 'Daniel Alcantar', 'Ruben Omar Romano', 'Jose Guadalupe Cruz', 'Francisco Jemez', 'Diego Torres', 'Jaime Lozano', 'Eduardo Coudet', 'Sergio Egea', 'Rafael Garcia Torres', 'Juan Antonio Luna', 'Ricardo Antonio La Volpe', 'Sergio Bueno', 'Carlos Reinoso', 'Pablo Marini', 'Ricardo Valino', 'Joaquin Moreno', 'Luis Zubeldia', 'Fernando Martinez Aldana y Marco Capetillo', 'Francisco Ramirez', 'Gustavo Costas', 'Luis Fernando Suarez', 'Juan Antonio Pizzi', 'Raul Chabrand', 'Hugo Norberto Castillo', 'Carlos Bustos', 'Daniel Guzman', 'Roberto Hernandez Ayala', 'Alfredo Tena', 'Carlos Barra', 'Cristobal Ortega', 'Ramon Morales', 'Cesar Farias', 'Angel David Comizzo', 'Jose Luis Trejo', 'Eduardo de la Torre Menchaca', 'Ruben Israel', 'Jose Luis Mata', 'Alvaro Galindo', 'Juan Carlos Ortega', 'Jorge Almiron', 'Omar Asad', 'Andres Carevic', 'Juan Antonio Torres Servin', 'Wilson Graniolatti', 'Benjamin Galindo', 'Manuel Lapuente', 'Antonio Torres Servin', 'Gerardo Silva', 'Carlos Maria Morales', 'Eduardo Fentanes', 'John Vant Schip', 'Alex Aguinaga', 'Hugo Sanchez', 'Mario Carrillo', 'Carlos de los Cobos', 'Joaquin del Olmo', 'Juan Carlos Chavez', 'Daniel Bartolotta', 'Efrain Flores', 'Hector Hugo Eugui', 'Manuel Martinez', 'Mario Alberto Garcia', 'Juan Carlos Osorio', 'Rene Isidoro Garcia', 'Fernando Quirarte', 'Gilberto Adame', 'Raul Arias', 'Eduardo Rergis', 'Jose Trevino / Hector Becerra', 'Octavio Becerril', 'Ignacio Sanchez Barrera', 'No definido', 'Omar Briseno', 'Jose Luis Salgado', 'Quique Septien', 'Andres Lillini', 'Nicolas Larcamon', 'Santiago Solari', 'Leonel Rocco']
#lista_DTs = ['Gabriel Caballero', 'Alfonso Sosa', 'Ricardo Ferreti']
matches = pd.read_excel('Matches_and_Coaches_2000_2021.xlsx')
matches = matches[['Season','Home','DT_Home','Away','DT_Away','FTHG','FTAG','FTR','HTH','HTA','HTR','SHH','SHA','SHR','B365H','B365D','B365A']]

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

metron = pd.read_excel('reference_system_means.xlsx')
metron = metron[['Escenario','FTHG','FTAG','HTHG','HTAG','HS','AS','HST','AST','HF','AF','HY','AY','HR','AR']]

escenario_list = [i for i  in metron['Escenario']]


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


def coach_profile(matches, metron, coach):

    performance = 0
    h_obPts, a_obPts, obPts = 0, 0, 0
    h_exPts, a_exPts, exPts = 0, 0, 0
    obPPM, exPPM = 0, 0
    h_obWins, a_obWins, obWins = 0, 0, 0
    h_obDraws, a_obDraws, obDraws = 0, 0, 0
    h_obLosses, a_obLosses, obLosses = 0, 0, 0
    h_exWins, a_exWins, exWins = 0, 0, 0
    h_exDraws, a_exDraws, exDraws = 0, 0, 0
    h_exLosses, a_exLosses, exLosses = 0, 0, 0
    winsP100, drawsP100, lossesP100 = 0, 0, 0
    h_winsP100, h_drawsP100, h_lossesP100 = 0, 0, 0
    a_winsP100, a_drawsP100, a_lossesP100 = 0, 0, 0
    h_obSG, a_obSG, obSG = 0, 0, 0
    h_obCG, a_obCG, obCG = 0, 0, 0
    h_exSG, a_exSG, exSG = 0, 0, 0
    h_exCG, a_exCG, exCG = 0, 0, 0
    SGP100, CGP100, h_SGP100, h_CGP100, a_SGP100, a_CGP100 = 0, 0, 0, 0, 0, 0
    h_played, a_played, played = 0, 0, 0

    escenario_list = [i for i  in metron['Escenario']]
    auxiliar = pd.DataFrame()

    results = []
    auxiliar = []

    for index, row in matches.iterrows():
    
        if math.isnan(row['ProbH']) or math.isnan(row['ProbD']) or math.isnan(row['ProbA']):
                continue
    
        if row['DT_Home'] == coach:
            
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
        
        if row['DT_Away'] == coach:
            
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
        
        if h_played + a_played == 30:
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
            except ZeroDivisionError:
                obPPM = 0
                exPPM = 0
            
            try: 
                performance = obPts / exPts
            except ZeroDivisionError:
                performance = 0

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

            auxiliar = [
                coach,played, h_played, a_played, performance,
                winsP100, drawsP100, lossesP100,
                h_winsP100, h_drawsP100, h_lossesP100,
                a_winsP100, a_drawsP100, a_lossesP100,
                obWins, exWins, obDraws, exDraws, obLosses, exLosses, 
                h_obWins, h_exWins, h_obDraws, h_exDraws, h_obLosses, h_exLosses,
                a_obWins, a_exWins, a_obDraws, a_exDraws, a_obLosses, a_exLosses,
                obPPM, exPPM, 
                obPts, exPts, h_obPts, h_exPts, a_obPts, a_exPts,
                obSG, obCG,
                exSG, exCG,
                h_obSG, h_obCG,
                h_exSG, h_exCG,
                a_obSG, a_obCG,
                a_exSG, a_exCG,
                SGP100, CGP100, h_SGP100, h_CGP100, a_SGP100, a_CGP100
                ]

            results.append(auxiliar)    

            performance = 0
            h_obPts, a_obPts, obPts = 0, 0, 0
            h_exPts, a_exPts, exPts = 0, 0, 0
            obPPM, exPPM = 0, 0                
            h_obWins, a_obWins, obWins = 0, 0, 0
            h_obDraws, a_obDraws, obDraws = 0, 0, 0
            h_obLosses, a_obLosses, obLosses = 0, 0, 0
            h_exWins, a_exWins, exWins = 0, 0, 0
            h_exDraws, a_exDraws, exDraws = 0, 0, 0
            h_exLosses, a_exLosses, exLosses = 0, 0, 0
            winsP100, drawsP100, lossesP100 = 0, 0, 0
            h_winsP100, h_drawsP100, h_lossesP100 = 0, 0, 0
            a_winsP100, a_drawsP100, a_lossesP100 = 0, 0, 0
            h_obSG, a_obSG, obSG = 0, 0, 0
            h_obCG, a_obCG, obCG = 0, 0, 0
            h_exSG, a_exSG, exSG = 0, 0, 0
            h_exCG, a_exCG, exCG = 0, 0, 0
            SGP100, CGP100, h_SGP100, h_CGP100, a_SGP100, a_CGP100 = 0, 0, 0, 0, 0, 0
            h_played, a_played, played = 0, 0, 0

    return results


def coachs_performances(matches, metron, coachs_list):
    coachs_performances = []
    # coachs_with_more_than_sixty_matches = []
    coaches_df = []

    for coach in coachs_list:
        if coach == 'No definido':
            continue
        # print(coach)
        coachs_performances.append(coach_profile(matches, metron, coach))

    for coach in coachs_performances:
        
        for coach_subset in coach:
            
            coaches_df.append(coach_subset)
        
        # if coach[1][] >= 60:
        #     coachs_with_more_than_sixty_matches.append(coach)

    # coachs_df = pd.DataFrame(coachs_with_more_than_sixty_matches, columns=['Name','Matches','H_Matches','A_Matches','Performance','Wins%','Draws%','Losses%','H_Wins%','H_Draws%','H_Losses%','A_Wins%','A_Draws%','A_Losses%','obWins','exWins','obDraws','exDraws','obLosses','exLosses','H_obWins','H_exWins','H_obDraws','H_exDraws','H_obLosses','H_exLosses','A_obWins','A_exWins','A_obDraws','A_exDraws','A_obLosses','A_exLosses','obPPM','exPPM','obPts','exPts','h_obPts','h_exPts','a_obPts','a_exPts','obSG','obCG','exSG','exCG','h_obSG','h_obCG','h_exSG','h_exCG','a_obSG','a_obCG','a_exSG','a_exCG','SG%','CG%','h_SG%','h_CG%','a_SG%','a_CG%'])
    coaches_df = pd.DataFrame(coaches_df, columns=['Name','Matches','H_Matches','A_Matches','Performance','Wins%','Draws%','Losses%','H_Wins%','H_Draws%','H_Losses%','A_Wins%','A_Draws%','A_Losses%','obWins','exWins','obDraws','exDraws','obLosses','exLosses','H_obWins','H_exWins','H_obDraws','H_exDraws','H_obLosses','H_exLosses','A_obWins','A_exWins','A_obDraws','A_exDraws','A_obLosses','A_exLosses','obPPM','exPPM','obPts','exPts','h_obPts','h_exPts','a_obPts','a_exPts','obSG','obCG','exSG','exCG','h_obSG','h_obCG','h_exSG','h_exCG','a_obSG','a_obCG','a_exSG','a_exCG','SG%','CG%','h_SG%','h_CG%','a_SG%','a_CG%'])
    
    return coaches_df


if __name__ == "__main__":

    performances = coachs_performances(matches, metron, lista_DTs)
    print(performances)
    performances.to_excel('coachs_profiles_per_60_matches_19-07-2021.xlsx',sheet_name='profiles')
    
    #print(coaches_df.iloc[20])
    #print(coach)
    #print(index_max)
    #print(index_max[1])
    #print(number_bins)
    #print(matches_df)