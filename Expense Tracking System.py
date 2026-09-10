import csv
import os
from datetime import datetime

FILE_NAME = "expenses.csv"

# Ensure CSV file exists with headers
def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Note"])

# Function to add a new expense
def add_expense():
    try:
        date = input("Enter date (YYYY-MM-DD): ")
        try:
            datetime.strptime(date, "%Y-%m-%d")  # Validate date format
        except ValueError:
            print("❌ Invalid date format! Please use YYYY-MM-DD.\n")
            return

        category = input("Enter category (e.g., Food, Travel, Shopping): ")
        try:
            amount = float(input("Enter amount: "))
        except ValueError:
            print("❌ Invalid amount! Please enter a number.\n")
            return

        note = input("Enter note (optional): ")

        with open(FILE_NAME, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([date, category, amount, note])

        print("✅ Expense added successfully!\n")
    except Exception as e:
        print(f"⚠️ Error adding expense: {e}\n")

# Function to view all expenses
def view_expenses():
    try:
        with open(FILE_NAME, mode="r") as file:
            reader = csv.reader(file)
            expenses = list(reader)

            if len(expenses) <= 1:
                print("No expenses recorded yet.\n")
                return

            total = 0
            print("\n--- All Expenses ---")
            for row in expenses[1:]:
                print(f"Date: {row[0]}, Category: {row[1]}, Amount: {row[2]}, Note: {row[3]}")
                total += float(row[2])
            print(f"\n💰 Total Amount Spent: {total}\n")
    except Exception as e:
        print(f"⚠️ Error reading expenses: {e}\n")

# Function to display category-wise summary
def category_summary():
    try:
        with open(FILE_NAME, mode="r") as file:
            reader = csv.reader(file)
            expenses = list(reader)

            if len(expenses) <= 1:
                print("No expenses recorded yet.\n")
                return

            summary = {}
            for row in expenses[1:]:
                category = row[1]
                amount = float(row[2])
                summary[category] = summary.get(category, 0) + amount

            print("\n--- Category Wise Spending ---")
            for category, total in summary.items():
                print(f"{category}: {total}")
            print()
    except Exception as e:
        print(f"⚠️ Error generating summary: {e}\n")

# Main menu
def menu():
    initialize_file()
    while True:
        print("===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Category Summary")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            category_summary()
        elif choice == "4":
            print("👋 Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please try again.\n")

if __name__ == "__main__":
    menu()
