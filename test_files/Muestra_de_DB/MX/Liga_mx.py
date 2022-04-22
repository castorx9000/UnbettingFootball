import pandas as pd
import numpy as np
import matplotlib as plt

#excel_file_1 = 'Muestra de DB\MX\LigaMX_2011_2020.xlsx'
TOTAL_PARTIDOS = 2910
lista_DTs = ['Gabriel Caballero', 'Alfonso Sosa', 'Rafael Puente Jr.', 'Paulo Pezzolano', 'Robert Dante Siboldi', 'Antonio Mohamed', 'Juan Reynoso', 'Miguel Gonzalez', 'Victor Manuel Vucetich', 'Guillermo Almada', 'Luis Fernando Tena', 'Ricardo Ferreti', 'Miguel Herrera', 'Gustavo Quinteros', 'Pablo Guede', 'Guillermo Vazquez', 'Jose Manuel de la Torre', 'Ignacio Ambriz', 'Omar Flores', 'Leandro Cufre', 'Jesus Rodriguez / Jose Maria Cruzalta', 'Martin Palermo', 'Oscar Pareja', 'Luis Garcia', 'Enrique Lopez Zarza', 'Ricardo La Volpe', 'Gustavo Matosas', 'Diego Alonso', 'Tomas Boy', 'Pedro Caixinha', 'Enrique Meza', 'Esteve Padilla', 'Jose Luis Sanchez Sola', 'Javier Torrente', 'Jose Luis Gonzalez China', 'Francisco Palencia', 'Bruno Marioni', 'Ruben Duarte', 'Alberto Coyote', 'Salvador Reyes de la Pena', 'Jose Saturnino Cardozo', 'Angel Guillermo Hoyos', 'Jose Luis Real', 'Gaston Obledo', 'Roberto Hernandez', 'Hernan Cristante', 'David Patino', 'Pako Ayestaran', 'Franky Oviedo', 'Jorge Martinez Merino', 'Hugo Guillermo Chavez', 'Diego Cocca', 'Juvenal Olmos', 'Marcelo Michel Leano', 'Gustavo Diaz', 'Gerardo Espinoza', 'Matias Almeyda', 'Daniel Alcantar', 'Ruben Omar Romano', 'Jose Guadalupe Cruz', 'Francisco Jemez', 'Diego Torres', 'Jaime Lozano', 'Eduardo Coudet', 'Sergio Egea', 'Rafael Garcia Torres', 'Juan Antonio Luna', 'Ricardo Antonio La Volpe', 'Sergio Bueno', 'Carlos Reinoso', 'Pablo Marini', 'Ricardo Valino', 'Joaquin Moreno', 'Luis Zubeldia', 'Fernando Martinez Aldana y Marco Capetillo', 'Francisco Ramirez', 'Gustavo Costas', 'Luis Fernando Suarez', 'Juan Antonio Pizzi', 'Raul Chabrand', 'Hugo Norberto Castillo', 'Carlos Bustos', 'Daniel Guzman', 'Roberto Hernandez Ayala', 'Alfredo Tena', 'Carlos Barra', 'Cristobal Ortega', 'Ramon Morales', 'Cesar Farias', 'Angel David Comizzo', 'Jose Luis Trejo', 'Eduardo de la Torre Menchaca', 'Ruben Israel', 'Jose Luis Mata', 'Alvaro Galindo', 'Juan Carlos Ortega', 'Jorge Almiron', 'Omar Asad', 'Andres Carevic', 'Juan Antonio Torres Servin', 'Wilson Graniolatti', 'Benjamin Galindo', 'Manuel Lapuente', 'Antonio Torres Servin', 'Gerardo Silva', 'Carlos Maria Morales', 'Eduardo Fentanes', 'John Vant Schip', 'Alex Aguinaga', 'Hugo Sanchez', 'Mario Carrillo', 'Carlos de los Cobos', 'Joaquin del Olmo', 'Juan Carlos Chavez', 'Daniel Bartolotta', 'Efrain Flores', 'Hector Hugo Eugui', 'Manuel Martinez', 'Mario Alberto Garcia', 'Juan Carlos Osorio', 'Rene Isidoro Garcia', 'Fernando Quirarte', 'Gilberto Adame', 'Raul Arias', 'Eduardo Rergis', 'Jose Trevino / Hector Becerra', 'Octavio Becerril', 'Ignacio Sanchez Barrera', 'No definido', 'Omar Briseno', 'Jose Luis Salgado']

#df = pd.read_excel(excel_file_1)
df2 = pd.read_excel('Muestra de DB\MX\LigaMX_2011_2020.xlsx')

print(df2.columns)
#print(df.DT_Home)

def coaches(matches):

    DTs_Home = matches['DT_Home']
    DTs_Away = matches['DT_Away']

    DTs_list = []

    for DT in DTs_Home:
        if DT not in DTs_list:
            DTs_list.append(DT)

    for DT in DTs_Away:
        if DT not in DTs_list:
            DTs_list.append(DT)

    return DTs_list

lista_DTs_MX = coaches(df2)
total_DTs_MX = len(lista_DTs_MX)
#print(lista_DTs_MX)

print(f'Entre 2011 y 2020 en México {total_DTs_MX} Directores Técnicos han dirigido {TOTAL_PARTIDOS} partidos.')
print(f'El promedio de partidos dirigidos es: {round(TOTAL_PARTIDOS/total_DTs_MX,1)} por DT.')

def count_matches_per_coach(matches, coach_name):
    count = 0

    for index, row in df.iterrows():

        if row['DT_Home'] == coach_name:
            count+=1
        if row['DT_Away'] == coach_name:
            count+=1

    return(count)

#print(count_matches_per_coach(df,'Ricardo Ferreti'))
#print(count_matches_per_coach(df,'Jose Luis Sanchez Sola'))