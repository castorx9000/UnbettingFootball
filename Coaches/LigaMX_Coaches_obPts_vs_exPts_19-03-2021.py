import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


coaches_df = pd.read_excel('coachs_profiles_19-03-2021.xlsx')
coaches_df = coaches_df[['Name','Matches','Performance','obPPM','exPPM']]
coaches_df = coaches_df.sort_values(by=['Performance'], ascending=False)

obPPM = coaches_df['obPPM'].tolist()
exPPM = coaches_df['exPPM'].tolist()
coaches = coaches_df['Name'].tolist()
performances = coaches_df['Performance'].tolist()
performances = [ i*100 for i in performances ]

# lists of data with performance lesser than 95
obPPM_lowest = []
exPPM_lowest = []
coaches_lowest = []

# lists of data with performance between 100 and 95
obPPM_low = []
exPPM_low = []
coaches_low = []

# lists of data with performance between 105 and 100
obPPM_good = []
exPPM_good = []
coaches_good = []

# lists of data with performance between 110 and 105
obPPM_high = []
exPPM_high = []
coaches_high = []

# lists of data with performance above 110
obPPM_highest = []
exPPM_highest = []
coaches_highest = []

# Process to separate coaches data into lists according to their performances: 
# lesser tan 95% (lowest), between 100% and 95% (low), between 105 and 100 (good),
# between 110 and 105 (high) and greater than 110% (highest)

i = 0
for performance in performances:
    if performance < 95:
        obPPM_lowest.append(obPPM[i])
        exPPM_lowest.append(exPPM[i])
        coaches_lowest.append(coaches[i])
        
    if (performance < 100) and (performance >= 95):
        obPPM_low.append(obPPM[i])
        coaches_low.append(coaches[i])
        exPPM_low.append(exPPM[i])
        
    if (performance < 105) and (performance >= 100):
        obPPM_good.append(obPPM[i])
        coaches_good.append(coaches[i])
        exPPM_good.append(exPPM[i])

    if (performance < 110) and (performance >= 105):
        obPPM_high.append(obPPM[i])
        coaches_high.append(coaches[i])
        exPPM_high.append(exPPM[i])

    if performance >= 110:
        obPPM_highest.append(obPPM[i])
        coaches_highest.append(coaches[i])
        exPPM_highest.append(exPPM[i])

    i += 1


