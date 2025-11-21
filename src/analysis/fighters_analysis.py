from src.data_preparation.load_data import load_processed_data
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def correlation_kd_matrix(df):
    plt.figure(figsize=(10, 8))
    sns.heatmap(df[['KD', 'STR', 'Total Fights', 'Total Wins']].corr(),
                annot=True, cmap="coolwarm")
    plt.title("Correlação entre estatísticas de luta")
    plt.show()

def correlation_td_matrix(df):
    plt.figure(figsize=(10, 8))
    sns.heatmap(df[['TD', 'STR', 'Total Fights', 'Total Wins']].corr(),
                annot=True, cmap="coolwarm")
    plt.title("Correlação entre estatísticas de luta")
    plt.show()

def correlation_sub_matrix(df):
    plt.figure(figsize=(10, 8))
    sns.heatmap(df[['SUB', 'STR', 'Total Fights', 'Total Wins']].corr(),
                annot=True, cmap="coolwarm")
    plt.title("Correlação entre estatísticas de luta")
    plt.show()

if __name__ == '__main__':
    fighter_summary, men_fighter_summary, women_fighter_summary = load_processed_data()
    #correlation_kd_matrix(fighter_summary)
    #correlation_td_matrix(fighter_summary)
    correlation_sub_matrix(fighter_summary)
