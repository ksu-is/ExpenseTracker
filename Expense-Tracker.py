from datetime import datetime
import json

def get_valid_date(): # Prompts the user to enter a valid date in the YYYY-MM-DD format. Repeats until the correct format is entered.
    while True:
        date_input = input("Enter the date (YYYY-MM-DD) or type 'cancel' to go back: ")
        if date_input.lower() == 'cancel':
            return None
        try:
            datetime.strptime(date_input, "%Y-%m-%d")
            return date_input
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

def save_expenses(expenses, filename="expenses.json"): # Saves the list of expenses to a specified JSON file.

    with open(filename, 'w') as f:
        json.dump(expenses, f)

def load_expenses(filename="expenses.json"): # Loads expenses from a specified JSON file and returns an empty list if the file does not exist or is empty.
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def add_expense(expenses, date, amount, category): # Adds a new expense to the list.
    expenses.append({'date' : date, 'amount': amount, 'category': category})

def remove_expense(expenses): # Lists expenses with an index and promts the user to choose the index number of the expense they want to remove from the list.
    if not expenses:
        print("No expenses to remove.")
        return

    print("\nExpenses:")
    for idx, expense in enumerate(expenses, start=1):
        print(f"{idx}. Date: {expense['date']}, Amount: {expense['amount']}, Category: {expense['category']}")

    while True:
        choice = input("Enter the number of the expense to remove or type 'cancel' to go back: ")
        if choice.lower() == 'cancel':
            print("Cancelled.")
            return
        try:
            choice = int(choice)
            if 1 <= choice <= len(expenses):
                removed = expenses.pop(choice - 1)
                print(f"Removed: {removed}")
                break
            else:
                print("Invalid number. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

def print_expenses(expenses): # Prints all expenses in a list format.
    for expense in expenses:
        print(f'Date: {expense["date"]}, Amount: ${expense["amount"]:.2f}, Category: {expense["category"]}')
    
def total_expenses(expenses): # Calculates the dollar amount of all expenses combined.
    total = sum(expense['amount'] for expense in expenses)
    return f"${total:.2f}"
    
def filter_expenses_by_category(expenses, category): # Allows the user to filter expenses by a specific category.
    return filter(lambda expense: expense['category'].lower() == category.lower(), expenses)

def list_categories(expenses): # Prints a list of all categories used by the user.
    categories = {expense['category'].lower() for expense in expenses}
    return sorted(categories)

def filter_expenses_by_month(expenses, year_month): # Allows the user to filter expenses by a specific month in a year.
    return [expense for expense in expenses if expense['date'].startswith(year_month)]

def get_valid_year_month(): # Prompts the user to enter a valid year and month in YYYY-MM format.
    while True:
        user_month_input = input("Enter year and month (YYYY-MM) or type 'cancel' to go back: ")
        if user_month_input.lower() == 'cancel':
            return None
        try:
            datetime.strptime(user_month_input, "%Y-%m")
            return user_month_input
        except ValueError:
            print("Invalid format. Please use YYYY-MM.")

def filter_expenses_by_year(expenses, year): # Allows the user to filter expenses by a specific year.
    return [expense for expense in expenses if expense['date'].startswith(year)]

def get_valid_year(): # Prompts the user to enter a valid year in YYYY format.
    while True:
        user_year_input = input("Enter year (YYYY) or type 'cancel' to go back: ")
        if user_year_input.lower() == 'cancel':
            return None
        try:
            datetime.strptime(user_year_input, "%Y")
            return user_year_input
        except ValueError:
            print("Invalid format. Please use YYYY.")

def get_valid_amount(): # Prompts the user to enter a valid amount and allows decimal numbers.
    while True:
        amount_input = input("Enter amount or type 'cancel' to go back: ")
        if amount_input.lower() == 'cancel':
            return None
        try:
            return float(amount_input)
        except ValueError:
            print("Please enter a valid number.")
    

def main(): # Main function to run the expense tracker application.
    expenses = load_expenses() 
    while True:
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. Remove an expense')
        print('3. List all expenses')
        print('4. List all categories')
        print('5. Show total expenses')
        print('6. Filter expenses by category')
        print('7. Filter expenses by month')
        print('8. Filter expenses by year')
        print('9. Save & Exit')
       
        choice = input('Enter your choice: ')

        if choice == '1':
            date = get_valid_date()
            if date is None:
                print ("Cancelled.")
                continue
            amount = get_valid_amount()
            if amount is None:
                print("Cancelled.")
            category = input('Enter category or type "cancel": ')
            if category.lower() == 'cancel':
                print("Cancelled.")
                continue
            add_expense(expenses, date, amount, category)
        
        elif choice == '2':
            remove_expense(expenses)

        elif choice == '3':
            print('\nAll Expenses:')
            print_expenses(expenses)
        
        elif choice == '4':
            print('\nAll Categories:')
            categories = list_categories(expenses)
            if categories:
                for category in categories:
                    print(category)
            else:
                print("No categories found.")
    
        elif choice == '5':
            print('\nTotal Expenses: ', total_expenses(expenses))
    
        elif choice == '6':
            category = input('Enter category to filter (or type "cancel" to go back): ')
            if category.lower() == 'cancel':
                print("Cancelled.")
                continue
            print(f'\nExpenses for {category}:')
            expenses_from_category = filter_expenses_by_category(expenses, category)
            print_expenses(expenses_from_category)
    
        elif choice == '7':
            year_month = get_valid_year_month()
            if year_month is None:
                print("Cancelled.")
                continue
            print(f'\nExpenses for {year_month}:')
            expenses_by_month = filter_expenses_by_month(expenses, year_month)
            print_expenses(expenses_by_month)

        elif choice == '8':
            year = get_valid_year()
            if year is None:
                print("Cancelled.")
                continue
            print(f'\nExpenses for {year}:')
            expenses_by_year = filter_expenses_by_year(expenses, year)
            print_expenses(expenses_by_year)

        elif choice == '9':
            save_expenses(expenses)
            print('Expenses saved. Goodbye!')
            break

        else:
            print("Invalid choice. Please enter a number 1-9.")

main()
