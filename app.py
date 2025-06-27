import os
file = "expenses.txt"
expenses_list = []

with open("expenses.txt") as f:
    for line in f:
        date, description, amount = [
            x.strip() for x in line.strip().split(",")]
        expenses_list.append(
            {"Date": date, "Description": description, "Amount": int(amount)})


def savefile():
    with open("expenses.txt", "w") as f:
        for item in expenses_list:
            f.write(
                f"{item['Date']}, {item['Description']}, {item['Amount']}\n")


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
        savefile()
        print("Expense added succesfully!")

    elif x == "2":
        print("Expense History: ")
        for e in expenses_list:
            print(f"{e['Date']}, {e['Description']}, {e['Amount']}")

    elif x == "3":
        print("Calculating Total Expenses...")
        total = sum(x["Amount"] for x in expenses_list)
        print("Total Expenses:", total)

    elif x == "4":
        break

    else:
        print("Invalid input. Try again.")