if __name__ == "__main__":

    
    plt.scatter(exPPM_highest, obPPM_highest, s=30, c='blue', label='Performance greater than 110%')
    plt.scatter(exPPM_high, obPPM_high, s=30, c='dodgerblue', label='Performance between 110% & 105%')
    plt.scatter(exPPM_good, obPPM_good, s=30, c='steelblue', label='Performance between 105% & 100%')
    plt.scatter(exPPM_low, obPPM_low, s=30, c='lightcoral', label='Performance between 100% & 95%')
    plt.scatter(exPPM_lowest, obPPM_lowest, s=30, c='red', label='Performance lesser than 95%')
    
    x = np.linspace(0.95,1.8,50)
    y = x
    plt.plot(x, y, color='lightgray',linestyle='dashed')
    plt.xlim(0.95,1.8)
    plt.ylim(0.95,1.8)
    plt.xlabel('Expected Points Per Match')
    plt.ylabel('Obtained Points Per Match')
    #plt.title('Expected vs Obtained Points Per Match \nCoaches with 60 or more matches\nLigaMX seasons 2011-2020\n(includes Juan Carlos Osorio with Atletico Nacional)')
    plt.title('Expected vs Obtained Points Per Match \nCoaches with 60 or more matches\nLigaMX seasons 2011-2020')

    
    plt.annotate(f'Rafael Puente Jr.\n{81.5} %',xy=(1.152,0.938),fontsize=8,color='red')
    plt.annotate(f'Rubén Omar Romano\n{88.9} %',xy=(1.235,1.098),fontsize=8,color='red')
    plt.annotate(f'Sergio Bueno\n{96.3} %',xy=(1.18,1.136),fontsize=8,color='lightcoral')
    plt.annotate(f'Pablo Marini\n{95.4} %',xy=(1.212,1.156),fontsize=8,color='lightcoral')
    plt.annotate(f'Francisco Palencia\n{95.6} %',xy=(1.253,1.197),fontsize=8,color='lightcoral')
    #plt.annotate(f'Juan Carlos Osorio\n{104.5} %',xy=(1.719,1.645),fontsize=8,color='steelblue')
    plt.annotate(f'Alfonso Sosa\n{105} %',xy=(1.172,1.231),fontsize=8,color='steelblue')
    plt.annotate(f'Ricardo Lavolpe\n{95.1} %',xy=(1.361,1.295),fontsize=8,color='lightcoral')
    plt.annotate(f'Matías Almeyda\n{97.1} %',xy=(1.397,1.356),fontsize=8,color='lightcoral')
    plt.annotate(f'Carlos Reinoso\n{98.6} %',xy=(1.255,1.238),fontsize=8,color='lightcoral')
    plt.annotate(f'Robert Dante Siboldi\n{99.8} %',xy=(1.385,1.382),fontsize=8,color='lightcoral')    
    plt.annotate(f'José Guadalupe Cruz\n{99.6} %',xy=(1.237,1.233),fontsize=8,color='steelblue',xytext=(1.16,1.27),arrowprops=dict(facecolor='black',arrowstyle='->'))
    plt.annotate(f'Enrique Meza\n{100.9} %',xy=(1.355,1.367),fontsize=8,color='steelblue')
    plt.annotate(f'José Manuel de la Torre\n{101.6} %',xy=(1.255,1.276),fontsize=8,color='steelblue')
    plt.annotate(f'José Saturnino Cardozo\n{103.3} %',xy=(1.323,1.367),fontsize=8,color='steelblue')
    plt.annotate(f'Roberto Hernández\n{112.2} %',xy=(1.201,1.387),fontsize=8,color='blue')
    plt.annotate(f'Víctor Manuel Vucetich\n{102} %',xy=(1.381,1.409),fontsize=8,color='steelblue',xytext=(1.419,1.395),arrowprops=dict(facecolor='black',arrowstyle='->'))
    plt.annotate(f'Tomás Boy\n{102.8} %',xy=(1.325,1.363),fontsize=8,color='steelblue')    
    plt.annotate(f'Benjamín Galindo\n{99.2} %',xy=(1.454,1.443),fontsize=8,color='lightcoral')
    plt.annotate(f'Luis Fernando Tena\n{97.2} %',xy=(1.437,1.397),fontsize=8,color='lightcoral',xytext=(1.505,1.472),arrowprops=dict(facecolor='black',arrowstyle='->'))
    plt.annotate(f'Gustavo Matosas\n{101.4} %',xy=(1.449,1.469),fontsize=8,color='steelblue')
    plt.annotate(f'Guillermo Vázquez\n{107.2} %',xy=(1.349,1.447),fontsize=8,color='blue')
    plt.annotate(f'Ignacio Ambriz\n{106.8} %',xy=(1.441,1.539),fontsize=8,color='dodgerblue')
    plt.annotate(f'Hernán Cristante\n{109.2} %',xy=(1.413,1.542),fontsize=8,color='dodgerblue')
    plt.annotate(f'Diego Alonso\n{101.3} %',xy=(1.526,1.546),fontsize=8,color='steelblue')
    plt.annotate(f'Pedro Caixinha\n{105} %',xy=(1.5,1.575),fontsize=8,color='dodgerblue')
    plt.annotate(f'Antonio Mohamed\n{106} %',xy=(1.558,1.652),fontsize=8,color='dodgerblue')
    plt.annotate(f'Miguel Herrera\n{107.1} %',xy=(1.551,1.661),fontsize=8,color='dodgerblue')
    plt.annotate(f'Ricardo Ferreti \n{102.3} %',xy=(1.634,1.671),fontsize=8,color='steelblue')
    plt.annotate(f'Guillermo Almada \n{109.7} %',xy=(1.529,1.677),fontsize=8,color='dodgerblue')
    plt.annotate(f'Gabriel Caballero \n{101.3} %',xy=(1.145,1.159),fontsize=8,color='steelblue')
    plt.annotate(f'Diego Cocca \n{99.6} %',xy=(1.306,1.302),fontsize=8,color='lightcoral')

    plt.style.use('fivethirtyeight')
    plt.legend()
    plt.show()
    print(coaches_df)
