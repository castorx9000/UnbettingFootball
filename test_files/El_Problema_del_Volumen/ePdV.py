import numpy as np
import pandas as pd
import math

population = np.random.randn(1000000)
population = np.sort(population)

below_96 = np.count_nonzero(population < 1.751) 
best_04_00 = np.count_nonzero(population >= 1.751)
best_01_00 = np.count_nonzero(population >= 2.332)
best_00_05 = np.count_nonzero(population >= 2.573)
best_00_01 = np.count_nonzero(population >= 3.7)

print(f'Distribución de la Población con {len(population)} personas:\n')
print(f'Below 96%: {below_96}, {np.round_(below_96 / len(population) *100,2)} %')
print(f'Best 4.00%: {best_04_00}, {np.round_(best_04_00 / len(population) *100,4)} %')
print(f'Best 1.00%: {best_01_00}, {np.round_(best_01_00 / len(population) *100,4)} %')
print(f'Best 0.05%: {best_00_05}, {np.round_(best_00_05 / len(population) *100,4)} %')
print(f'Best 0.01%: {best_00_01}, {np.round_(best_00_01 / len(population) *100,4)} %')

print(f'\n')

population_2 = np.random.rand(100000)

below_96 = np.count_nonzero(population_2 < 0.96) 
best_04_00 = np.count_nonzero(population_2 >= 0.96)
best_01_00 = np.count_nonzero(population_2 >= 0.99)
best_00_05 = np.count_nonzero(population_2 >= 0.9995)
best_00_01 = np.count_nonzero(population_2 >= 0.9999)

print(f'Distribución de la Población con {len(population_2)} personas:\n')
print(f'Below 96%: {below_96}, {np.round_(below_96 / len(population_2) *100,2)} %')
print(f'Best 4.00%: {best_04_00}, {np.round_(best_04_00 / len(population_2) *100,4)} %')
print(f'Best 1.00%: {best_01_00}, {np.round_(best_01_00 / len(population_2) *100,4)} %')
print(f'Best 0.05%: {best_00_05}, {np.round_(best_00_05 / len(population_2) *100,4)} %')
print(f'Best 0.01%: {best_00_01}, {np.round_(best_00_01 / len(population_2) *100,4)} %')

Messi = 1 / 265000000
print(f'\nP(Messi)={Messi}')