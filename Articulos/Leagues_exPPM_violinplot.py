import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

if __name__ == "__main__":
    
    # load data into dataframe
    df = pd.read_excel('Leagues_exPPM_5clubs.xlsx', engine='openpyxl')

    fig, axes = plt.subplots()
    # plot violin, 'League' is according to x axis
    # exPPM is y axis
    sns.violinplot('exPPM','League',data=df,ax=axes)
    axes.set_title('Leagues\' Density of Expected Points\nSeasons 2020-2021', fontsize=20)
    axes.yaxis.grid(True)
    axes.set_xlabel('Expected Points Per Match', fontsize=12)
    axes.set_ylabel('Leagues', fontsize=12)

    plt.show()