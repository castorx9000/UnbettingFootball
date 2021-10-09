import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os 

path = 'D:\Dropbox\La Cima del Éxito\Futbol\Ligas_csv'
files = os.listdir(path)

excel_files = [f for f in files if f[-3:] == 'xls' or f[-3:] == 'lsx']
input_data_frame = pd.DataFrame()
ouput_data_frame = pd.DataFrame()
#for file in excel_files:
#    data = pd.read_excel(file)
#    for sheet in data.sheet_names:
#        print()

data = pd.read_excel('all_euro_data_2000-2001.xls')
print(data)
#for sheet in data.sheet_names:
#    print(sheet)