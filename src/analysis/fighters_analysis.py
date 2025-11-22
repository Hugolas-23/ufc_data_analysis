from src.data_preparation.load_data import load_processed_data
import matplotlib.pyplot as plt
import seaborn as sns


fighter_summary, men_fighter_summary, women_fighter_summary = load_processed_data()

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


def top_fighter_by_weight_class(column):
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


def method_percentage_by_weight():
    totals = fighter_summary.groupby("Weight Class")[["KD", "SUB", "TD"]].sum()
    totals['Total Actions'] = totals.sum(axis=1)

    percentages = totals.div(totals['Total Actions'], axis=0)[['KD', 'SUB', 'TD']] * 100
    return percentages.round(2)




