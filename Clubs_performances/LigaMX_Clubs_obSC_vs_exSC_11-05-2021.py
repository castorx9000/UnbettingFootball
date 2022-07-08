import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

paths = [
    r'D:\Dropbox\La Cima del Éxito\Futbol\Clus_Logos\AME96X96.png',
    r'D:\Dropbox\La Cima del Éxito\Futbol\Clus_Logos\CRA96X96.png',
    r'D:\Dropbox\La Cima del Éxito\Futbol\Clus_Logos\PUE96X96.png',
    r'D:\Dropbox\La Cima del Éxito\Futbol\Clus_Logos\MAZ96X96.png',
    r'D:\Dropbox\La Cima del Éxito\Futbol\Clus_Logos\TOL96X96.png',
    r'D:\Dropbox\La Cima del Éxito\Futbol\Clus_Logos\SAN96X96.png',
    r'D:\Dropbox\La Cima del Éxito\Futbol\Clus_Logos\QRO96X96.png',
    r'D:\Dropbox\La Cima del Éxito\Futbol\Clus_Logos\PUM96X96.png',
    r'D:\Dropbox\La Cima del Éxito\Futbol\Clus_Logos\CHI96X96.png',
    r'D:\Dropbox\La Cima del Éxito\Futbol\Clus_Logos\LEO96X96.png',
    r'D:\Dropbox\La Cima del Éxito\Futbol\Clus_Logos\TIJ96X96.png',
    r'D:\Dropbox\La Cima del Éxito\Futbol\Clus_Logos\ATL96X96.png',
    r'D:\Dropbox\La Cima del Éxito\Futbol\Clus_Logos\PAC96X96.png',
    r'D:\Dropbox\La Cima del Éxito\Futbol\Clus_Logos\MON96X96.png',
    r'D:\Dropbox\La Cima del Éxito\Futbol\Clus_Logos\JUA96X96.png',
    r'D:\Dropbox\La Cima del Éxito\Futbol\Clus_Logos\TIG96X96.png',
    r'D:\Dropbox\La Cima del Éxito\Futbol\Clus_Logos\ASL96X96.png',
    r'D:\Dropbox\La Cima del Éxito\Futbol\Clus_Logos\NEC96X96.png'
    ]

clubs_df = pd.read_excel('D:\Dropbox\La Cima del Éxito\Futbol\Clubs_performances\Liga MX_2020-2021_enero-mayo_11-05-2021.xlsx')
clubs_df = clubs_df[['Club','Performance','p_SG','obSGPM','exSGPM','obCGPM','exCGPM']]
clubs_df = clubs_df.sort_values(by=['Performance'], ascending=False)

obSGPM = clubs_df['obSGPM'].tolist()
exSGPM = clubs_df['exSGPM'].tolist()
obCGPM = clubs_df['obCGPM'].tolist()
exCGPM = clubs_df['exCGPM'].tolist()
clubs = clubs_df['Club'].tolist()
performances = clubs_df['Performance'].tolist()
performances = [ i*100 for i in performances ]


if __name__ == "__main__":

    x = exSGPM
    y = obSGPM

    x2 = exCGPM
    y2 = obCGPM

    fig, (ax, ax2) = plt.subplots(1, 2)
    ax.scatter(x, y)
    ax.set_xlim([0, 3])
    ax.set_ylim([0, 3])
    ax.set_title('Scored Goals')
    ax.set_xlabel('Expected Scored Goals')
    ax.set_ylabel('Observed Scored Goals')
    ax2.scatter(x2, y2)
    ax2.set_xlim([0, 3])
    ax2.set_ylim([0, 3])
    ax2.set_title('Conceided Goals')
    ax2.set_xlabel('Expected Conceided Goals')
    ax2.set_ylabel('Observed Conceided Goals')


    for x0, y0, path in zip(exSGPM, obSGPM, paths):
        ab = AnnotationBbox(OffsetImage(plt.imread(path), zoom=0.3), (x0, y0), frameon=False)
        ax.add_artist(ab)

    for x0, y0, path in zip(exCGPM, obCGPM, paths):
        ab = AnnotationBbox(OffsetImage(plt.imread(path), zoom=0.3), (x0, y0), frameon=False)
        ax2.add_artist(ab)
    
    x = np.linspace(0,3,50)
    y = x
    
    ax.plot(x, y, color='black',linestyle='dashed')
    ax2.plot(x, y, color='black',linestyle='dashed')

    fig.suptitle('Observed vs Expected Goals per Match \nLigaMX season Guardianes 2021', size=15)

    plt.style.use('fivethirtyeight')
    plt.show()
    print(clubs_df)
