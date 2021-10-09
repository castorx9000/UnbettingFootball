import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.pylab as pylab
params = {'legend.fontsize': 22,
          'figure.figsize': (14.5, 9.5),
         'axes.labelsize': 'x-large',
         'axes.titlesize':60,
         'xtick.labelsize':'x-large',
         'ytick.labelsize':'large',
         'legend.loc':'right'}
pylab.rcParams.update(params)

plt.style.use('fivethirtyeight')

x_results = ['Overall','Home','Away']

x_indexes = np.arange(len(x_results))
width = 0.25

y_s_goals = [108.4,109,107.6]
plt.bar(x_indexes - width/2, y_s_goals, width=0.25, color='royalblue', label='Scored')

y_c_goals = [100.4,105.4,96.5]
plt.bar(x_indexes + width/2, y_c_goals, width=0.25, color='indianred', label='Conceided')

plt.legend()
plt.xticks(ticks=x_indexes, labels=x_results)

x_line_coordinates = [-0.5, 2.5]
y_line_coordinates = [100, 100]
plt.plot(x_line_coordinates, y_line_coordinates, color='darkgrey',linestyle=(0,(5,1)))

plt.title('Quique Septien\nPerformance: 113.8%\nMatches: 58 home, 56 away')
plt.xlabel('\nExpected Scored Goals / Expected Conceided Goals')
plt.ylabel('Percentage')
plt.tight_layout()

plt.show()