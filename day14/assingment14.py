
# Task 1 — Student & Teacher Management

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age  = age
    def introduce(self):
        print(f"Name: {self.name}, Age: {self.age}")
class Student(Person):
    def __init__(self, name, age ,grad):
        super().__init__(name, age)
        self.grad = grad
    def Student_Profile(self):
        print(f"Name: {self.name}, age: {self.age}, Grad: {self.grad}")
class Teacher(Person):
    def __init__(self, name, age ,sub):
        super().__init__(name, age)
        self.sub = sub
    def Teacher_Profile(self):
        print(f"Name: {self.name}, age: {self.age}, Subject: {self.sub}")

Student1 = Student("Aminul", 25 , "A")
Student1.Student_Profile()
Teacher1 = Teacher("Rahim", 30, "Mathematics")
Teacher1.Teacher_Profile()

# Task 2 — Secure Bank Account

class BankAccount:
    def __init__(self, name, balance):
        self.name =name
        self.__balance = balance
    def Account_holder(self):
        print(f"Account Holder: {self.name}, \nInitial Balance: {self.__balance}")
    def deposit(self,amount):
        if amount < 0 :
            print("Amount Can't Below 0")
        self.__balance += amount
        print(f"Deposit: {amount}")
    def Withdraw(self, withdraw):
        if withdraw > self.__balance or withdraw < 0:
            print("Withdraw flied")
        self.__balance - withdraw
        print(f"Withdrawn: {withdraw}")
    def get_balance(self):
        return f"Current Balance {self.__balance}"

account = BankAccount("Aminul",1000)
account.Account_holder()
account.deposit(500)
account.Withdraw(300)
print(account.get_balance())

# Task 3 — Employee Salary System

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary= salary
    def calculate_bonus(self):
        bouns = self.__salary * 5 / 100
        print(f'5% bouns is {bouns}')
class Manager(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)
        self.name = name
        self.salary = salary
    def calculate_bonus(self):

        bouns = self.salary * 20 / 100
        total = self.salary + bouns
        print(f"Manager: {self.name}, \n Salary: {self.salary} \nBouns: {bouns}\nTotal: {total}")       
class Developer(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)
        self.name = name
        self.salary = salary
    def calculate_bonus(self):
        bouns = self.salary * 10 / 100
        total = self.salary + bouns
        print(f"Developer: {self.name}, \n Salary: {self.salary} \nBouns: {bouns}\nTotal: {total}")       
Manager1 = Manager("Aminul", 1000)
Manager1.calculate_bonus()
Developer1 = Developer("Rahim", 10000)
Developer1.calculate_bonus()


# Task 4 — Smart Shape Calculator

import math
class Shape:
    def area(self):
        raise NotImplementedError("Child class must implement area()")
class Rectangle(Shape):
    def __init__(self,length, width):
        if length <= 0 or width <= 0:
            raise ValueError("Length and Width must be positive!")

        self.length = length
        self.width = width

    def area(self):
        return f"Rectangle Area: {self.length * self.width}"

class Circle(Shape):
    def __init__(self,radius):
            if radius <= 0 :
                raise ValueError("Redius must be positive!")
    
            self.radius = radius
    def area(self):
         return f"Circle Area: {math.pi * (self.radius ** 2)}"
class Square(Shape):
    def __init__(self, side):
        if side <= 0:
            raise ValueError("Side must be positive!")

        self.side = side

    def area(self):
        return f"Square Area: {self.side ** 2}"


shapes = [
    Rectangle(10, 5),
    Circle(5),
    Square(6)
]


for shape in shapes:

    print(shape.area())