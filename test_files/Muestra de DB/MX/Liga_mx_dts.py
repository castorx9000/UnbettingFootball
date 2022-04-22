import pandas as pd 
import numpy as np 
from matplotlib import pyplot as plt
import math

TOTAL_PARTIDOS = 3083
lista_DTs = ['Gabriel Caballero', 'Alfonso Sosa', 'Rafael Puente Jr.', 'Paulo Pezzolano', 'Robert Dante Siboldi', 'Antonio Mohamed', 'Juan Reynoso', 'Miguel Gonzalez', 'Victor Manuel Vucetich', 'Guillermo Almada', 'Luis Fernando Tena', 'Ricardo Ferreti', 'Miguel Herrera', 'Gustavo Quinteros', 'Pablo Guede', 'Guillermo Vazquez', 'Jose Manuel de la Torre', 'Ignacio Ambriz', 'Omar Flores', 'Leandro Cufre', 'Jesus Rodriguez / Jose Maria Cruzalta', 'Martin Palermo', 'Oscar Pareja', 'Luis Garcia', 'Enrique Lopez Zarza', 'Gustavo Matosas', 'Diego Alonso', 'Tomas Boy', 'Pedro Caixinha', 'Enrique Meza', 'Esteve Padilla', 'Jose Luis Sanchez Sola', 'Javier Torrente', 'Jose Luis Gonzalez China', 'Francisco Palencia', 'Bruno Marioni', 'Ruben Duarte', 'Alberto Coyote', 'Salvador Reyes de la Pena', 'Jose Saturnino Cardozo', 'Angel Guillermo Hoyos', 'Jose Luis Real', 'Gaston Obledo', 'Roberto Hernandez', 'Hernan Cristante', 'David Patino', 'Pako Ayestaran', 'Franky Oviedo', 'Jorge Martinez Merino', 'Hugo Guillermo Chavez', 'Diego Cocca', 'Juvenal Olmos', 'Marcelo Michel Leano', 'Gustavo Diaz', 'Gerardo Espinoza', 'Matias Almeyda', 'Daniel Alcantar', 'Ruben Omar Romano', 'Jose Guadalupe Cruz', 'Francisco Jemez', 'Diego Torres', 'Jaime Lozano', 'Eduardo Coudet', 'Sergio Egea', 'Rafael Garcia Torres', 'Juan Antonio Luna', 'Ricardo Antonio La Volpe', 'Sergio Bueno', 'Carlos Reinoso', 'Pablo Marini', 'Ricardo Valino', 'Joaquin Moreno', 'Luis Zubeldia', 'Fernando Martinez Aldana y Marco Capetillo', 'Francisco Ramirez', 'Gustavo Costas', 'Luis Fernando Suarez', 'Juan Antonio Pizzi', 'Raul Chabrand', 'Hugo Norberto Castillo', 'Carlos Bustos', 'Daniel Guzman', 'Roberto Hernandez Ayala', 'Alfredo Tena', 'Carlos Barra', 'Cristobal Ortega', 'Ramon Morales', 'Cesar Farias', 'Angel David Comizzo', 'Jose Luis Trejo', 'Eduardo de la Torre Menchaca', 'Ruben Israel', 'Jose Luis Mata', 'Alvaro Galindo', 'Juan Carlos Ortega', 'Jorge Almiron', 'Omar Asad', 'Andres Carevic', 'Juan Antonio Torres Servin', 'Wilson Graniolatti', 'Benjamin Galindo', 'Manuel Lapuente', 'Antonio Torres Servin', 'Gerardo Silva', 'Carlos Maria Morales', 'Eduardo Fentanes', 'John Vant Schip', 'Alex Aguinaga', 'Hugo Sanchez', 'Mario Carrillo', 'Carlos de los Cobos', 'Joaquin del Olmo', 'Juan Carlos Chavez', 'Daniel Bartolotta', 'Efrain Flores', 'Hector Hugo Eugui', 'Manuel Martinez', 'Mario Alberto Garcia', 'Juan Carlos Osorio', 'Rene Isidoro Garcia', 'Fernando Quirarte', 'Gilberto Adame', 'Raul Arias', 'Eduardo Rergis', 'Jose Trevino / Hector Becerra', 'Octavio Becerril', 'Ignacio Sanchez Barrera', 'No definido', 'Omar Briseno', 'Jose Luis Salgado']

