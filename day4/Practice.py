
# Project Name: Smart Student Management System

Studnet_Name = input("Student Name: ")
Studnet_Age = int(input("Student Age: "))

subOne = int(input("Write English Subject Number: "))
subTwo = int(input("Write Bangla Subject Number: "))
subThree = int(input("Write Math Subject Number: "))

Total_Marks = subOne + subTwo + subThree
Avarege_Marks = Total_Marks / 3

Grad = ""
Course_Eligibility = ""
Scholarship = "NO"

Course_Fee = int(input("Enter Course Fee: "))
Discount = 0
Final_Fee = 0

if (subOne < 0 or subOne > 100 or
    subTwo < 0 or subTwo > 100 or
    subThree < 0 or subThree > 100):

    print("Invalid Marks! Marks must be between 0 and 100.")

elif Studnet_Age < 1 or Studnet_Age > 100:
    print("Invalid Age!")

elif Course_Fee < 0:
    print("Invalid Course Fee!")

else:

    if Avarege_Marks <= 33:
        Grad = "D"

    elif Avarege_Marks <= 50:
        Grad = "C"

    elif Avarege_Marks <= 60:
        Grad = "B"

    elif Avarege_Marks <= 80:
        Grad = "A"

    else:
        Grad = "A+"

    if Studnet_Age >= 18 and Avarege_Marks > 50:
        Course_Eligibility = "YES"

        Scholarship = input(
            "Do You Have Any Scholarship? (YES/NO): "
        ).strip().upper()

        if Scholarship == "YES":
            Discount = (Course_Fee * 20) / 100

        else:
            Scholarship = "NO"
            Discount = 0

        Final_Fee = Course_Fee - Discount

    else:
        Course_Eligibility = "NO"
        Scholarship = "NO"
        Discount = 0
        Final_Fee = 0

    print("\n----- Student Report -----")
    print(f"Name : {Studnet_Name}")
    print(f"Age : {Studnet_Age}")
    print(f"Total Marks : {Total_Marks}")
    print(f"Average Marks : {Avarege_Marks:.2f}")
    print(f"Grade : {Grad}")
    print(f"Course Eligible : {Course_Eligibility}")
    print(f"Scholarship : {Scholarship}")
    print(f"Course Fee : {Course_Fee}")
    print(f"Discount : {Discount:.2f}")
    print(f"Final Fee : {Final_Fee:.2f}")
