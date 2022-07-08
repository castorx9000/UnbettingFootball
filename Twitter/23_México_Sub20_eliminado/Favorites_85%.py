from nis import match
import numpy as np
import pandas as pd

if __name__ == '__main__':
    
    range = '70-74'
    matches = pd.read_excel('df_matches.xlsx')
    matches = matches[((matches['OddH'] <= 1.35) & (matches['OddH'] >= 1.26)) | ((matches['OddA'] <= 1.35) & (matches['OddA'] >= 1.26))]
    print(matches)
    matches.to_excel(f'Favorites_{range}.xlsx', encoding='utf-8', index=True)