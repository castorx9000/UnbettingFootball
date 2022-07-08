import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


coaches_df = pd.read_excel('coachs_profiles.xlsx')
coaches_df = coaches_df[['Name','Matches','Performance','obPPM','exPPM','h_obPts','h_exPts','a_obPts','a_exPts','H_Matches','A_Matches']]

coaches_df['obPPM_A'] = ''
coaches_df['exPPM_A'] = ''
coaches_df['Performance_A'] = ''

coaches_df.obPPM_A = coaches_df.a_obPts / coaches_df.A_Matches
coaches_df.exPPM_A = coaches_df.a_exPts / coaches_df.A_Matches
coaches_df.Performance_A = coaches_df.a_obPts / coaches_df.a_exPts
coaches_df = coaches_df.sort_values(by=['Performance_A'], ascending=False)

obPPM = coaches_df['obPPM_A'].tolist()
exPPM = coaches_df['exPPM_A'].tolist()
coaches = coaches_df['Name'].tolist()
performances = coaches_df['Performance_A'].tolist()
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
    
    x = np.linspace(0.7,1.8,50)
    y = x
    plt.plot(x, y, color='lightgray',linestyle='dashed')
    plt.xlim(0.7,1.8)
    plt.ylim(0.7,1.8)
    plt.xlabel('Expected Points Per Away Match')
    plt.ylabel('Obtained Points Per Away Match')
    plt.title('Expected vs Obtained Points Per Away Match\nCoaches with 30 or more matches\nLigaMX seasons 2011-2020\n(includes Juan Carlos Osorio with Atletico Nacional)')

    plt.annotate(f'Tomás Boy\n{128.2} %',xy=(1.09,1.398),fontsize=8,color='blue',xytext=(1.02,1.455),arrowprops=dict(facecolor='blue',arrowstyle='->'))
    plt.annotate(f'Ignacio Ambriz\n{123.5} %',xy=(1.145,1.408),fontsize=8,color='blue')
    plt.annotate(f'Guillermo Vázquez\n{122.7} %',xy=(1.113,1.365),fontsize=8,color='blue',xytext=(1.09,1.435),arrowprops=dict(facecolor='blue',arrowstyle='->'))
    plt.annotate(f'Matías Almeyda\n{121.5} %',xy=(1.134,1.36),fontsize=8,color='blue')
    
    plt.annotate(f'Gustavo Matosas\n{108.3} %',xy=(1.16,1.257),fontsize=8,color='dodgerblue',xytext=(1.101,1.297),arrowprops=dict(facecolor='blue',arrowstyle='->'))  
    plt.annotate(f'Hernán Cristante\n{106.8} %',xy=(1.169,1.22),fontsize=8,color='dodgerblue')
    plt.annotate(f'José Manuel de la Torre\n{90.6} %',xy=(1.023,0.927),fontsize=8,color='red',xytext=(0.97,1.009),arrowprops=dict(facecolor='blue',arrowstyle='->'))
    plt.annotate(f'Robert Dante Siboldi\n{86.7} %',xy=(1.068,0.927),fontsize=8,color='red',xytext=(1.047,0.987),arrowprops=dict(facecolor='blue',arrowstyle='->'))
    plt.annotate(f'Francisco Palencia\n{78} %',xy=(1.013,0.789),fontsize=8,color='red',xytext=(1.053,0.789),arrowprops=dict(facecolor='blue',arrowstyle='->'))
    plt.annotate(f'Roberto Hernández\n{133.4} %',xy=(1.005,1.333),fontsize=8,color='blue')
    plt.annotate(f'Alfonso Sosa\n{119} %',xy=(0.925,1.095),fontsize=8,color='blue')
    plt.annotate(f'Juan Carlos Osorio\n{117.9} %',xy=(1.354,1.591),fontsize=8,color='blue')
    plt.annotate(f'Miguel Herrera\n{115.6} %',xy=(1.318,1.518),fontsize=8,color='blue')
    plt.annotate(f'Enrique Meza\n{113.8} %',xy=(1.065,1.255),fontsize=8,color='blue')
    plt.annotate(f'Luis Fernando Tena\n{111.2} %',xy=(1.204,1.333),fontsize=8,color='blue')
    plt.annotate(f'Antonio Mohamed\n{108.3} %',xy=(1.282,1.383),fontsize=8,color='dodgerblue')
    plt.annotate(f'José Saturnino Cardozo\n{108.1} %',xy=(1.069,1.15),fontsize=8,color='steelblue')
    plt.annotate(f'Ricardo Ferreti \n{105.6} %',xy=(1.358,1.429),fontsize=8,color='dodgerblue')
    plt.annotate(f'Pedro Caixinha\n{104.7} %',xy=(1.23,1.282),fontsize=8,color='steelblue')
    plt.annotate(f'Sergio Bueno\n{103.4} %',xy=(0.91,0.965),fontsize=8,color='steelblue')
    plt.annotate(f'Rubén Omar Romano\n{97.6} %',xy=(0.96,0.946),fontsize=8,color='lightcoral')
    plt.annotate(f'Benjamín Galindo\n{96.9} %',xy=(1.163,1.122),fontsize=8,color='lightcoral')
    plt.annotate(f'Rafael Puente Jr.\n{90.7} %',xy=(0.9,0.843),fontsize=8,color='red')
    plt.annotate(f'Víctor Manuel Vucetich\n{85.7} %',xy=(1.112,0.956),fontsize=8,color='red')
    plt.annotate(f'José Guadalupe Cruz\n{85.4} %',xy=(0.983,0.835),fontsize=8,color='red')
    plt.annotate(f'Diego Alonso\n{85.3} %',xy=(1.279,1.087),fontsize=8,color='red')
    plt.annotate(f'Pablo Marini\n{79.5} %',xy=(0.973,0.791),fontsize=8,color='red')
    plt.annotate(f'Ricardo Lavolpe\n{79.4} %',xy=(1.134,0.897),fontsize=8,color='red')
    plt.annotate(f'Carlos Reinoso\n{77.5} %',xy=(0.965,0.744),fontsize=8,color='red')
    

    #plt.figure(figsize=(10,10))
    #plt.style.use('fivethirtyeight')
    plt.legend()
    plt.show()
    print(coaches_df[['Name','Performance_A','exPPM_A','obPPM_A']])
