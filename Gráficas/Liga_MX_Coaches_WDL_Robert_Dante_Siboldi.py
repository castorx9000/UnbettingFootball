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

x_results = ['Overall','Home','Away']

x_indexes = np.arange(len(x_results))
width = 0.25

y_wins = [96.2,111.3,72.7]
plt.bar(x_indexes - width, y_wins, width=0.25, color='cornflowerblue', label='Wins')

y_draws = [110.1,89,129.8]
plt.bar(x_indexes, y_draws, width=0.25, color='salmon', label='Draws')

y_losses = [96.6,92.4,98.9]
plt.bar(x_indexes + width, y_losses, width=0.25, color='mediumseagreen', label='Losses')

plt.legend()
plt.xticks(ticks=x_indexes, labels=x_results)

x_line_coordinates = [-0.5, 2.5]
y_line_coordinates = [100, 100]
plt.plot(x_line_coordinates, y_line_coordinates, color='royalblue',linestyle=(0,(1,2)))

plt.title('Robert Dante Siboldi\nPerformance: 98.9%\nMatches: 38 home, 41 away')
plt.xlabel('\nWins Draws Losses\ndistribution')
plt.ylabel('Percentage')
plt.tight_layout()

plt.show()