import pandas as pd

def load_data():
    fighter_statistics = pd.read_csv(r'C:\Users\hugom\PycharmProjects\ufc_data_analysis\data\raw\ufc.csv')
    return fighter_statistics

def load_clean_data():
    return pd.read_csv(r'C:\Users\hugom\PycharmProjects\ufc_data_analysis\data\interim\ufc_cleaned.csv')

def load_processed_data():
    fighter_summary = pd.read_csv(r'C:\Users\hugom\PycharmProjects\ufc_data_analysis\data\processed\fighter_summary.csv')
    men_fighter_summary = pd.read_csv(r'C:\Users\hugom\PycharmProjects\ufc_data_analysis\data\processed\men_fighter_summary.csv')
    women_fighter_summary = pd.read_csv(r'C:\Users\hugom\PycharmProjects\ufc_data_analysis\data\processed\women_fighter_summary.csv')
    return fighter_summary, men_fighter_summary, women_fighter_summary



