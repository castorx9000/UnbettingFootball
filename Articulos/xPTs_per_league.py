import numpy as np
import pandas as pd


if __name__ == '__main__':

    matches = pd.read_excel('2012-2021_UEFA.xlsx')
    matches['xPPM'] = ''
    matches.xPPM = (matches.xWins * 3 + matches.xDraws) / matches.Matches
    matches.sort_values(by=['xPPM'], ascending=False, inplace=True)

    a = len(matches)
    b = len(matches[matches['xPPM'] >= 2.0])
    c = len(matches[(matches.xPPM < 2) & (matches.xPPM >= 1.5)])
    d = len(matches[(matches.xPPM < 1.5) & (matches.xPPM >= 1)])
    e = len(matches[(matches.xPPM < 1)])

    print(a, b, c, d, e, b+c+d+e)