data_frame = pd.read_excel('Muestra_de_DB\MX\LigaMX_2011_2020.xlsx')
data_frame = data_frame[['Season','Home','DT_Home','Away','DT_Away','FTHG','FTAG','FTR','HTH','HTA','HTR','SHH','SHA','SHR','B365H','B365D','B365A']]

def change_odds_to_implied_probabilities(matches):

    for index, row in data_frame.iterrows():
        
        matches['B365H'] = matches['B365H'].replace(row['B365H'], 1 / row['B365H'])
        matches['B365D'] = matches['B365D'].replace(row['B365D'], 1 / row['B365D'])
        matches['B365A'] = matches['B365A'].replace(row['B365A'], 1 / row['B365A'])
    
    return matches
    

def points_obtained_and_expected_per_coach(data_frame, coach):

    home_obtained_points = 0
    away_obtained_points = 0
    total_obtained_points = 0
    performance = 0

    home_expected_points = 0
    away_expected_points = 0
    total_expected_points = 0

    points_per_match = 0
    expected_points_per_match = 0

    home_expected_wins = 0
    home_expected_draws = 0
    home_expected_losses = 0

    away_expected_wins = 0
    away_expected_draws = 0
    away_expected_losses = 0

    home_obtained_wins = 0
    home_obtained_draws = 0
    home_obtained_losses = 0

    away_obtained_wins = 0
    away_obtained_draws = 0
    away_obtained_losses = 0

    total_expected_wins = 0
    total_expected_draws = 0
    total_expected_losses = 0

    total_obtained_wins = 0
    total_obtained_draws = 0
    total_obtained_losses = 0

    home_goals_scored = 0
    home_goals_conceded = 0
    away_goals_scored = 0
    away_goals_conceded = 0
    total_goals_scored = 0
    total_goals_conceded = 0

    total_expected_played = 0

    home_played = 0
    away_played = 0
    total_played = 0

    results = []

    for index, row in data_frame.iterrows():

        if row['DT_Home'] == coach:

            if math.isnan(row['B365H']) or math.isnan(row['B365D']) or math.isnan(row['B365A']):
                continue

            home_expected_points = home_expected_points + 3 * (row['B365H'] - 0.037) + 1 * (row['B365D'] -0.037)
            home_expected_wins = home_expected_wins + row['B365H'] -0.037
            home_expected_draws = home_expected_draws + row['B365D'] -0.037
            home_expected_losses = home_expected_losses + row['B365A'] -0.037
            
            home_goals_scored += row['FTHG']
            home_goals_conceded += row['FTAG']

            home_played += 1
            
            if row['FTR'] == 'H':
                home_obtained_points += 3
                home_obtained_wins += 1
            if row['FTR'] == 'D':
                home_obtained_points += 1
                home_obtained_draws += 1
            if row['FTR'] == 'A':
                home_obtained_losses += 1
  
        if row['DT_Away'] == coach:

            if math.isnan(row['B365H']) or math.isnan(row['B365D']) or math.isnan(row['B365A']):
                continue

            away_expected_points = away_expected_points + 3 * (row['B365A'] -0.037) + 1 * (row['B365D'] -0.037)
            away_expected_wins = away_expected_wins + row['B365A'] -0.037
            away_expected_draws = away_expected_draws + row['B365D'] -0.037
            away_expected_losses = away_expected_losses + row['B365H'] -0.037

            away_goals_scored += row['FTAG']
            away_goals_conceded += row['FTHG']       

            away_played += 1
            if row['FTR'] == 'A':
                away_obtained_points += 3
                away_obtained_wins += 1
            if row['FTR'] == 'D':
                away_obtained_points += 1
                away_obtained_draws += 1
            if row['FTR'] == 'H':
                away_obtained_losses += 1

        total_obtained_points = home_obtained_points + away_obtained_points
        total_expected_points = home_expected_points + away_expected_points

        total_obtained_wins = home_obtained_wins + away_obtained_wins
        total_expected_wins = home_expected_wins + away_expected_wins
        
        total_obtained_draws = home_obtained_draws + away_obtained_draws
        total_expected_draws = home_expected_draws + away_expected_draws
        
        total_obtained_losses = home_obtained_losses + away_obtained_losses
        total_expected_losses = home_expected_losses + away_expected_losses

        #home_goals_difference = home_goals_scored - home_goals_conceded
        #away_goals_difference = away_goals_scored - away_goals_conceded

        #home_goals_scored_per_match = round(home_goals_scored/home_played,1)
        #home_goals_conceded_per_match = round(home_goals_conceded/home_played,1)

        #away_goals_scored_per_match = round(away_goals_scored/away_played,1)
        #away_goals_conceded_per_match = round(away_goals_conceded/away_played,1)

        #home_goals_difference_per_match = 
        #away_goals_difference_per_match =

        total_goals_scored = home_goals_scored + away_goals_scored
        total_goals_conceded = home_goals_conceded + away_goals_conceded
              
        total_expected_played = total_expected_wins + total_expected_draws + total_expected_losses
        total_played = home_played + away_played
        try:
            points_per_match = round(total_obtained_points / total_played,2)
            expected_points_per_match = round(total_expected_points / total_expected_played,2)
        except ZeroDivisionError:
            points_per_match = 0
            expected_points_per_match = 0

        try:
            performance = round((points_per_match/expected_points_per_match) * 100, 2)
        except ZeroDivisionError:
            performance = 0

    results = [coach, performance, points_per_match, expected_points_per_match, total_obtained_points, round(total_expected_points,1), total_played, round(total_obtained_wins/total_played *100,1), round(total_obtained_draws/total_played *100,1), round(total_obtained_losses/total_played *100,1), round(total_expected_wins/total_expected_played *100,1), round(total_expected_draws/total_expected_played *100,1), round(total_expected_losses/total_expected_played *100,1), total_obtained_wins, total_obtained_draws, total_obtained_losses, round(total_expected_wins,1), round(total_expected_draws,1), round(total_expected_losses,1),total_goals_scored,total_goals_conceded,home_goals_scored,home_goals_conceded,away_goals_scored,away_goals_conceded]

    return results
    

