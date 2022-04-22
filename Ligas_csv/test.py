import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os 

path = os.getcwd()
files = os.listdir(path)

files_xls = [f for f in files if f[-3:] == 'xls']
print(path)

# abrir todos los archivos de una carpeta

# abrir cada archivo con for sheet in excel_file

#   Dentro del for anterior, convertir cada sheet en un data frame
#   Dar formato al data frame 
#   1) quitar columnas sobrantes
#   2) crear columnas falantes vacías
#   3) cambiar el nombre a las columnas de los momios
#   4) guardar cada data frame como archivo de excel en otra carpeta