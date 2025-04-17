from datetime import datetime

def get_valid_date():
    while True:
        date_input = input("Enter the date (YYYY-MM-DD): ")
        try:
            datetime.strptime(date_input, "%Y-%m-%d")
            return date_input
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

import json

def save_expenses(expenses, filename="expenses.json"):
    with open(filename, 'w') as f:
        json.dump(expenses, f)

def load_expenses(filename="expenses.json"):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def add_expense(expenses, date, amount, category):
    expenses.append({'date' : date, 'amount': amount, 'category': category})
    
def print_expenses(expenses):
    for expense in expenses:
        print(f'Date: {expense["date"]}, Amount: {expense["amount"]}, Category: {expense["category"]}')
    
def total_expenses(expenses):
    return sum(map(lambda expense: expense['amount'], expenses))
    
def filter_expenses_by_category(expenses, category):
    return filter(lambda expense: expense['category'].lower() == category.lower(), expenses)

def filter_expenses_by_month(expenses, year_month):
    return [expense for expense in expenses if expense['date'].startswith(year_month)]

def get_valid_amount():
    while True:
        try:
            return float(input('Enter amount: '))
        except ValueError:
            print("Please enter a valid number.")
    

def main():
    expenses = load_expenses() 
    while True:
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Filter expenses by month')
        print('6. Save & Exit')
       
        choice = input('Enter your choice: ')

        if choice == '1':
            date = get_valid_date()
            amount = get_valid_amount()
            category = input('Enter category: ')
            add_expense(expenses, date, amount, category)

        elif choice == '2':
            print('\nAll Expenses:')
            print_expenses(expenses)
    
        elif choice == '3':
            print('\nTotal Expenses: ', total_expenses(expenses))
    
        elif choice == '4':
            category = input('Enter category to filter: ')
            print(f'\nExpenses for {category}:')
            expenses_from_category = filter_expenses_by_category(expenses, category)
            print_expenses(expenses_from_category)
    
        elif choice == '5':
            year_month = input('Enter year and month (YYYY-MM): ')
            print(f'\nExpenses for {year_month}:')
            expenses_by_month = filter_expenses_by_month(expenses, year_month)
            print_expenses(expenses_by_month)

        elif choice == '6':
            save_expenses(expenses)
            print('Expenses saved. Goodbye!')
            break

        else:
            print("Invalid choice. Please enter a number 1-6.")

main()
