import os
file = "expenses.txt"
expenses_list = [
    {"Date": "2024-12-20", "Description": "Lunch", "Amount": 50}
]


while True:
    print("""
Simple Expense Tracker
1: Add Expense
2: View Expenses
3: Calculate Total Expenses
4: Exit """)
    x = input("Choose an option: ")

    if x == "1":
        date = input("Enter the date (YYYY-MM-DD): ")
        description = input("Enter the description: ")
        amount = int(input("Enter the amount: "))
        new_expense = {"Date": date,
                       "Description": description,
                       "Amount": amount}
        expenses_list.append(new_expense)
        print("Expense added succesfully!")

    elif x == "2":
        print("Expense History: ")
        f = open(file)
        print(f.read())

    elif x == "3":
        print("Calculating Total Expenses...")
        total = sum(x["Amount"] for x in expenses_list)
        print("Total Expenses:", total)

    elif x == "4":
        break

    else:
        print("Invalid input. Try again.")
