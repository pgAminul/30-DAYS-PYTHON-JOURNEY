# Task 1 — Student Profile System

from asyncio import Task


class Student:
    def __init__(self, name, age, city):
        self.name= name
        self.age= age
        self.city= city
    def show_profile(self):
        name = self.name
        age = self.age
        city = self.city
        return name, age, city
student1 = Student("aminul", 20, "Dhaka")
student2= Student("aminul", 20, "Dhaka")


print(student1.show_profile())
print(student2.show_profile())


# Task 2 — Bank Account System

class BankAccount:
    def __init__(self, owner, balance):
        self.owner= owner
        self.balance= balance

    def deposit(self,amount):
        if amount <= 0:
            print("invalid amount")
        else:
            self.balance += amount
            print(f"Successfully Deposit {amount} ")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Withdraw Failed")
        elif amount <=0 :
            print("Invalid Amount")
        else:
            self.balance -= amount
            print(amount)
    def show_balance(self):
        curentBalance = f"Your Current Balance is {self.balance}"
        return curentBalance
current = BankAccount("Aminul", 2000)
print(f"Ower Name {current.owner}")
print(f"Ower Balance {current.balance}")
current.deposit(500)
current.withdraw(800)
print(current.show_balance())


# Task 3 — Employee Salary Manager

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def increase_salary(self, percent):
        if percent < 0:
            print("invalid percent")
            print(f"Increase: 0%")
            print(f"New Salary {self.salary}")
        else:
           increse_Salary = percent
           print(f"Increase: {increse_Salary}%")
           newSalary = self.salary * percent / 100
           current_Salary = self.salary + newSalary
           print (f"New Salary {current_Salary}" )
       
    def show_details(self):
        print(f"Employee Name {self.name}")
        print(f"Old Salary {self.salary}")
details = Employee("Aminul", 10000)
details.show_details()
details.increase_salary(10)


# Task 4 — Smart Student Result System


class StudentResult:
    def __init__(self, name, python_marks, math_marks, english_marks):
        self.name = name
        self.python_marks = python_marks
        self.math_marks = math_marks
        self.english_marks = english_marks
        print(self.name)
    def calculate_total(self):
 
        if self.python_marks < 0 or  self.math_marks < 0 or self.english_marks < 0 or self.python_marks > 100 or  self.math_marks > 100 or self.english_marks > 100: 
            print("Marks Can't Be below 0")
        else:
           total = self.python_marks + self.math_marks + self.english_marks 

           return total

    def calculate_average(self):
         total = self.calculate_total()
         average = total / 3
         return average

    def get_grade(self):
        mark = self.calculate_average()

        if mark < 40:
            return "F"
        elif mark < 50:
            return "D"
        elif mark < 60:
            return "C"
        elif mark < 70:
            return "B"
        elif mark < 80:
            return "A"
        elif mark <= 100:
            return "A+"
        else:
            return "Invalid Marks"
    def show_result(self):
        if self.python_marks < 40 or self.math_marks < 40 or self.english_marks < 40:
          result = "Fail"
          print(f"Result: {result}")
        else:
            result = "Pass"
            print(f"Result: {result}")

allDetails = StudentResult("Aminul", 20, 50, 80)
print(f"Total: {allDetails.calculate_total()}")
print(f"Average: {allDetails.calculate_average()}")
print(f"Grade: {allDetails.get_grade()}" )
allDetails.show_result()