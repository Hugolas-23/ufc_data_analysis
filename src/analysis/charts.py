from src.data_preparation.load_data import load_processed_data
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

fighter_summary, men_fighter_summary, women_fighter_summary = load_processed_data()
#distribuição de vitórias
def win_distribution():
    plt.figure(figsize=(10, 5))
    sns.histplot(fighter_summary['Total Wins'], bins=30)
    plt.title("Distribuição de Vitórias")
    plt.xlabel("Vitórias")
    plt.ylabel("Número de Lutadores")
    plt.show()

#distribuição de peso masculino
def men_weight_destribution():
    plt.figure(figsize=(12,6))
    men_fighter_summary['Weight Class'].value_counts().plot(kind='bar')
    plt.title("Quantidade de Lutadores por Categoria de Peso")
    plt.xlabel("Categoria")
    plt.ylabel("Total")
    plt.tight_layout()
    plt.show()

#distribuição de peso feminina
def women_weight_destribution():
    plt.figure(figsize=(12, 6))
    women_fighter_summary['Weight Class'].value_counts().plot(kind='bar')
    plt.title("Quantidade de Lutadoras por Categoria de Peso")
    plt.xlabel("Categoria")
    plt.ylabel("Total")
    plt.tight_layout()
    plt.show()

#distribuição de lutas por lutador
def fights_distribution():
    plt.figure(figsize=(12, 6))
    sns.histplot(fighter_summary['Total Fights'], bins=100)
    plt.title("Distribuição de lutas por lutador")
    plt.xlabel("Lutas")
    plt.ylabel("Número de lutadores")
    plt.xticks(np.arange(0, fighter_summary['Total Fights'].max()+1, 1))
    plt.show()

#distribuição de Knockdowns por lutador
def knockdown_distribution():
    plt.figure(figsize=(12, 6))
    sns.histplot(fighter_summary['KD'], bins=100)
    plt.title("Distribuição de knockdowns por lutador")
    plt.xlabel("KD")
    plt.ylabel("Número de lutadores")
    plt.xticks(np.arange(0, fighter_summary['KD'].max() + 1, 1))
    plt.tight_layout()
    plt.show()

#distribuição de submissions por lutador
def submission_distribution():
    plt.figure(figsize=(12, 6))
    sns.histplot(fighter_summary['SUB'], bins=100)
    plt.title("Distribuição de knockdowns por lutador")
    plt.xlabel("SUB")
    plt.ylabel("Número de lutadores")
    plt.xticks(np.arange(0, fighter_summary['SUB'].max() + 1, 1))
    plt.tight_layout()
    plt.show()

#distribuição de takedowns por lutador
def takedown_distribution():
    plt.figure(figsize=(12, 6))
    sns.histplot(fighter_summary['TD'], bins=100)
    plt.title("Distribuição de knockdowns por lutador")
    plt.xlabel("TD")
    plt.ylabel("Número de lutadores")
    plt.xticks(np.arange(0, fighter_summary['TD'].max() + 1, 10))
    plt.tight_layout()
    plt.show()





if __name__ == '__main__':
    fighter_summary, men_fighter_summary, women_fighter_summary = load_processed_data()
    #fights_distribution()
    #knockdown_distribution()
    #submission_distribution()
    takedown_distribution()