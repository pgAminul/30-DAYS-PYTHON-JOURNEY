import math
import random
from datetime import datetime
from student_utils import calculate_grade, get_average

# Task 1 — Smart Math Calculator
try:
    
    UserInput = float(input("Enter a number"))
    if UserInput <0 :
        raise ValueError ("Nagative Number")
    else:
        print(f'Sqrt: {math.sqrt(UserInput)}')
        print(f'Celi: {math.ceil(UserInput)}')
        print(f"Floor: {math.floor(UserInput)}")

except ValueError as error:
    print(error)


# Task 2 — Lucky Number Guessing

try:
    for i in range(0, 3):
        number = int(input("enter your lucky number between 1 to 10"))
        luckyNumber = random.randint(1, 10)
        if number == luckyNumber:
            print("you won")
            break
        elif number != luckyNumber:
            print("try Again")
        
except ValueError:
    print('just accept number')

finally:
    print("Game Over")


# Task 3 — Date & Time Reporter

currentDateTime = datetime.now()

year = currentDateTime.year
month = currentDateTime.month
day = currentDateTime.day
weekday = currentDateTime.strftime("%A")

dateFormat = currentDateTime.strftime("%d-%m-%Y")
timeFormat = currentDateTime.strftime("%H:%M:%S")


print(f"Current Date: {dateFormat}")
print(f"Current Time: {timeFormat}")
print(f"Year: {year}")
print(f"Month: {month}")
print(f"Day: {day}")
print(f"Weekday: {weekday}")



# Task 4 — Custom Student Result Module

try:
    name = input("Enter Your Name: ").strip()

    marks_all = []

    for i in range(1, 4):
        marks = float(input(f"Enter your Subject {i} marks: "))

        if marks < 0 or marks > 100:
            raise ValueError("Marks must be between 0 to 100")

        marks_all.append(marks)

    print(f"\nName: {name}")

    for i, mark in enumerate(marks_all, start=1):
        result = calculate_grade(mark)
        print(f"Subject {i} Mark: {mark} - {result}")

    average = get_average(marks_all)
    print(f"Overall Average: {average:.2f}")

except ValueError as error:
    print(error)
