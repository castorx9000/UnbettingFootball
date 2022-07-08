from os import remove
import numpy as np
import pandas as pd


def remove_matches_without_referees(df_matches):

    print(df_matches)
    df_matches['Referee'].dropna()
    print(df_matches)



if __name__ == "__main__":

    df_matches = pd.read_csv('D:\Dropbox\La Cima del Éxito\Futbol\Ligas_csv\df_Leagues.csv')
    seasons_list = ['2000-2001','2001-2002','2002-2003','2003-2004','2004-2005','2005-2006','2006-2007','2007-2008','2008-2009','2009-2010','2010-2011','2011-2012','2012-2013','2013-2014','2014-2015','2015-2016','2016-2017','2017-2018','2018-2019','2019-2020','2020-2021']
    
    remove_matches_without_referees(df_matches)
