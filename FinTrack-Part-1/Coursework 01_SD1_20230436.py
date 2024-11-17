import json
import datetime

# Global list to store transactions
transactions = []

# File handling functions
def load_transactions():
    pass

def save_transactions():
    with open('transactions.json', 'w') as file:  
        json.dump(transactions, file)
        
""" dump() function to convert the Python objects into their respective JSON object,  
so it makes it easy to write data to files. See the following table given below """

# Feature implementations
def add_transaction():
    try:
      amount = float(input("Enter amount: "))
      category = input("Enter category: ")
      while True:
          transaction_type = input("Enter type (Income/Expense): ").capitalize()
          if transaction_type in ["Income","Expense"]:
              break
          else:
              print("Invalid Transaction type")
      while True:
          date = input("Enter date (YYYY-MM-DD): ")
          if len(date)!=10:
              print("Invalid date")
              continue
          year,month,day = date.split("-")
          if len(date)==10 and int(month)<=12 and int(day)<=31:
              break
          else:
              print("Invalid date")
      transactions.append([amount, category, transaction_type, date]) # Creates a new list containing the inputed transaction details
      save_transactions()
      print("Transaction added successfully.")
    except ValueError:
        print("Invalid amount, Please enter a valid amount") # Print this instead of displaying error

def view_transactions():
    if not transactions:
        print("No transactions available.")
        return
    print("Transactions:")
    for index, transaction in enumerate(transactions, start=1): # If there are transactions in the list, the function iterates over each transaction using a for loop.
        print(f"{index}. Amount: {transaction[0]}, Category: {transaction[1]}, Type: {transaction[2]}, Date: {transaction[3]}")

# index: Each transaction is printed with an index number starting from 1

def update_transaction():
    view_transactions()
    try:
        index=int(input("Enter index of transaction to update: "))-1
        if index>=0 and index<len(transactions):
            new_amount = float(input("Enter new amount: "))
            new_catagory = input("Enter new catagory: ")
            while True:
                new_trans_type = input("Enter new transaction type(Income/Expense): ").capitalize()
                if new_trans_type in ["Income","Expense"]:
                    break
                else:
                    print("Invalid transaction type")
            while True:
                new_date = input("Enter new Date(YYYY-MM-DD): ")
                if len(new_date)!=10:
                    print("Invalid date")
                    continue
                year,month,day = new_date.split("-")
                if len(new_date)==10 and int(month)<=12 and int(day)<=31:
                    break
                else:
                    print("Invalid date")
                    
            
            transactions[index]=[new_amount,new_catagory,new_trans_type,new_date]
            save_transactions()
            print("Transaction updated successfully")
        else:
            print("Invalid index, Please enter a valid index")
    except ValueError:
            print("Invalid amount, Please enter a valid amount")

def delete_transaction():
    view_transactions()
    try:
        index=int(input("Enter index of transaction to delete: "))-1
        if index>=0 and index<len(transactions):
            del transactions[index]
            save_transactions()
            print("Transaction deleted successfully")
        else:
            print("Invalid index, please enter a valid index")
    except ValueError:
        print("Invalid index. Please eneter a valid index")

def display_summary():
    total_income = sum(transaction[0] for transaction in transactions if transaction[2] == "Income")
    total_expense = sum(transaction[0] for transaction in transactions if transaction[2] == "Expense")
    print(f"Total Income: {total_income}")
    print(f"Total Expense: {total_expense}")
    print(f"Balance: {total_income - total_expense}")

def main_menu():
    load_transactions()  # Load transactions at the start
    while True:
        print("\nPersonal Finance Tracker")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Update Transaction")
        print("4. Delete Transaction")
        print("5. Display Summary")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_transaction()
        elif choice == '2':
            view_transactions()
        elif choice == '3':
            update_transaction()
        elif choice == '4':
            delete_transaction()
        elif choice == '5':
            display_summary()
        elif choice == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()

# if you are paid to do this assignment please delete this line of comment 
