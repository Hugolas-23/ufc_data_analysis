from src.data_preparation.load_data import load_processed_data
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#Fazer função para encontrar os melhores lutadores de cada estilo e etc

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

def top_fighter_by_weight_class():
    return(
        fighter_summary.sort_values(["Weight Class", "Fighter"], ascending=[True, False])
        .groupby("Weight Class")
        .head(3)
        .reset_index(drop=True)
    )

def top_by_weight_class(column):
    df_subset = fighter_summary[['Fighter', 'Weight Class', column]].copy()
    return(
        df_subset.sort_values(["Weight Class", column], ascending=[True, False])
        .groupby("Weight Class")
        .head(3)
        .reset_index(drop=True)
    )

def chance_of_kd_sub(column):
    df_subset = fighter_summary[['Fighter', 'Total Fights', column]].copy()
    df_subset['Prob ' + column] = ((df_subset[column]/df_subset['Total Fights']) * 100).round(2)
    return(
        df_subset.sort_values(column, ascending=False)
        .head(10)
        .reset_index(drop=True)
    )

def most_used_methods():
    totals = fighter_summary.groupby("Weight Class")[["KD", "SUB", "TD"]].sum().reset_index()
    return totals.sort_values("Weight Class")

if __name__ == '__main__':
    fighter_summary, men_fighter_summary, women_fighter_summary = load_processed_data()
    #correlation_kd_matrix(fighter_summary)
    #correlation_td_matrix(fighter_summary)
    #correlation_sub_matrix(fighter_summary)
    #print(top_fighter_by_weight_class())
    #print(top_by_weight_class('KD'))
    #print(top_by_weight_class('SUB'))
    #print(top_by_weight_class('TD'))
    #print(chance_of_kd_sub('KD'))
    #print(chance_of_kd_sub('SUB'))
    print(most_used_methods())
