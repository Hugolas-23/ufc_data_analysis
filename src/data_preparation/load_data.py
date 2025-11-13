import pandas as pd

def load_data():
    fighter_statistics = pd.read_csv(r'C:\Users\hugom\PycharmProjects\ufc_data_analysis\data\raw\ufc.csv')
    return fighter_statistics

def load_clean_data():
    return pd.read_csv(r'C:\Users\hugom\PycharmProjects\ufc_data_analysis\data\processed\ufc_cleaned.csv')



