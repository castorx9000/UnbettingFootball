import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
from itertools import product
from pandas.core.indexes.base import Index

def create_matches_df(clubs_list,matches):
    
    match = []
    cartesian_product = []
    i = 0
    total_clubs = len(clubs_list)
    matches_local = pd.DataFrame()
    matches_champions = matches[matches['FIFA ID'] == 'EU CL']

    for club in clubs_list:
        
        if i == total_clubs -1:
            break

        cartesian_product = list(product([clubs_list[i]], clubs_list[i+1:]))

        for element in cartesian_product:

            probH = 0
            probD = 0
            probA = 0

            # Check if both teams are in the same national league
            if element[0][1] == element[1][1]:
                
                matches_local = matches[matches['FIFA ID'] == element[0][1]]                
                matches_local = matches_local[matches_local['Home'] == element[0][0]]

                probH = matches_local.loc[matches_local['Away'] == element[1][0], 'ProbH'].values[0]
                probD = matches_local.loc[matches_local['Away'] == element[1][0], 'ProbD'].values[0]
                probA = matches_local.loc[matches_local['Away'] == element[1][0], 'ProbA'].values[0]
                
                match.append([element[0][0],element[0][2],element[1][0],element[1][2],probH,probD,probA])

                matches_local = matches[matches['FIFA ID'] == element[0][1]]
                matches_local = matches_local[matches_local['Away'] == element[0][0]]

                probH = matches_local.loc[matches_local['Home'] == element[1][0], 'ProbH'].values[0]
                probD = matches_local.loc[matches_local['Home'] == element[1][0], 'ProbD'].values[0]
                probA = matches_local.loc[matches_local['Home'] == element[1][0], 'ProbA'].values[0]
                
                match.append([element[1][0],element[1][2],element[0][0],element[0][2],probH,probD,probA])
            
            # Check if both teams participated in the Champions League
            elif (element[0][0] in matches_champions.values) and (element[1][0] in matches_champions.values):

                matches_local = matches_champions[matches_champions['Home'] == element[0][0]]
                matches_local2 = matches_champions[matches_champions['Away'] == element[0][0]]
                
                # OJO --> ¿Qué pasaría si se enfrentasen 2 veces en la champions? OMG
                # Check if both teams faced each other in CL
                if element[1][0] in matches_local.values:

                    print(element[1][0], element[0][0])

                    probH = matches_local.loc[matches_local['Home'] == element[0][0], 'ProbH'].values[0]
                    probD = matches_local.loc[matches_local['Home'] == element[0][0], 'ProbD'].values[0]
                    probA = matches_local.loc[matches_local['Home'] == element[0][0], 'ProbA'].values[0]

                    match.append([element[0][0],element[0][2],element[1][0], element[1][2],probH, probD, probA])

                    probH = matches_local2.loc[matches_local2['Home'] == element[1][0], 'ProbH'].values[0]
                    probD = matches_local2.loc[matches_local2['Home'] == element[1][0], 'ProbD'].values[0]
                    probA = matches_local2.loc[matches_local2['Home'] == element[1][0], 'ProbA'].values[0]

                    match.append([element[1][0],element[1][2],element[0][0], element[0][2],probH, probD, probA])

                else:
                    # This applies for cases of matches with no common matches in CL nor National league
                    #print(element[0][0],element[0][1],element[0][2],element[1][0],element[1][1],element[1][2])
                    
                    probH, probD, probA = triangling(element[0][0],element[0][1],element[0][2],element[1][0],element[1][1],element[1][2],matches)
                    match.append([element[0][0],element[0][2],element[1][0],element[1][2],probH,probD,probA])
                    probH, probD, probA = triangling(element[1][0],element[1][1],element[1][2],element[0][0],element[0][1],element[0][2],matches)
                    match.append([element[1][0],element[1][2],element[0][0],element[0][2],probH,probD,probA])

            else:
                # This applies when teams have no common matches in CL nor National League
                match.append([element[0][0],element[0][2],element[1][0],element[1][2],probH,probD,probA])
                match.append([element[1][0],element[1][2],element[0][0],element[0][2],probH,probD,probA])
        
        i+=1
    
    matches_new_league = pd.DataFrame(match, columns=['Home','Home Country','Away','Away Country','ProbH','ProbD','ProbA'])
    
    return matches_new_league


