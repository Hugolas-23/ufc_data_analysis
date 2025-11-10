from load_data import fighter_statistics
import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None)
#print(fighter_statistics.info())
#print(fighter_statistics.isna().sum())
#print(fighter_statistics.duplicated().sum())
new_fighter_statistics = fighter_statistics.copy()
new_fighter_statistics.dropna()
#print(new_fighter_statistics['Date'].head())
new_fighter_statistics['Date'] = pd.to_datetime(new_fighter_statistics['Date'], format='%d-%b-%y', errors='coerce')
#print(new_fighter_statistics['Date'].head())
#print(new_fighter_statistics.info())
new_fighter_statistics = new_fighter_statistics[new_fighter_statistics['Date'].dt.year >= 2000]
#print(new_fighter_statistics['Date'].tail())
print(new_fighter_statistics.columns)
#print(new_fighter_statistics['Time'].head())
#new_fighter_statistics['Time'] = pd.to_datetime(new_fighter_statistics['Time'], format='%H:%M:%S')
#new_fighter_statistics['Time'] = new_fighter_statistics['Time'].apply(lambda x: str(x).split()[-1])
print(new_fighter_statistics['Time'].head())
print(new_fighter_statistics.info())
