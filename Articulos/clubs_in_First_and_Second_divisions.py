import numpy as np
import pandas as pd


def remove_clubs_played_in_only_one_division(list_of_clubs):

    clubs_played_in_fist_and_second_divisions = [club for club in list_of_clubs if list_of_clubs.count(club) > 1]
    clubs_played_in_fist_and_second_divisions = list(set(clubs_played_in_fist_and_second_divisions))

    return clubs_played_in_fist_and_second_divisions


def cut_df_remove_clubs_played_in_only_one_division(clubs_dataframe, clubs_played_in_first_and_second_divisions):

    clubs_df_played_in_first_and_second_divisions = pd.DataFrame()

    for club in clubs_played_in_first_and_second_divisions:

        clubs_df_played_in_first_and_second_divisions = clubs_df_played_in_first_and_second_divisions.append(clubs_dataframe[clubs_dataframe['Club'] == club])

    return clubs_df_played_in_first_and_second_divisions


if __name__ == '__main__':

    clubs_leagues = pd.read_excel('D:\Dropbox\La Cima del Éxito\Futbol\\articulos\First_Second_Divisions.xlsx')
    clubs_list = clubs_leagues['Club'].tolist()

    clubs_played_in_first_and_second_divisions = remove_clubs_played_in_only_one_division(clubs_list)

    clubs_leagues = cut_df_remove_clubs_played_in_only_one_division(clubs_leagues, clubs_played_in_first_and_second_divisions)

    clubs_leagues.to_excel(f'D:\Dropbox\La Cima del Éxito\Futbol\\articulos\clubs_in_First_and_Second_divisions.xlsx',encoding='utf-8',index=True)