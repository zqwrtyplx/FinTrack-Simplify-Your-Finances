import tkinter as tk
from tkinter import ttk
import json

class FinanceTrackerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Finance Tracker")
        self.root.iconbitmap('icon.ico') # icon
        root.geometry('750x400') # width x height
        root.resizable(False,False) # using this for avoiding resize the GUI
        self.create_widgets()
        self.transactions = self.load_transactions("transactions.json")

    def create_widgets(self):
        # Frame for table and scrollbar

        self.tree_frame1 = tk.Frame(self.root,background='#B2BEB5') # This line creates a Frame widget named self.tree_frame within the self.root window
        self.tree_frame1.pack(fill = "x",pady=10) # Pady puts some space between the button widgets and the borders of the frame and the borders of the root window
        # fill="x" means the frame will fill the available horizontal space within the root window. 

        label1 = tk.Label(self.tree_frame1,text= "Personal Finance Tracker",font=("rf dewi expanded semibold",20),background='#B2BEB5')
        label1.pack(ipady=5)
        
        self.tree_frame2 = tk.Frame(self.root)
        self.tree_frame2.pack(fill="x",pady=10)

        label2 = tk.Label(self.tree_frame2,text="Search Your Recorded Transactions",font=("rf dewi expanded semibold",13))
        label2.pack(padx=10)
        

        # Treeview for displaying transactions

        self.table = ttk.Treeview(self.root, columns=('Category', 'Amount', 'Date'), show='headings')

        self.table.column('Amount', width=100)
        self.table.column('Date', width=100)
        self.table.column('Category', width=100)

        self.table.heading('Amount', text="Amount", command=lambda: self.sort_by_column("Amount"))
        self.table.heading('Date', text="Date", command=lambda: self.sort_by_column("Date"))
        self.table.heading('Category', text="Category", command=lambda: self.sort_by_column("Category"))


        self.table.pack(fill="x", pady=10)


        # Scrollbar for the Treeview

        scrollbar = ttk.Scrollbar(self.table, orient="vertical", command=self.table.yview)
        self.table.configure(yscrollcommand=scrollbar.set)

        # Pack the Treeview and scrollbar widgets
        
        self.table.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")


        # Search bar and button
        
        self.search_text=tk.StringVar()
        self.search_option = ttk.Entry(self.tree_frame2, width=60,textvariable=self.search_text)
        
        self.search_click = ttk.Button(self.tree_frame2, text="Search",command=self.search_transactions)

        self.search_option.pack(padx=6, pady=6)
        self.search_click.pack(padx=6, pady=6)       

        pass
        

    def load_transactions(self, filename):
        try:
            with open(filename,'r') as file:
                transactions = json.load(file)
                return transactions
        except FileNotFoundError:
                return{}
            
        except FileNotFoundError:
            return {}
        
    def display_transactions(self, transactions):
        self.display=transactions
        for data in self.table.get_children():
            self.table.delete(data)

        for self.keys, self.values in self.display.items():
            for self.data in self.values:
                self.table.insert("", index='end', values=(f'{self.keys}',
                                                           self.data['Amount'],
                                                           self.data['Date']))

    def search_transactions(self):
        search_text = self.search_text.get().lower()
        searched = {}

        for category, category_data in self.transactions.items():
            filtered_category_transactions = []
            for transaction in category_data:
                if any(
                    search_text in str(value).lower()
                    for value in [category, transaction["Amount"], transaction["Date"]]
                ):
                    filtered_category_transactions.append(transaction)
            if filtered_category_transactions:
                searched[category] = filtered_category_transactions

        self.display_transactions(searched)

    def sort_by_column(self, col):
        # Get the current items in the treeview
        data = [(self.table.set(child, col), child) for child in self.table.get_children('')]

        # Sort the data
        data.sort()

        for index, (val, child) in enumerate(data):
            self.table.move(child, '', index)

        # Change the heading to reflect the sort
        self.table.heading(col, command=lambda: self.sort_by_column(col))

def main():
    root = tk.Tk()
    app = FinanceTrackerGUI(root)
    app.display_transactions(app.transactions)
    root.mainloop()

if __name__ == "__main__":
    main()



