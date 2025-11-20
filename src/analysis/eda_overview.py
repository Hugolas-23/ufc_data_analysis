import pandas as pd
import matplotlib.pyplot as plt
from src.data_preparation.load_data import load_processed_data

def eda_overview():
    fighter_summary, men_fighter_summary, women_fighter_summary = load_processed_data()
    print("-------DATASETS OVERVIEW-------")

    print("-------General Fighter Summary-------")
    print(fighter_summary.columns)
    print(fighter_summary.head())
    print(fighter_summary.info())
    print("-------Missing Values-------")
    print(fighter_summary.isna().sum())
    print("-------Duplicated Values-------")
    print(fighter_summary.duplicated().sum)
    print("-------Initial Statistics-------")
    print(fighter_summary.describe())

    print("-------Men Fighter Summary-------")
    print(men_fighter_summary.columns)
    print(men_fighter_summary.head())
    print(men_fighter_summary.info())
    print(men_fighter_summary.describe())

    print("-------Women Fighter Summary-------")
    print(women_fighter_summary.columns)
    print(women_fighter_summary.head())
    print(women_fighter_summary.info())
    print(women_fighter_summary.describe())

