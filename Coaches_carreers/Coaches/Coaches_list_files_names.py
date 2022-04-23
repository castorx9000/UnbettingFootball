import os
import numpy as np


coaches_list = []

for file in os.listdir():
    if file.endswith('.xlsx'):
        coaches_list.append(file)

np.savetxt('Coaches_list.csv', coaches_list, delimiter=', ', fmt='% s')