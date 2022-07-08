import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.pylab as pylab
params = {'legend.fontsize': 22,
          'figure.figsize': (14.5, 9.5),
         'axes.labelsize': 'x-large',
         'axes.titlesize':60,
         'xtick.labelsize':'x-large',
         'ytick.labelsize':'large'}
pylab.rcParams.update(params)

plt.style.use('fivethirtyeight')

#plt.style.use('seaborn-darkgrid')

#x_results = ['Wins','Draws','Losses']
x_results = ['Overall','Home','Away']

x_indexes = np.arange(len(x_results))
width = 0.25

#y_overall = [96.7,129.2,83.9]
y_wins = [118.6,100.9,148.1]
#plt.bar(x_indexes - width, y_overall, width=0.25, color='cornflowerblue', label='Overall')
plt.bar(x_indexes - width, y_wins, width=0.25, color='cornflowerblue', label='Wins')

#y_home = [78.3,163.1,72.7]
y_draws = [89.5,80.5,98.6]
#plt.bar(x_indexes, y_home, width=0.25, color='salmon', label='Home')
plt.bar(x_indexes, y_draws, width=0.25, color='salmon', label='Draws')

#y_away = [130,91.1,91.7]
y_losses = [92.4,115.7,77.8]
#plt.bar(x_indexes + width, y_away, width=0.25, color='mediumseagreen', label='Away')
plt.bar(x_indexes + width, y_losses, width=0.25, color='mediumseagreen', label='Losses')

plt.legend()
plt.xticks(ticks=x_indexes, labels=x_results)

x_line_coordinates = [-0.5, 2.5]
y_line_coordinates = [100, 100]
plt.plot(x_line_coordinates, y_line_coordinates, color='royalblue',linestyle=(0,(1,2)))

plt.title('Roberto Hernández\nPerformance: 82%\nMatches: 40 home, 42 away')
plt.xlabel('\nWins Draws Losses\ndistribution')
plt.ylabel('Percentage')
plt.tight_layout()

plt.show()