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

       f1 = new_fighter_statistics[['Fighter 1', 'Fighter_1_KD', 'Fighter_1_STR', 'Fighter_1_TD', 'Fighter_1_SUB', 'Weight_Class', 'Win_F1']].copy()
       f2 = new_fighter_statistics[['Fighter 2', 'Fighter_2_KD', 'Fighter_2_STR', 'Fighter_2_TD', 'Fighter_2_SUB', 'Weight_Class', 'Win_F2']].copy()

       #Estatísticas de desempenho dos lutadores e divisão entre masculino e feminino
       f1.columns = ['Fighter', 'KD', 'STR', 'TD', 'SUB', 'Weight_Class', 'Total_wins']
       f2.columns = ['Fighter', 'KD', 'STR', 'TD', 'SUB', 'Weight_Class', 'Total_wins']

       combined = pd.concat([f1, f2], ignore_index=True)

       fighter_summary = (
              combined
              .groupby('Fighter', as_index=False)
              .agg({
                     'KD': 'sum',
                     'STR': 'sum',
                     'TD': 'sum',
                     'SUB': 'sum',
                     'Weight_Class': 'first',
                     'Total_wins': 'sum'
              })
              .sort_values('Total_wins', ascending=False)
       )

       #print(fighter_summary.tail())

       women_fighter_summary = fighter_summary[fighter_summary['Weight_Class'].str.contains('Women', na=False)]

       men_fighter_summary = fighter_summary[~fighter_summary['Weight_Class'].str.contains('Women', na=False)]

       print(fighter_summary.head())
       print(women_fighter_summary.head())
       print(men_fighter_summary.head())

       #Total de vitórias




if __name__ == '__main__':
       transform_data()