def coach_performance(data_frame, coaches_list):

    coaches_performances = []
    coaches_with_more_than_thirty_matches = []

    for coach in coaches_list:

        if coach == 'No definido':
            continue

        coaches_performances.append(points_obtained_and_expected_per_coach(data_frame, coach))

    for coach in coaches_performances:
        if coach[6] >= 60:
            coaches_with_more_than_thirty_matches.append(coach)


    return coaches_with_more_than_thirty_matches
        

data_frame = change_odds_to_implied_probabilities(data_frame)
performances = coach_performance(data_frame, lista_DTs)
print(f'El total de DTs: {len(lista_DTs)}')
print(f'El total de Dts con 60 o más partidos dirigidos es: {len(performances)} o {round(len(performances)/len(lista_DTs),1)*100} % del total')

# Creating the pandas data frame
coaches_data_frame = pd.DataFrame(performances, columns = ['Name','Performance','obPPM', 'exPPM','obPts','exPts','matches','obWins%','obDraws%','obLosses%','exWins%','exDraws%','exLosses%','obWins','obDraws','obLosses','exWins','exDraws','exLosses','TGS','TGC','HGS','HGC','AGS','AGC'])
print(coaches_data_frame)
coaches_data_frame.to_excel('coaches_performances_v3.xlsx',sheet_name='performances')
#plt.scatter(coaches_data_frame['obPPM'],coaches_data_frame['exPPM'])