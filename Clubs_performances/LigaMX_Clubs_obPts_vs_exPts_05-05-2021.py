import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

paths = [
    r'D:\Dropbox\La Cima del Éxito\Futbol\Liga_MX_escudos\AME96X96.png',
    r'D:\Dropbox\La Cima del Éxito\Futbol\Liga_MX_escudos\PUE96X96.png',
    r'D:\Dropbox\La Cima del Éxito\Futbol\Liga_MX_escudos\PUM96X96.png',
    r'D:\Dropbox\La Cima del Éxito\Futbol\Liga_MX_escudos\CRA96X96.png',
    r'D:\Dropbox\La Cima del Éxito\Futbol\Liga_MX_escudos\LEO96X96.png',
    r'D:\Dropbox\La Cima del Éxito\Futbol\Liga_MX_escudos\TOL96X96.png',
    r'D:\Dropbox\La Cima del Éxito\Futbol\Liga_MX_escudos\CHI96X96.png',
    r'D:\Dropbox\La Cima del Éxito\Futbol\Liga_MX_escudos\SAN96X96.png',
    r'D:\Dropbox\La Cima del Éxito\Futbol\Liga_MX_escudos\MAZ96X96.png',
    r'D:\Dropbox\La Cima del Éxito\Futbol\Liga_MX_escudos\JUA96X96.png',
    r'D:\Dropbox\La Cima del Éxito\Futbol\Liga_MX_escudos\MON96X96.png',
    r'D:\Dropbox\La Cima del Éxito\Futbol\Liga_MX_escudos\PAC96X96.png',
    r'D:\Dropbox\La Cima del Éxito\Futbol\Liga_MX_escudos\NEC96X96.png',
    r'D:\Dropbox\La Cima del Éxito\Futbol\Liga_MX_escudos\TIG96X96.png',
    r'D:\Dropbox\La Cima del Éxito\Futbol\Liga_MX_escudos\ATL96X96.png',
    r'D:\Dropbox\La Cima del Éxito\Futbol\Liga_MX_escudos\TIJ96X96.png',
    r'D:\Dropbox\La Cima del Éxito\Futbol\Liga_MX_escudos\QRO96X96.png',
    r'D:\Dropbox\La Cima del Éxito\Futbol\Liga_MX_escudos\ASL96X96.png'
    ]

clubs_df = pd.read_excel('D:\Dropbox\La Cima del Éxito\Futbol\Clubs_performances\Liga MX_2020-2021_enero-mayo_05-05-2021.xlsx')
clubs_df = clubs_df[['Club','Performance','obPPM','exPPM']]
clubs_df = clubs_df.sort_values(by=['Performance'], ascending=False)

obPPM = clubs_df['obPPM'].tolist()
exPPM = clubs_df['exPPM'].tolist()
clubs = clubs_df['Club'].tolist()
performances = clubs_df['Performance'].tolist()
performances = [ i*100 for i in performances ]


if __name__ == "__main__":

    x = exPPM
    y = obPPM

    fig, ax = plt.subplots()
    ax.scatter(x, y)

    for x0, y0, path in zip(exPPM, obPPM, paths):
        ab = AnnotationBbox(OffsetImage(plt.imread(path), zoom=0.4), (x0, y0), frameon=False)
        ax.add_artist(ab)
    
    x = np.linspace(0,3,50)
    y = x
    plt.plot(x, y, color='black',linestyle='dashed')
    plt.xlim(0.0,3)
    plt.ylim(0.0,3)
    plt.xlabel('Expected Points Per Match')
    plt.ylabel('Obtained Points Per Match')
    plt.title('Expected vs Obtained Points Per Match \nLigaMX season Guardianes 2020 & Guardianes 2021')

    plt.style.use('fivethirtyeight')
    plt.show()
    print(clubs_df)
