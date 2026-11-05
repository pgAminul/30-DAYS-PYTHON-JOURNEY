# Task 1 — Safe Division Calculator

try:
    firstNumber = int(input("Enter Your First Number"))
    secondNumber = int(input("Enter Your Second Number"))
    result = firstNumber / secondNumber

except (ValueError, ZeroDivisionError) as error:
    print(f"cannot divide by zero and must be it's will number {error}")
else:
    print(f"First Number is {firstNumber}\nSecond Number is {secondNumber}\nAnswer is: {result}")
finally:
    print("Calculation Completed")


# Task 2 — Smart Age Validator 

try:
    def check_age(age):
        msg =""
        if age <= 0:
            raise ValueError("Age cannot be negative")
        if age >0 and age <= 18:
            msg = ("Minor")
            
        elif age >18:
            msg =("adult")
            
        return msg
except ValueError as error:
    print(error)
print(check_age(55))


# Task 3 — Safe Student File Reader 

try:
    userFile = input("Enter The file Name").strip()
    with open(userFile, "r") as file:
       content = file.read()
except FileNotFoundError:
    print("file Not Found")
else:
    print(content)
finally:
    print("File Operation Finished")


# Task 4 — Student Marks Validator (20 Marks)

try:
    studentName = input("Enter Your Name").strip()
    studentMark = int(input("Enter Your Marks"))
    if studentMark < 0 or studentMark > 100:
        raise ValueError ("Marks must be between 0 and 100")
    elif studentMark > 0 or studentMark <= 33 :
        print("Fail")
    elif studentMark >= 33 or studentMark <= 100:
        print('pass')
except ValueError as error:
    print(error)
else:
    print(f"Studnet Name: {studentName}")
    print(f"Studnet Mark: {studentMark}")