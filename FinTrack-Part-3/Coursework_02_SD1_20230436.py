import json
from datetime import datetime
import sys
import Coursework_03_SD1_20230436

# Global dictionary for storing transactions
transactions = {}

# Functions for file handling
def load_transactions():
    global transactions
    try:
        with open('transactions.json', 'r') as file:
            transactions = json.load(file)
    except FileNotFoundError:
        transactions = {}

def save_transactions():
    with open('transactions.json', 'w') as file:
        json.dump(transactions, file, indent=4)

def read_bulk_transactions(file_name):
    global transactions
    try:
        with open(file_name, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 3:
                    category, amount, date = map(str.strip, parts)
                    category = category.capitalize()
                    amount = float(amount)
                    transactions.setdefault(category, []).append({"Amount": amount, "Date": date})
                else:
                    print("Invalid format in line:", line)
            print("Bulk transactions added successfully.")
            save_transactions()
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")

# Function for adding a single transaction
def add_transactions():
    while True:
        category = input("\nEnter transaction category: ").capitalize()
        while True:
            try:
                amount = float(input("Enter the amount: "))
                break
            except ValueError:
                print("Invalid amount. Please enter a valid number.")
        while True:
            try:
                date = input(f"Enter the date for {category} (YYYY-MM-DD): ")
                datetime.strptime(date, "%Y-%m-%d")
                break
            except ValueError:
                print("Invalid date format. Please enter as YYYY-MM-DD.")
        transactions.setdefault(category, []).append({"Amount": amount, "Date": date})
        choice = input("Do you want to add more transactions? (Y/N): ").upper()
        if choice != "Y":
            break
    print("\nTransaction added successfully!")
    save_transactions()

# Function for viewing all transactions
def view_transactions():
    if not transactions:
        print("No transactions found.")
    else:
        for category, details in transactions.items():
            print(f"\nCategory: {category}")
            for idx, trans in enumerate(details, start=1):
                print(f"{idx}. Amount: {trans['Amount']}, Date: {trans['Date']}")

# Function for updating a transaction
def update_transactions():
    view_transactions()
    if not transactions:
        return
    while True:
        category = input("\nEnter the transaction category to update: ").capitalize()
        if category in transactions:
            print(f"{category} transactions: {transactions[category]}")
            break
        else:
            print("No transactions found for this category.")
    while True:
        field = input("\nEnter the field to update (Amount/Date): ").capitalize()
        if field in ["Amount", "Date"]:
            idx = int(input("Enter the index of the transaction to update: "))
            if 0 < idx <= len(transactions[category]):
                new_value = input(f"Enter the new {field}: ")
                transactions[category][idx - 1][field] = new_value
                print(f"{field} updated successfully!")
                break
            else:
                print("Invalid transaction index.")
        else:
            print("Invalid field. Please enter 'Amount' or 'Date'.")

# Function for deleting a transaction
def delete_transactions():
    view_transactions()
    if not transactions:
        return
    while True:
        category = input("Enter the transaction category to delete from: ").capitalize()
        if category in transactions:
            print(f"{category} transactions: {transactions[category]}")
            break
        else:
            print("No transactions found for this category.")
    while True:
        idx = int(input("Enter the index of the transaction to delete: "))
        if 0 < idx <= len(transactions[category]):
            transactions[category].pop(idx - 1)
            print("Transaction deleted successfully!")
            break
        else:
            print("Invalid transaction index.")

# Function for displaying a summary
def display_summary():
    view_transactions()
    max_amount = 0
    for category, details in transactions.items():
        for trans in details:
            if trans["Amount"] > max_amount:
                max_amount = trans["Amount"]
    print("\nThe total of the expenses are: ", max_amount)

# Main menu function
def main_menu():
    load_transactions()
    while True:
        print("\nPersonal Finance Tracker")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Update Transactions")
        print("4. Delete Transactions")
        print("5. Read Bulk Transactions")
        print("6. Display Summary")
        print("7. Open GUI")
        print("8. Exit")
        choice = input("\nEnter your choice: ")
        if choice == '1':
            add_transactions()
        elif choice == '2':
            view_transactions()
        elif choice == '3':
            update_transactions()
        elif choice == '4':
            delete_transactions()
        elif choice == '5':
            file_name = input("Enter the file name to read bulk transactions from: ")
            read_bulk_transactions(file_name)
        elif choice == '6':
            display_summary()
        elif choice == '7':
            Coursework_03_SD1_20230436.main()
        elif choice == '8':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
