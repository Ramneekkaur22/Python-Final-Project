from expense_tracker import ExpenseTracker


def main():
    tracker = ExpenseTracker()

    while True:

        print("\n========== PERSONAL EXPENSE TRACKER ==========")
        print("1. Add New Expense")
        print("2. View All Expenses")
        print("3. Search Expense")
        print("4. Update Expense")
        print("5. Delete Expense")
        print("6. View Summary")
        print("7. Exit")
        print("==============================================")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            tracker.add_expense()

        elif choice == "2":
            tracker.view_expenses()

        elif choice == "3":
            tracker.search_expense()

        elif choice == "4":
            tracker.update_expense()

        elif choice == "5":
            tracker.delete_expense()

        elif choice == "6":
            tracker.view_summary()

        elif choice == "7":
            tracker.save_expenses()
            print("\nExpenses saved successfully!")
            print("Thank you for using Personal Expense Tracker.")
            break

        else:
            print("Invalid choice! Please enter a number between 1 and 7.")


if __name__ == "__main__":
    main()