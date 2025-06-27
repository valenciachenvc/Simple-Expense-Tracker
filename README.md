Description
----------------------------------------------------
This project helps users keep track of their daily expenses. Users can add new expenses, view their expense history, and calculate the total expenses. The data will be stored in a text file for persistence.


Main Features
----------------------------------------------------
1. Add an Expense
    - Input: Date, Description, and Amount.
    - The data is saved to a file (expenses.txt).
2. View Expense History
    - Displays a list of all expenses from the file.
3. Calculate Total Expenses
    - Sums up all expense amounts and displays the total.
4. Exit
    - Exits the program.


File Format
----------------------------------------------------
The data is stored in a file named expenses.txt.
Each line in the file represents an expense in the following format: Date, Description, Amount
- 2024-12-20, Lunch, 50
- 2024-12-20, Groceries, 150


Implementation Steps
----------------------------------------------------
1. Create the Main Menu
    The program starts by showing the following options:
    - 1: Add Expense
    - 2: View Expenses
    - 3: Calculate Total Expenses
    - 4: Exit
2. Add Expense
    - Prompt the user to input the date, description, and amount of the expense.
    - Append this data to expenses.txt.
3. View Expenses
    - Read the file expenses.txt.
    - Display the list of expenses.
4. Calculate Total Expenses
    - Read the file expenses.txt.
    - Sum up the amounts and display the total.
5. Exit
    - Stop the program.
