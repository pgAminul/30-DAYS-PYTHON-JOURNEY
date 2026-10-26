# Task 1: Number Printer — 15 Marks

userInput= int(input("Give Your Number For Print from 1 to until your input"))
for userInput in range(0, userInput):
    userInput += 1
    print(userInput)

# Task 2: Multiplication Table — 15 Marks

userMultiplication = int(input("Multiplication input"))
for i in range(1,11):
    multiply = userMultiplication * i
    print(f"{userMultiplication} X {i} X {multiply}")


# Task 3: Even/Odd Sum — 15 Marks

even_Number = 0
Odd_Number = 0

for i in range(1, 101):
    if i % 2 == 0:
        even_Number += i

    if i % 2 == 1:
        Odd_Number += i

print(f"Even Number Sum: {even_Number}")
print(f"Odd Number Sum: {Odd_Number}")



# Task 4: Password Checker — 15 Marks

password= 1234
userPass = ""
while password != userPass:
    userPass= int(input('Wrong Password'))
print("Access Granted")

# Task 5: Smart Savings Calculator — 20 Marks

totalDaySavings = int(input('How much day you want to savings?'))
totalMoneySavings = int(input('How much Rm you want to savings?'))
total = 0
for totalDaySavings in range (0 , totalDaySavings):
    totalDaySavings += 1 
    total= totalMoneySavings * totalDaySavings
    print (f"Day {totalDaySavings}: RM {total}")

if total >= 500:
    print("Congratulations! Goal Achieved")
else:
    print("Goal Not Achieved")
