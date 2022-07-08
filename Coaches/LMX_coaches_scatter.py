import pandas as pd
import numpy as np

data_frame = pd.read_excel('coaches_performances_v2.1.xlsx')
data_frame = data_frame[['Name','Performance','obPPM','exPPM']]
data_frame = data_frame.sort_values(by=['obPPM'], ascending=True)

print(data_frame)

obPPM = data_frame['obPPM'].tolist()
coaches = data_frame['Name'].tolist()
performances = data_frame['Performance'].tolist()
exPPM = data_frame['exPPM'].tolist()

obPPM_poor = []
coaches_poor = []
exPPM_poor = []

obPPM_average = []
coaches_average = []
exPPM_average = []

obPPM_good = []
coaches_good = []
exPPM_good = []


# Process to separate coaches info intro lists according to
# their performance: less tan 95% (poor), between 95% and 
# 105% (average) and more tan 105% (high) 
i = 0
for performance in performances:
    if performance < 95:
        obPPM_poor.append(obPPM[i])
        coaches_poor.append(coaches[i])
        exPPM_poor.append(exPPM[i])
    elif performance <= 105:
        obPPM_average.append(obPPM[i])
        coaches_average.append(coaches[i])
        exPPM_average.append(exPPM[i])
    else:
        obPPM_good.append(obPPM[i])
        coaches_good.append(coaches[i])
        exPPM_good.append(exPPM[i])
    i += 1


plt.scatter(exPPM_good, obPPM_good, s=30, c='blue', label='Performance greater than 105%')
plt.scatter(exPPM_average, obPPM_average, s=30, c='black', label='Performance between 105% & 95%')
plt.scatter(exPPM_poor, obPPM_poor, s=30, c='red', label='Performance lesser than 95%')

x = np.linspace(0.95,1.7,50)
y = x
plt.plot(x, y, color='black',linestyle='dashed')
plt.xlim(0.95,1.7)
plt.ylim(0.95,1.7)
plt.xlabel('Expected Points Per Match')
plt.ylabel('Obtained Points Per Match')
plt.title('Expected vs Obtained Points Per Match \nCoaches with 60 or more matches\nLigaMX seasons 2011-2020')
#z = np.polyfit(exPPM,obPPM,1)
#p = np.poly1d(z)
#plt.plot(exPPM,p(exPPM),'r--')
plt.annotate(f'Rafael Puente Jr.\n{84.4} %',xy=(1.155,0.975),fontsize=8,color='red',label='Performance < 95%')
plt.annotate(f'Rubén Omar Romano\n{89.4} %',xy=(1.235,1.105),fontsize=8,color='red')
plt.annotate(f'Sergio Bueno\n{96.7} %',xy=(1.172,1.112),fontsize=8)
plt.annotate(f'Pablo Marini\n{95.9} %',xy=(1.205,1.171),fontsize=8)
plt.annotate(f'Francisco Palencia\n{96} %',xy=(1.235,1.207),fontsize=8)
plt.annotate(f'Alfonso Sosa\n{104.3} %',xy=(1.165,1.233),fontsize=8)
plt.annotate(f'Carlos Reinoso\n{99.2} %',xy=(1.25,1.236),fontsize=8,xytext=(1.285,1.16),arrowprops=dict(facecolor='blue',arrowstyle='->'))
plt.annotate(f'José Manuel de la Torre\n{100} %',xy=(1.25,1.25),fontsize=8,xytext=(1.175,1.279),arrowprops=dict(facecolor='blue',arrowstyle='->'))
plt.annotate(f'José Guadalupe Cruz\n{99.2} %',xy=(1.26,1.25),fontsize=8,xytext=(1.36,1.21),arrowprops=dict(facecolor='black',arrowstyle='->'))
plt.annotate(f'Ricardo Lavolpe\n{94.9} %',xy=(1.365,1.265),fontsize=8,color='red')
plt.annotate(f'Matías Almeyda\n{97.1} %',xy=(1.405,1.365),fontsize=8)
plt.annotate(f'Robert Dante Siboldi\n{103.8} %',xy=(1.322,1.372),fontsize=8,xytext=(1.31,1.437),arrowprops=dict(facecolor='black',arrowstyle='->'))
plt.annotate(f'José Saturnino Cardozo\n{103.8} %',xy=(1.322,1.37),fontsize=8,xytext=(1.25,1.319),arrowprops=dict(facecolor='black',arrowstyle='->'))
plt.annotate(f'Enrique Meza\n{100.8} %',xy=(1.36,1.37),fontsize=8,xytext=(1.365,1.31),arrowprops=dict(facecolor='black',arrowstyle='->'))
plt.annotate(f'Roberto Hernández\n{112.2} %',xy=(1.235,1.385),fontsize=8,color='blue')
plt.annotate(f'Víctor Manuel Vucetich\n{101.5} %',xy=(1.372,1.39),fontsize=8,xytext=(1.415,1.395),arrowprops=dict(facecolor='black',arrowstyle='->'))
plt.annotate(f'Tomás Boy\n{104.4} %',xy=(1.355,1.415),fontsize=8)
plt.annotate(f'Benjamín Galindo\n{98.6} %',xy=(1.465,1.437),fontsize=8)
plt.annotate(f'Gustavo Matosas\n{101.4} %',xy=(1.425,1.477),fontsize=8)
plt.annotate(f'Luis Fernando Tena\n{100} %',xy=(1.472,1.47),fontsize=8,xytext=(1.505,1.472),arrowprops=dict(facecolor='black',arrowstyle='->'))
plt.annotate(f'Ignacio Ambriz\n{107.1} %',xy=(1.405,1.50),fontsize=8,color='blue')
plt.annotate(f'Guillermo Vázquez\n{110.2} %',xy=(1.37,1.51),fontsize=8,color='blue',xytext=(1.325,1.568),arrowprops=dict(facecolor='blue',arrowstyle='->'))
plt.annotate(f'Hernán Cristante\n{107.8} %',xy=(1.425,1.535),fontsize=8,color='blue')
plt.annotate(f'Diego Alonso\n{101.3} %',xy=(1.535,1.555),fontsize=8)
plt.annotate(f'Pedro Caixinha\n{104.7} %',xy=(1.505,1.575),fontsize=8,color='blue')
plt.annotate(f'Antonio Mohamed\n{106.5} %',xy=(1.556,1.636),fontsize=8,color='blue')
plt.annotate(f'Miguel Herrera\n{107.1} %',xy=(1.525,1.667),fontsize=8,color='blue')
plt.annotate(f'Ricardo Ferreti \n{103.1} %',xy=(1.635,1.675),fontsize=8)

#for i, txt in enumerate(coaches):
#    plt.annotate(f'{coaches[i]}\n{performances[i]} %', (exPPM[i]+0.005,obPPM[i]+0.005),fontsize=6)

plt.legend()
plt.show()

#graph = plt.scatter(obPPM, coaches, s=100, c='red')
#graph = plt.scatter(exPPM, coaches, s=100, c='green', marker='X')
#graph = plt.xticks(rotation=90)
#grah = plt.xticks(fontsize=8)
#graph = plt.xlabel('obtained and expected Points Per Match')
#graph = plt.title('Coaches with 60 matches or more \n sorted by performance')
#graph = plt.annotate('Best Performance: 112.56%',xy=(1,27),xytext=(1,1.5))

#plt.show(graph)