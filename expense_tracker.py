import csv
import os
from datetime import datetime
from expense import Expense


class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.file_name = "expenses.csv"
        self.next_id = 101
        self.load_expenses()

    def load_expenses(self):
        if not os.path.exists(self.file_name):
            return

        with open(self.file_name, mode="r", newline="") as file:
            reader = csv.reader(file)
            next(reader, None)  # Skip header

            for row in reader:
                expense = Expense(
                    int(row[0]),
                    row[1],
                    float(row[2]),
                    row[3],
                    row[4]
                )

                self.expenses.append(expense)

        if self.expenses:
            self.next_id = max(exp.expense_id for exp in self.expenses) + 1

    def save_expenses(self):
        with open(self.file_name, mode="w", newline="") as file:
            writer = csv.writer(file)

            writer.writerow(["ID", "Title", "Amount", "Category", "Date"])

            for expense in self.expenses:
                writer.writerow([
                    expense.expense_id,
                    expense.title,
                    expense.amount,
                    expense.category,
                    expense.date
                ])
                
    def add_expense(self):
        title = input("Enter Expense Title: ")

        while True:
            try:
                amount = float(input("Enter Expense Amount: "))
                break
            except ValueError:
                print("Invalid amount! Please enter a number.")

        category = input("Enter Expense Category: ")

        while True:
            date = input("Enter Expense Date (DD-MM-YYYY) or press Enter for today: ")

            if date == "":
                date = datetime.now().strftime("%d-%m-%Y")
                break

            try:
                datetime.strptime(date, "%d-%m-%Y")
                break
            except ValueError:
                print("Invalid date format!")

        expense = Expense(
            self.next_id,
            title,
            amount,
            category,
            date
        )

        self.expenses.append(expense)

        print(f"\nExpense Added Successfully!")
        print(f"Generated ID: {self.next_id}")

        self.next_id += 1
        
    def view_expenses(self):

        if not self.expenses:
            print("\nNo expenses found.")
            return

        print("\n")
        print("-" * 75)
        print(f"{'ID':<6}{'Title':<20}{'Amount':<12}{'Category':<18}{'Date'}")
        print("-" * 75)

        for expense in self.expenses:
            print(f"{expense.expense_id:<6}"
                  f"{expense.title:<20}"
                  f"{expense.amount:<12.2f}"
                  f"{expense.category:<18}"
                  f"{expense.date}")

        print("-" * 75)
        
    def search_expense(self):

        try:
            expense_id = int(input("Enter Expense ID: "))
        except ValueError:
            print("Invalid ID!")
            return

        for expense in self.expenses:

            if expense.expense_id == expense_id:

                print("\nExpense Found")
                print("---------------------------")
                print("ID:", expense.expense_id)
                print("Title:", expense.title)
                print("Amount:", expense.amount)
                print("Category:", expense.category)
                print("Date:", expense.date)

                return

        print("Expense not found.")
        

    def update_expense(self):

        try:
            expense_id = int(input("Enter Expense ID to Update: "))
        except ValueError:
            print("Invalid ID!")
            return

        for expense in self.expenses:

            if expense.expense_id == expense_id:

                print("\nLeave field blank to keep current value.\n")

                title = input(f"New Title ({expense.title}): ")
                if title:
                    expense.title = title

                amount = input(f"New Amount ({expense.amount}): ")
                if amount:
                    try:
                        expense.amount = float(amount)
                    except ValueError:
                        print("Invalid amount!")

                category = input(f"New Category ({expense.category}): ")
                if category:
                    expense.category = category

                date = input(f"New Date ({expense.date}): ")
                if date:
                    try:
                        datetime.strptime(date, "%d-%m-%Y")
                        expense.date = date
                    except ValueError:
                        print("Invalid Date!")

                print("\nExpense Updated Successfully!")
                return

        print("Expense not found.")
        
    def delete_expense(self):

        try:
            expense_id = int(input("Enter Expense ID to Delete: "))
        except ValueError:
            print("Invalid ID!")
            return

        for expense in self.expenses:

            if expense.expense_id == expense_id:

                self.expenses.remove(expense)

                print("\nExpense Deleted Successfully!")

                return

        print("Expense not found.")
        
    def view_summary(self):

        if not self.expenses:
            print("\nNo expenses available.")
            return

        total = 0
        category_total = {}

        for expense in self.expenses:

            total += expense.amount

            if expense.category in category_total:
                category_total[expense.category] += expense.amount
            else:
                category_total[expense.category] = expense.amount

        print("\n========== SUMMARY ==========")
        print(f"Total Expenses : ₹{total:.2f}")
        print(f"Number of Expenses : {len(self.expenses)}")

        print("\nCategory Wise Spending")

        for category, amount in category_total.items():
            print(f"{category:<15} ₹{amount:.2f}")

        print("=============================")