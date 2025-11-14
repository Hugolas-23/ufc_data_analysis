from src.data_preparation.load_data import load_data
import pandas as pd
import numpy as np
def convert_time_to_seconds(new_fighter_statistics, column):
    def time_to_seconds(t):
        try:
            parts = list(map(float, t.split(':')))
            if len(parts) == 2:
                m, s = parts
                return m * 60 + s
            elif len(parts) == 3:
                h, m, s = parts
                return h * 3600 + m * 60 + s
            else:
                return None
        except:
            return None
    new_fighter_statistics['Time'] = new_fighter_statistics['Time'].astype(str).apply(time_to_seconds)
    return new_fighter_statistics

def clean_data():
    fighter_statistics = load_data()
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

    #Apenas estatísticas a partir de 2000
    new_fighter_statistics = new_fighter_statistics[new_fighter_statistics['Date'].dt.year >= 2000]

    #print(new_fighter_statistics['Date'].tail())
    #print(new_fighter_statistics.columns)
    #print(new_fighter_statistics['Time'].head())

    new_fighter_statistics = convert_time_to_seconds(new_fighter_statistics, 'Time')
    new_fighter_statistics.rename(columns={'Time': 'Time(s)'}, inplace=True)

    #print(new_fighter_statistics['Time(s)'].head())
    #print(new_fighter_statistics['Winner'].head())
    #print(new_fighter_statistics['Fighter_1_KD'].head())

    print(new_fighter_statistics.columns)
    #print(new_fighter_statistics.info())

    #Salvar arquivo limpo
    interim_path = r'data/interim/ufc_cleaned.csv'
    new_fighter_statistics.to_csv(interim_path, index=False)
    return new_fighter_statistics

