from nis import match
import numpy as np
import pandas as pd


def club_performance(matches,club):
    
    Points = 0
    xPoints = 0
    results = []

    matches_club = matches[ matches['HomeTeam'] == club ]
    
    Points += matches_club['PtsH'].sum()
    xPoints += matches_club['xPtsH'].sum()

    matches_club = matches[ matches['AwayTeam'] == club ]

    Points += matches_club['PtsA'].sum()
    xPoints += matches_club['xPtsA'].sum()

    Performance_Points = Points / xPoints

    #print(club, Points, xPoints, Performance_Points)

    results = [club, Points, xPoints, Performance_Points]

    return results


if __name__ == '__main__':

    matches = pd.read_excel('EPL_2015-2016.xlsx')
    teams_list = matches['HomeTeam'].tolist()
    teams_list = list(set(teams_list))
    league_results = []

    for team in teams_list:

        league_results.append(club_performance(matches, team))

    
    df_league_results = pd.DataFrame(league_results, columns=['Club', 'Points', 'xPoints', 'Performance'])
    print(df_league_results)
    df_league_results.to_excel(f'Leicester_2015-16.xlsx')