# This function implies club_H and club_A have no commmon matches in european nor domestic competitions
def triangling(club_H, club_H_league, club_H_nation, club_A, club_A_league, club_A_nation, matches):

    # Matches DF national league of club_H (home club) and club_A (away club)
    matches_club_H_national_league = matches[matches['FIFA ID'] == club_H_league]
    matches_club_A_national_league = matches[matches['FIFA ID'] == club_A_league]

    # Matches DF all UCL matches
    matches_champions = matches[matches['FIFA ID'] == 'EU CL']
    
    # Matches DF all UEL matches
    matches_europa_league = matches[matches['FIFA ID'] == 'EU EUL']
    
    # Matches DF international matches of club_a (away club)
    matches_club_A_international = matches[ np.logical_and( np.logical_or( matches['Away'] == club_A, matches['Home'] == club_A ), matches['FIFA ID'] != club_A_league,) ]
    matches_club_H_international = matches[ np.logical_and( np.logical_or( matches['Away'] == club_H, matches['Home'] == club_H ), matches['FIFA ID'] != club_H_league,) ]

    #print(matches_club_A_international)
    #print(matches_club_H_international)
    probH = 1
    probD = 1
    probA = 1
    
    # Check if the club_A (away club) faced a club from the same national league of club_H (home club) within international matches
    if club_H_nation in matches_club_A_international.values:
        
        # DF including matches ONLY between club_A and teams from club_H's nation
        matches_club_A_vs_club_H_nation = matches_club_A_international[matches_club_A_international['Home Country'] == club_H_nation]
        
        for index, row in matches_club_A_vs_club_H_nation.iterrows():
            
            index_H = row['Index H']
            index_A = row['Index A']
            
            # DF including club_H national league matches where the away club odds match +/- 0.05 the odds of club_A
            # in this point we are looking for a club_H national league equivalent club (regarding club_A)
            matches_club_H_vs_national_league_similar_rivals = matches_club_H_national_league[ np.logical_and(matches_club_H_national_league['Index A'] <= index_A + 0.02, matches_club_H_national_league['Index A'] >= index_A - 0.02) ]
            
            #print(club_H,index_H,club_A,index_A)
            #print(matches_club_H_vs_national_league_similar_rivals)
            
            # Here we look if there is a national league match for club_H where the odds distribution of the match are the same
            # as the international match against club_A
            if club_H in matches_club_H_vs_national_league_similar_rivals['Home'].values:

                #print(club_H, 'is in', '\n')
            
                probH = matches_club_H_vs_national_league_similar_rivals['ProbH'].mean()
                probD = matches_club_H_vs_national_league_similar_rivals['ProbD'].mean()
                probA = matches_club_H_vs_national_league_similar_rivals['ProbA'].mean()
            
                return probH, probD, probA
            else:
                print(club_H, 'not in', '\n')

    # Check if the club_H (home club) faced a club from the same national league of club_A (away club) within international matches
    if club_A_nation in matches_club_H_international.values:
        
        # DF including matches ONLY between club_H and teams from club_A's nation
        matches_club_H_vs_club_A_nation = matches_club_H_international[matches_club_H_international['Away Country'] == club_A_nation]
        
        for index, row in matches_club_H_vs_club_A_nation.iterrows():
            
            index_H = row['Index H']
            index_A = row['Index A']
            
            # DF including club_A national league matches where the home club odds match +/- 0.05 the odds of club_H
            # we are looking for a club_A national league equivalent club (regarding club_H)
            matches_club_A_vs_national_league_similar_rivals = matches_club_A_national_league[ np.logical_and(matches_club_A_national_league['Index H'] <= index_H + 0.02, matches_club_A_national_league['Index H'] >= index_H - 0.02) ]
            
            #print(club_H,index_H,club_A,index_A)
            #print(matches_club_A_vs_national_league_similar_rivals)
            
            # Here we look if there is a national league match for club_H where the odds distribution of the match are the same
            # similar to the international match against club_A
            if club_A in matches_club_A_vs_national_league_similar_rivals['Away'].values:

                #print(club_A, 'is in', '\n')
            
                probH = matches_club_A_vs_national_league_similar_rivals['ProbH'].mean()
                probD = matches_club_A_vs_national_league_similar_rivals['ProbD'].mean()
                probA = matches_club_A_vs_national_league_similar_rivals['ProbA'].mean()
            
                return probH, probD, probA
            else:
                print(club_A, 'not in', '\n')

    return probH, probD, probA
            

if __name__ == "__main__":
    
    # Open Excel file as Dataframe
    matches = pd.read_excel('D:\Dropbox\La Cima del Éxito\Futbol\Triangling\Matches_2018-2019.xlsx', engine='openpyxl')
    
    # Remove rows with empty cels from Dataframe
    matches = matches.dropna()
    
    # Add indexes to search in metron
    matches['Index H'] = round(matches['ProbH'],2)
    matches['Index A'] = round(matches['ProbA'],2)
    
    # Set the order of columns in Dataframe
    matches = matches[['Date','FIFA ID','Home','Home Country','Away','Away Country','Index H','Index A','ProbH','ProbD','ProbA']]
    
    # List of leagues involved in calculations
    list_of_leagues_FIFA_ID = ['ESP D1','ENG PL','GER D1','FRA D1','ITA D1']
    
    # List of clubs involved in calculations as examples
    list_of_clubs = [['Liverpool','ENG PL','England'],['Manchester City','ENG PL','England'],['Manchester Utd','ENG PL','England'],['Barcelona','ESP D1','Spain'],['Atl. Madrid','ESP D1','Spain']]
    list_of_clubs_2 = [['Liverpool','ENG PL','England'],['Manchester City','ENG PL','England'],['Manchester Utd','ENG PL','England'],['Barcelona','ESP D1','Spain'],['Atl. Madrid','ESP D1','Spain'],['Tottenham','ENG PL','England'],['Dortmund','GER D1','Germany']]

    #new_league_matches = create_matches_df(list_of_clubs_2,matches)
    #print(new_league_matches)
    print(triangling('Liverpool','ENG PL','England','Dortmund','GER D1','Germany',matches))

    #print(matches)

    #create_season(list_of_clubs, matches)


    #index_h = 0
    #index_a = 0
    #matches_auxiliar = pd.DataFrame()

    #matches_auxiliar = matches[matches['FIFA ID'] == list_of_leagues_FIFA_ID[0]]
    #matches_auxiliar = matches_auxiliar[(matches_auxiliar['Index H'] >= 0.37) & (matches_auxiliar['Index H'] <= 0.4)]

    
    #print(matches_auxiliar)
    #print(matches_auxiliar['ProbH'].mean(), matches_auxiliar['ProbD'].mean(), matches_auxiliar['ProbA'].mean())
    #print(matches_auxiliar['ProbH'].std(),matches_auxiliar['ProbD'].std(),matches_auxiliar['ProbA'].std())
    #print(len(matches_auxiliar.index))