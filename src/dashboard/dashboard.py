from src.visualization.charts import *
from src.analysis.fighters_analysis import *
from src.analysis.eda_overview import eda_overview


def menu():
    print("\n===== UFC DASHBOARD =====")
    print("1 - Win Distribution")
    print("2 - Men Weight Distribution")
    print("3 - Women Weight Distribution")
    print("4 - Fights Distribution")
    print("5 - Knockdowns Distribution (KD)")
    print("6 - Submissions Distribution (SUB)")
    print("7 - Takedowns Distribution (TD)")
    print("8 - Total Fights by Weight Class")
    print("9 - Total KDs by Weight Class")
    print("10 - Total SUBs by Weight Class")
    print("11 - Total TDs by Weight Class")
    print("12 - Correlation KD Matrix")
    print("13 - Correlation TD Matrix")
    print("14 - Correlation SUB Matrix")
    print("15 - Top 3 Fighters by Weight Class")
    print("16 - Chance of KD or SUB by Fighter")
    print("17 - Most Utilized Method by Weight")
    print("18 - EDA Overview")
    print("0 - Exit")


def dashboard():
    while True:
        menu()
        choice = int(input("\nSelecione uma opção: "))
        if choice == 1:
            win_distribution()

        elif choice == 2:
            men_weight_destribution()

        elif choice == 3:
            women_weight_destribution()

        elif choice == 4:
            fights_distribution()

        elif choice == 5:
            knockdown_distribution()

        elif choice == 6:
            submission_distribution()

        elif choice == 7:
            takedown_distribution()

        elif choice == 8:
            total_fights_by_weight_class()

        elif choice == 9:
            total_kd_by_weight_class()

        elif choice == 10:
            total_sub_by_weight_class()

        elif choice == 11:
            total_td_by_weight_class()

        elif choice == 12:
            df = input("Which dataframe do you want to use? (fighter_summary/men_fighter_summary/women_fighter_summary)")
            correlation_kd_matrix(df)

        elif choice == 13:
            df = input("Which dataframe do you want to use? (fighter_summary/men_fighter_summary/women_fighter_summary)")
            correlation_td_matrix(df)

        elif choice == 14:
            df = input("Which dataframe do you want to use? (fighter_summary/men_fighter_summary/women_fighter_summary)")
            correlation_sub_matrix(df)

        elif choice == 15:
            method = input("Which method do you want to analyze? (KD/SUB/TD)")
            print(top_fighter_by_weight_class(method))

        elif choice == 16:
            method = input("Which method do you want to analyze? (KD/SUB)")
            print(chance_of_kd_sub(method))

        elif choice == 17:
            print(method_percentage_by_weight())

        elif choice == 18:
            eda_overview()

        elif choice == 0:
            print("END")
            break

        else:
            print("Invalid option! Try again.")
