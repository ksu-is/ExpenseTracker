from datetime import datetime
import json

def get_valid_date():
    while True:
        date_input = input("Enter the date (YYYY-MM-DD): ")
        try:
            datetime.strptime(date_input, "%Y-%m-%d")
            return date_input
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

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

def remove_expense(expenses):
    if not expenses:
        print("No expenses to remove.")
        return

    print("\nExpenses:")
    for idx, expense in enumerate(expenses, start=1):
        print(f"{idx}. Date: {expense['date']}, Amount: {expense['amount']}, Category: {expense['category']}")

    while True:
        try:
            choice = int(input("Enter the number of the expense to remove: "))
            if 1 <= choice <= len(expenses):
                removed = expenses.pop(choice - 1)
                print(f"Removed: {removed}")
                break
            else:
                print("Invalid number. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

def print_expenses(expenses):
    for expense in expenses:
        print(f'Date: {expense["date"]}, Amount: {expense["amount"]}, Category: {expense["category"]}')
    
def total_expenses(expenses):
    return sum(map(lambda expense: expense['amount'], expenses))
    
def filter_expenses_by_category(expenses, category):
    return filter(lambda expense: expense['category'].lower() == category.lower(), expenses)

def filter_expenses_by_month(expenses, year_month):
    return [expense for expense in expenses if expense['date'].startswith(year_month)]

def get_valid_year_month():
    while True:
        user_input = input("Enter year and month (YYYY-MM): ")
        try:
            datetime.strptime(user_input, "%Y-%m")
            return user_input
        except ValueError:
            print("Invalid format. Please use YYYY-MM.")

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
        print('2. Remove expenses')
        print('3. List all expenses')
        print('4. Show total expenses')
        print('5. Filter expenses by category')
        print('6. Filter expenses by month')
        print('7. Save & Exit')
       
        choice = input('Enter your choice: ')

        if choice == '1':
            date = get_valid_date()
            amount = get_valid_amount()
            category = input('Enter category: ')
            add_expense(expenses, date, amount, category)
        
        elif choice == '2':
            remove_expense(expenses)

        elif choice == '3':
            print('\nAll Expenses:')
            print_expenses(expenses)
    
        elif choice == '4':
            print('\nTotal Expenses: ', total_expenses(expenses))
    
        elif choice == '5':
            category = input('Enter category to filter: ')
            print(f'\nExpenses for {category}:')
            expenses_from_category = filter_expenses_by_category(expenses, category)
            print_expenses(expenses_from_category)
    
        elif choice == '6':
            year_month = get_valid_year_month()
            print(f'\nExpenses for {year_month}:')
            expenses_by_month = filter_expenses_by_month(expenses, year_month)
            print_expenses(expenses_by_month)

        elif choice == '7':
            save_expenses(expenses)
            print('Expenses saved. Goodbye!')
            break

        else:
            print("Invalid choice. Please enter a number 1-6.")

main()
