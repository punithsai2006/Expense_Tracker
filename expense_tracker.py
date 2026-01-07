import csv
import datetime
import matplotlib.pyplot as plt

FILE_NAME = "expenses.csv"

# Add Expense
def add_expense():
    date = datetime.date.today().strftime("%Y-%m-%d")
    category = input("Enter category (Food, Travel, Shopping, etc): ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])

    print("Expense added successfully!")


# Monthly Summary
def monthly_summary():
    month = input("Enter month (YYYY-MM): ")
    total = 0

    print("\nDate | Category | Amount | Description")
    print("-" * 45)

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["date"].startswith(month):
                print(row["date"], row["category"], row["amount"], row["description"])
                total += float(row["amount"])

    print(f"\nTotal Expense for {month}: ₹{total}")


# Expense Chart
def show_chart():
    category_total = {}

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            category = row["category"]
            amount = float(row["amount"])

            if category in category_total:
                category_total[category] += amount
            else:
                category_total[category] = amount

    plt.bar(category_total.keys(), category_total.values())
    plt.xlabel("Category")
    plt.ylabel("Amount (₹)")
    plt.title("Category-wise Expense Distribution")
    plt.show()


# Export CSV
def export_csv():
    with open(FILE_NAME, "r") as source:
        data = source.read()

    with open("expense_report.csv", "w") as target:
        target.write(data)

    print("Data exported to expense_report.csv")


# Menu
def main():
    while True:
        print("\n====== EXPENSE TRACKER ======")
        print("1. Add Expense")
        print("2. Monthly Summary")
        print("3. Show Expense Chart")
        print("4. Export CSV")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            monthly_summary()
        elif choice == "3":
            show_chart()
        elif choice == "4":
            export_csv()
        elif choice == "5":
            print("Exiting program")
            break
        else:
            print("Invalid choice, try again")


main()
