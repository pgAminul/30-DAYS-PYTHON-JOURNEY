
# Smart Personal Finance & Student Tracker

name = input("Write your name: ")
age = int(input("Write your age: "))
expense = int(input("Write your monthly expense: "))
income = int(input("Write your monthly income: "))

balance = income - expense

# Age Validation
if age < 1:
    print("Invalid Age")
elif age < 18:
    print("You are a minor")
else:
    print("You are an adult")

print(f"Total Balance: RM {balance}")

# Weekly Expense Tracker
total = 0

for day in range(1, 8):
    daily_expense = int(input(f"Write expense for day {day}: "))
    total += daily_expense

average = total / 7

print(f"Total Weekly Expense: RM {total}")
print(f"Average Daily Expense: RM {average:.2f}")

# Menu System
while True:
    menuInput = input(
        "Choose menu (Profile, Expense, Savings, Exit): "
    ).strip().lower()

    if menuInput == "profile":
        print(f"Welcome to Profile, {name}")

    elif menuInput == "expense":
        print(f"Monthly Expense: RM {expense}")
        print(f"Weekly Expense: RM {total}")
        print(f"Average Daily Expense: RM {average:.2f}")

    elif menuInput == "savings":
        print(f"Monthly Balance: RM {balance}")

    elif menuInput == "exit":
        print("Thank you for using Smart Personal Finance Tracker!")
        break

    else:
        print("Invalid menu. Please try again.")
