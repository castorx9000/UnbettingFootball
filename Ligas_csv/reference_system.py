import pandas as pd
import numpy as np
import matplotlib as plt

matches_df = pd.read_csv('D:\Dropbox\La Cima del Éxito\Futbol\Ligas_csv\df_Euro_Leagues.csv',encoding='iso-8859-15')

# Removes empty rows and rows with Odds = 0 from data frame
matches_df['OddH'].replace('', np.nan, inplace=True)
matches_df.dropna(subset=['OddH'], inplace=True)
matches_df['OddD'].replace('', np.nan, inplace=True)
matches_df.dropna(subset=['OddD'], inplace=True)
matches_df['OddA'].replace('', np.nan, inplace=True)
matches_df.dropna(subset=['OddA'], inplace=True)
matches_df['OddH'].replace(0, np.nan, inplace=True)
matches_df.dropna(subset=['OddH'], inplace=True)
matches_df['OddD'].replace(0, np.nan, inplace=True)
matches_df.dropna(subset=['OddD'], inplace=True)
matches_df['OddA'].replace(0, np.nan, inplace=True)
matches_df.dropna(subset=['OddA'], inplace=True)

# Initiates the new columns for probabilities and margin
matches_df['ProbH'] = ''
matches_df['ProbD'] = ''
matches_df['ProbA'] = ''
matches_df['margin'] = ''

# Calculates margins and Implicit Probabilities
matches_df.margin = ( (1/matches_df.OddH) + (1/matches_df.OddD) + (1/matches_df.OddA) - 1 ) / 3
matches_df.ProbH = (1/matches_df.OddH) - matches_df.margin
matches_df.ProbD = (1/matches_df.OddD) - matches_df.margin
matches_df.ProbA = (1/matches_df.OddA) - matches_df.margin


def reference_frame(matches,start,end,step):
    
    index = start
    metron = pd.DataFrame()
    columns = [f'[1.00,{start}] AVG',f'[1.00,{start}] STD',f'[1.00,{start}] OCR']
    
    mean = pd.DataFrame()
    mean = matches[matches.ProbH >= start].mean()
    std_dev = pd.DataFrame()
    std_dev =matches[matches.ProbH >= start].std()
    count = pd.DataFrame()
    count = matches[matches.ProbH >= start].count()
    metron = pd.concat([mean,std_dev,count],axis=1)
    
    while index > end:
        start = index
        index = round(index - step,2)
        mean = matches[(matches.ProbH < start) & (matches.ProbH >= index)].mean()
        std_dev = matches[(matches.ProbH < start) & (matches.ProbH >= index)].std()
        count = matches[(matches.ProbH < start) & (matches.ProbH >= index)].count()
        metron = pd.concat([metron,mean,std_dev,count],axis=1)

        columns.append(f'({start},{index}] AVG')
        columns.append(f'({start},{index}] STD')
        columns.append(f'({start},{index}] OCR')
        
    mean = matches[matches.ProbH < index].mean()
    std_dev = matches[matches.ProbH < index].std()
    count = matches[matches.ProbH < index].count()
    metron = pd.concat([metron,mean,std_dev,count],axis=1)

    columns.append(f'({index},0.00) AVG')
    columns.append(f'({index},0.00) STD')
    columns.append(f'({index},0.00) OCR')

    metron.columns = [columns]
    
    return metron


def reference_frame_mean(matches,start,end,step):
    
    index = start
    metron = pd.DataFrame()
    columns = [start]
    
    mean = pd.DataFrame()
    mean = matches[matches.ProbH >= start].mean()
    metron = pd.concat([mean],axis=1)
    
    while index > end:
        start = index
        index = round(index - step,2)
        mean = matches[(matches.ProbH < start) & (matches.ProbH >= index)].mean()
        metron = pd.concat([metron,mean],axis=1)

        columns.append(index)
        
    mean = matches[matches.ProbH < index].mean()
    metron = pd.concat([metron,mean],axis=1)

    columns.append(0)

    metron.columns = [columns]
    
    return metron


metron = pd.DataFrame()
metron = reference_frame_mean(matches_df,0.92,0.08,0.02)


metron = metron.T

metron = metron[['OddH', 'OddD', 'OddA', 'ProbH', 'ProbD', 'ProbA', 'FTHG', 'FTAG', 'HTHG', 'HTAG', 'HS', 'AS', 'HST', 'AST', 'HF', 'AF',
       'HY', 'AY', 'HR', 'AR']]

metron.to_excel('reference_system_means.xlsx',encoding='iso-8859-15',index=True)