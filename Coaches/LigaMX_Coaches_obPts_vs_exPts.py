import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


coaches_df = pd.read_excel('coachs_profiles.xlsx')
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

    plt.annotate(f'Rafael Puente Jr.\n{83.7} %',xy=(1.159,0.967),fontsize=8,color='red')
    plt.annotate(f'Rubén Omar Romano\n{89.4} %',xy=(1.239,1.09),fontsize=8,color='red')
    plt.annotate(f'Sergio Bueno\n{96.7} %',xy=(1.185,1.117),fontsize=8,color='lightcoral')
    plt.annotate(f'Pablo Marini\n{95.9} %',xy=(1.218,1.157),fontsize=8,color='lightcoral')
    plt.annotate(f'Francisco Palencia\n{96} %',xy=(1.259,1.197),fontsize=8,color='lightcoral')
    #plt.annotate(f'Juan Carlos Osorio\n{104.2} %',xy=(1.649,1.718),fontsize=8,color='steelblue')
    plt.annotate(f'Alfonso Sosa\n{104.2} %',xy=(1.165,1.231),fontsize=8,color='steelblue')
    plt.annotate(f'Ricardo Lavolpe\n{95.1} %',xy=(1.365,1.265),fontsize=8,color='lightcoral')
    plt.annotate(f'Matías Almeyda\n{97.1} %',xy=(1.4,1.355),fontsize=8,color='lightcoral')
    plt.annotate(f'Carlos Reinoso\n{98.6} %',xy=(1.261,1.232),fontsize=8,color='lightcoral')
    plt.annotate(f'Robert Dante Siboldi\n{98.9} %',xy=(1.335,1.307),fontsize=8,color='lightcoral')    
    plt.annotate(f'José Guadalupe Cruz\n{100} %',xy=(1.248,1.248),fontsize=8,color='steelblue',xytext=(1.16,1.27),arrowprops=dict(facecolor='black',arrowstyle='->'))
    plt.annotate(f'Enrique Meza\n{100.9} %',xy=(1.335,1.336),fontsize=8,color='steelblue')
    plt.annotate(f'José Manuel de la Torre\n{102.2} %',xy=(1.224,1.301),fontsize=8,color='steelblue')
    plt.annotate(f'José Saturnino Cardozo\n{103.3} %',xy=(1.279,1.367),fontsize=8,color='steelblue')
    plt.annotate(f'Roberto Hernández\n{112.2} %',xy=(1.201,1.387),fontsize=8,color='blue')
    plt.annotate(f'Víctor Manuel Vucetich\n{101.4} %',xy=(1.375,1.392),fontsize=8,color='steelblue',xytext=(1.419,1.395),arrowprops=dict(facecolor='black',arrowstyle='->'))
    plt.annotate(f'Tomás Boy\n{104.1} %',xy=(1.355,1.415),fontsize=8,color='steelblue')    
    plt.annotate(f'Benjamín Galindo\n{99.2} %',xy=(1.46,1.432),fontsize=8,color='lightcoral')
    plt.annotate(f'Luis Fernando Tena\n{99.9} %',xy=(1.472,1.47),fontsize=8,color='lightcoral',xytext=(1.505,1.472),arrowprops=dict(facecolor='black',arrowstyle='->'))
    plt.annotate(f'Gustavo Matosas\n{101.4} %',xy=(1.425,1.477),fontsize=8,color='steelblue')
    plt.annotate(f'Guillermo Vázquez\n{110.3} %',xy=(1.345,1.523),fontsize=8,color='blue')
    plt.annotate(f'Ignacio Ambriz\n{107} %',xy=(1.405,1.503),fontsize=8,color='dodgerblue')
    plt.annotate(f'Hernán Cristante\n{107.7} %',xy=(1.425,1.538),fontsize=8,color='dodgerblue')
    plt.annotate(f'Diego Alonso\n{101.3} %',xy=(1.515,1.557),fontsize=8,color='steelblue')
    plt.annotate(f'Pedro Caixinha\n{105} %',xy=(1.471,1.58),fontsize=8,color='dodgerblue')
    plt.annotate(f'Antonio Mohamed\n{106.6} %',xy=(1.52,1.622),fontsize=8,color='dodgerblue')
    plt.annotate(f'Miguel Herrera\n{106.9} %',xy=(1.527,1.667),fontsize=8,color='dodgerblue')
    plt.annotate(f'Ricardo Ferreti \n{103.7} %',xy=(1.628,1.675),fontsize=8,color='steelblue')

    #plt.figure(figsize=(10,10))
    #plt.style.use('fivethirtyeight')
    plt.legend()
    plt.show()
    #print(coaches_df)
