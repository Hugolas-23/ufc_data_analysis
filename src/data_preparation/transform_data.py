import pandas as pd
import numpy as np
from src.data_preparation.load_data import load_clean_data


def transform_data():
       pd.set_option('display.max_columns', None)
       new_fighter_statistics = load_clean_data()

       # Total de vitórias
       new_fighter_statistics['Win_F1'] = new_fighter_statistics.apply(
              lambda row: 1 if row['Winner'] == row['Fighter 1'] else 0, axis=1
       )

       new_fighter_statistics['Win_F2'] = new_fighter_statistics.apply(
              lambda row: 1 if row['Winner'] == row['Fighter 2'] else 0, axis=1
       )

       # Total de lutas
       f1_count = new_fighter_statistics['Fighter 1'].value_counts().reset_index()
       f1_count.columns = ['Fighter', 'Total Fights']

       f2_count = new_fighter_statistics['Fighter 2'].value_counts().reset_index()
       f2_count.columns = ['Fighter', 'Total Fights']

       combined1 = pd.concat([f1_count, f2_count], ignore_index=True)
       total_fights = (
              combined1
              .groupby('Fighter', as_index=False)['Total Fights'].sum()
       )

       f1 = new_fighter_statistics[['Fighter 1', 'Fighter_1_KD', 'Fighter_1_STR', 'Fighter_1_TD', 'Fighter_1_SUB', 'Weight_Class', 'Win_F1']].copy()
       f2 = new_fighter_statistics[['Fighter 2', 'Fighter_2_KD', 'Fighter_2_STR', 'Fighter_2_TD', 'Fighter_2_SUB', 'Weight_Class', 'Win_F2']].copy()

       #Estatísticas de desempenho dos lutadores e divisão entre masculino e feminino
       f1.columns = ['Fighter', 'KD', 'STR', 'TD', 'SUB', 'Weight Class', 'Total Wins']
       f2.columns = ['Fighter', 'KD', 'STR', 'TD', 'SUB', 'Weight Class', 'Total Wins']

       combined = pd.concat([f1, f2], ignore_index=True)

       fighter_summary = (
              combined
              .groupby('Fighter', as_index=False)
              .agg({
                     'KD': 'sum',
                     'STR': 'sum',
                     'TD': 'sum',
                     'SUB': 'sum',
                     'Weight Class': 'first',
                     'Total Wins': 'sum'
              })
              .sort_values('Total Wins', ascending=False)
       )

       fighter_summary = total_fights.merge(fighter_summary, on='Fighter', how='left')

       #print(fighter_summary.tail())

       women_fighter_summary = fighter_summary[fighter_summary['Weight Class'].str.contains('Women', na=False)]

       men_fighter_summary = fighter_summary[~fighter_summary['Weight Class'].str.contains('Women', na=False)]

       #print(fighter_summary.head())
       #print(women_fighter_summary.head())
       #print(men_fighter_summary.head())

       fighter_summary.to_csv('data/processed/fighter_summary.csv', index=False)
       women_fighter_summary.to_csv('data/processed/women_fighter_summary.csv', index=False)
       men_fighter_summary.to_csv('data/processed/men_fighter_summary.csv', index=False)
