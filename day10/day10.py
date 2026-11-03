# Task 1 — Student File Creator


name = input("Enter Your Name")
age = int(input("Enter Your Age"))
city = input("Enter Your City")

with open("day10/student.txt", "w") as file:
    file.write(name)
with open ("day10/student.txt", "a") as file:
    file.write(f"\n {age}, \n {city}")
with open ("day10/student.txt", "r") as readFile:
    print(readFile.read())

# Task 2 — Daily Expense Tracker

expense_name = input("Enter Your Expense")
expense_amount = int(input("Enter Your Expense Amount"))


with open ("day10/expenses.txt", "a") as expense:
    expense.write(f"{expense_name} : {expense_amount} \n")
with open("day10/expenses.txt", "r") as expense:
    print(expense.read())


# 3 — Student Names Reader


with open ("day10/names.txt", "r") as nameFile:
    readFile = nameFile.readlines()


    for index, names in enumerate(readFile, start=1):
        print(f"{index}. {names}")
        print(f"total student {index}")


# Task 4 — Safe File Reader


fileName = input("Enter Your File Name")
try:
    with open(fileName, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("file Not Found")