import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


coaches_df = pd.read_excel('coachs_profiles.xlsx')
coaches_df = coaches_df[['Name','Matches','Performance','obPPM','exPPM','h_obPts','h_exPts','a_obPts','a_exPts','H_Matches','A_Matches']]

coaches_df['obPPM_H'] = ''
coaches_df['exPPM_H'] = ''
coaches_df['Performance_H'] = ''

coaches_df.obPPM_H = coaches_df.h_obPts / coaches_df.H_Matches
coaches_df.exPPM_H = coaches_df.h_exPts / coaches_df.H_Matches
coaches_df.Performance_H = coaches_df.h_obPts / coaches_df.h_exPts
coaches_df = coaches_df.sort_values(by=['Performance_H'], ascending=False)

obPPM = coaches_df['obPPM_H'].tolist()
exPPM = coaches_df['exPPM_H'].tolist()
coaches = coaches_df['Name'].tolist()
performances = coaches_df['Performance_H'].tolist()
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
    
    x = np.linspace(0.95,2.1,50)
    y = x
    plt.plot(x, y, color='lightgray',linestyle='dashed')
    plt.xlim(0.95,2.1)
    plt.ylim(0.95,2.1)
    plt.xlabel('Expected Points Per Match at Home')
    plt.ylabel('Obtained Points Per Match at Home')
    plt.title('Expected vs Obtained Points Per Match at Home \nCoaches with 30 or more matches\nLigaMX seasons 2011-2020\n(includes Juan Carlos Osorio with Atletico Nacional)')

    
    plt.annotate(f'Rafael Puente Jr.\n{79.3} %',xy=(1.387,1.097),fontsize=8,color='red')
    plt.annotate(f'Rubén Omar Romano\n{83.2} %',xy=(1.527,1.267),fontsize=8,color='red')
    plt.annotate(f'Sergio Bueno\n{91.4} %',xy=(1.475,1.343),fontsize=8,color='red')
    plt.annotate(f'Pablo Marini\n{106.3} %',xy=(1.446,1.531),fontsize=8,color='dodgerblue')
    plt.annotate(f'Francisco Palencia\n{107.5} %',xy=(1.498,1.605),fontsize=8,color='dodgerblue')  
    plt.annotate(f'Juan Carlos Osorio\n{95.1} %',xy=(1.949,1.848),fontsize=8,color='lightcoral')
    plt.annotate(f'Alfonso Sosa\n{95} %',xy=(1.411,1.346),fontsize=8,color='lightcoral')
    plt.annotate(f'Matías Almeyda\n{81} %',xy=(1.659,1.339),fontsize=8,color='red')
    plt.annotate(f'José Guadalupe Cruz\n{109.6} %',xy=(1.526,1.667),fontsize=8,color='dodgerblue')    
    plt.annotate(f'Enrique Meza\n{92.5} %',xy=(1.608,1.483),fontsize=8,color='red')
    plt.annotate(f'José Saturnino Cardozo\n{100.1} %',xy=(1.584,1.545),fontsize=8,color='steelblue')    
    plt.annotate(f'Roberto Hernández\n{97} %',xy=(1.474,1.425),fontsize=8,color='lightcoral')
    plt.annotate(f'Tomás Boy\n{87.9} %',xy=(1.621,1.42),fontsize=8,color='red')        
    plt.annotate(f'Benjamín Galindo\n{100.9} %',xy=(1.78,1.764),fontsize=8,color='steelblue')    
    plt.annotate(f'Luis Fernando Tena\n{92.1} %',xy=(1.749,1.607),fontsize=8,color='red')    
    plt.annotate(f'Gustavo Matosas\n{96.7} %',xy=(1.747,1.685),fontsize=8,color='lightcoral')   
    plt.annotate(f'Guillermo Vázquez\n{102.1} %',xy=(1.627,1.651),fontsize=8,color='steelblue')
    plt.annotate(f'Ignacio Ambriz\n{96} %',xy=(1.66,1.589),fontsize=8,color='lightcoral')    
    plt.annotate(f'Diego Alonso\n{112.7} %',xy=(1.78,2),fontsize=8,color='blue')
    plt.annotate(f'Pedro Caixinha\n{105.2} %',xy=(1.767,1.854),fontsize=8,color='dodgerblue')   
    plt.annotate(f'Antonio Mohamed\n{105.4} %',xy=(1.822,1.897),fontsize=8,color='dodgerblue')
    plt.annotate(f'Miguel Herrera\n{100.3} %',xy=(1.806,1.806),fontsize=8,color='steelblue')
    plt.annotate(f'Ricardo Ferreti \n{102.3} %',xy=(1.897,1.939),fontsize=8,color='steelblue')
    plt.annotate(f'Víctor Manuel Vucetich\n{112.1} %',xy=(1.645,1.845),fontsize=8,color='blue',xytext=(1.55,1.95),arrowprops=dict(facecolor='blue',arrowstyle='->'))
    plt.annotate(f'Hernán Cristante\n{108.3} %',xy=(1.689,1.83),fontsize=8,color='dodgerblue',xytext=(1.689,1.89),arrowprops=dict(facecolor='blue',arrowstyle='->'))
    plt.annotate(f'Ricardo Lavolpe\n{106.9} %',xy=(1.611,1.722),fontsize=8,color='dodgerblue',xytext=(1.641,1.702),arrowprops=dict(facecolor='blue',arrowstyle='->'))
    plt.annotate(f'Robert Dante Siboldi\n{107.6} %',xy=(1.614,1.737),fontsize=8,color='dodgerblue',xytext=(1.624,1.757),arrowprops=dict(facecolor='blue',arrowstyle='->'))            
    plt.annotate(f'Carlos Reinoso\n{111.5} %',xy=(1.535,1.707),fontsize=8,color='blue',xytext=(1.4,1.71),arrowprops=dict(facecolor='blue',arrowstyle='->'))
    plt.annotate(f'José Manuel de la Torre\n{111.5} %',xy=(1.556,1.735),fontsize=8,color='blue',xytext=(1.51,1.79),arrowprops=dict(facecolor='blue',arrowstyle='->'))
    

    #plt.figure(figsize=(10,10))
    #plt.style.use('fivethirtyeight')
    plt.legend()
    plt.show()
    #print(coaches_df[['Name','Performance_H','exPPM_H','obPPM_H']])
