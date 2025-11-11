import pandas as pd
import numpy as np
from src.data_preparation.clean_data import clean_data


def transform_data():
       pd.set_option('display.max_columns', None)
       new_fighter_statistics = clean_data()

       f1 = new_fighter_statistics[['Fighter 1', 'Fighter_1_KD', 'Fighter_1_STR', 'Fighter_1_TD', 'Fighter_1_SUB',
                                    'Round', 'Time(s)', 'Weight_Class']].copy()
       f2 = new_fighter_statistics[['Fighter 2', 'Fighter_2_KD', 'Fighter_2_STR', 'Fighter_2_TD', 'Fighter_2_SUB',
                                    'Round', 'Time(s)', 'Weight_Class']].copy()

       f1.columns = ['Fighter', 'KD', 'STR', 'TD', 'SUB', 'Total_Rounds', 'Total_Time(s)', 'Weight_Class']
       f2.columns = ['Fighter', 'KD', 'STR', 'TD', 'SUB', 'Total_Rounds', 'Total_Time(s)', 'Weight_Class']

       combined = pd.concat([f1, f2], ignore_index=True)

       fighter_summary = (
              combined
              .groupby('Fighter', as_index=False)
              .agg({
                     'KD': 'sum',
                     'STR': 'sum',
                     'TD': 'sum',
                     'SUB': 'sum',
                     'Total_Rounds': 'sum',
                     'Total_Time(s)': 'sum',
                     'Weight_Class': 'first'
              })
       )

       print(fighter_summary.tail())

       women_fighter_summary = fighter_summary[fighter_summary['Weight_Class'].str.contains('Women', na=False)]

       men_fighter_summary = fighter_summary[~fighter_summary['Weight_Class'].str.contains('Women', na=False)]

       print(women_fighter_summary.head())
       print(men_fighter_summary.head())

if __name__ == '__main__':
    transform_data()