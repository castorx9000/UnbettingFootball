import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os 

path = 'D:\Dropbox\La Cima del Éxito\Futbol\Ligas_csv'
files = os.listdir(path)
input_df = pd.DataFrame()
output_df = pd.DataFrame()
seasons_list = ['2000-2001','2001-2002','2002-2003','2003-2004','2004-2005','2005-2006','2006-2007','2007-2008','2008-2009','2009-2010','2010-2011','2011-2012','2012-2013','2013-2014','2014-2015','2015-2016','2016-2017','2017-2018','2018-2019','2019-2020','2020-2021']
season_counter = 0
output_columns = ['Season','Div','Date','HomeTeam','AwayTeam','FTHG','FTAG','FTR','HTHG','HTAG','HTR','Referee','HS','AS','HST','AST','HF','AF','HY','AY','HR','AR','HO','AO','OddH','OddD','OddA','Over2.5','Under2.5']

excel_files = [f for f in files if f[-3:] == 'xls' or f[-3:] == 'lsx']

for file in excel_files:
    # opens in pandas the file 'file' from the list 'excel_files' as a ExcelFile
    data = pd.ExcelFile(f'D:\Dropbox\La Cima del Éxito\Futbol\Ligas_csv\{file}')

    # opens sheet by sheet of every excel file
    for sheet in data.sheet_names:
        # transforms every sheet into a data frame
        input_df = pd.read_excel(data,sheet)

        input_df['Season'] = seasons_list[season_counter] 

        # check if the league has B365 odds, if it's the case, the columns name are changed
        # to the standard OddH, OddD and OddA. If the league has no B365, check if it has GB
        # and, if it's the case, apply the same transformations
        if 'B365H' in input_df.columns:
            input_df = input_df.rename(columns={'B365H':'OddH','B365D':'OddD','B365A':'OddA'}) 
        elif 'GBH' in input_df.columns:
            input_df = input_df.rename(columns={'GBH':'OddH','GBD':'OddD','GBA':'OddA'})
        else:
            input_df['OddH'] = ''
            input_df['OddD'] = ''
            input_df['OddA'] = ''

        if 'Avg>2.5' in input_df.columns:
            input_df = input_df.rename(columns={'Avg>2.5':'Over2.5','Avg<2.5':'Under2.5'})
        elif 'GB>2.5' in input_df.columns:
            input_df = input_df.rename(columns={'GB>2.5':'Over2.5','GB<2.5':'Under2.5'})
        elif 'B365>2.5' in input_df.columns:
            input_df = input_df.rename(columns={'B365>2.5':'Over2.5','B365<2.5':'Under2.5'})
        else:
            input_df['Over2.5'] = ''
            input_df['Under2.5'] = ''
        
        # check if the sheet has the columns specified in var output_columns
        # if a column doesnt exist in the df, the column is added, but empty
        for column in output_columns:
            if column not in input_df.columns:
                input_df[column] = ''

        # stablish the final cut of input_df columns in order 
        input_df = input_df[output_columns]
 
        # appends the league season into the data frame of all seasons
        output_df = output_df.append(input_df)
    
    # increases the season counter
    season_counter += 1

    
output_df['Div'].replace('', np.nan, inplace=True)
output_df.dropna(subset=['Div'], inplace=True)

print(len(output_df.index))
output_df.to_csv('D:\Dropbox\La Cima del Éxito\Futbol\Ligas_csv\df_Leagues.csv',encoding='utf-8',index=False)