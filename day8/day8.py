# Task 1: Student Profile Manager

name = input("enter Your Name")
age = int(input("enter Your age"))
course = input("enter Your Course Name")
marks = int(input("enter Your marks"))

student ={
"Name": name,
"Age": age,
"Course": course,
"Mark": marks,
"Previos_Mark": 0
}

update = int(input("enter Your update marks"))

student["Previos_Mark"] = update
print(student)
print(student.get("Previos_Mark"))

if student.get("Previos_Mark") < 0 or student.get("Previos_Mark") > 100 or student.get("Mark")<0 or student.get("Mark") > 100:
    print("Fail")
if student.get("Previos_Mark") < 40 or  student.get("Mark")<40:
    print("Fail")
elif student.get("Previos_Mark") >= 40 or  student.get("Mark") >= 40:
    print("pass")

# Task 2: Product Inventory

product ={
    "apple": 20,
    "orange": 30,
    "banana": 40,
    "mango": 50
}

name = input("Enter Your Product Name")
if name not in product.keys():
    print("Product not Found")
else:
    print(product.get(name))

addProduct = input("Add a Product")
addPrice = int(input("Add Product price"))
product[addProduct]= addPrice

PSearch = input("search by name")
priceUpdate = int(input("Add Product price"))

if PSearch not in product.keys():
    print("Product not Found")
else:
    product[PSearch] = priceUpdate

for pro in product.items() :
    print(pro)

# Task 3: Unique Number Analyzer

numbers = [10, 20, 10, 30, 40, 20, 50]
sum = 0
removeDuplicate= set(numbers)
unique = len(removeDuplicate)
for summ in removeDuplicate:
    sum +=summ
maximum = max(removeDuplicate)
minimum = min(removeDuplicate)
print(f"After removing duplicate value the value is {removeDuplicate}, and the total lenth is {unique}, after removing the duplicate value the total result is {sum}, maximum number is {maximum} and the minimum number is {minimum}")


# Task 4: Student Marks Tracker

studentss ={
    "student1":{
        "name": "Aminul Islam",
        "mark": 90
    },
    "student2":{
        "name": "Ariful Islam",
        "mark": 80
    },
    "student3":{
        "name": "Wajid Hasan",
        "mark": 70
    }
}

def analyze_students(students):
    maxi= 0
    heighstMark =""
    total = 0
    average = 0
    for student in students.values():
        mark = (student["mark"])
        allMarks = int(mark)
        total += allMarks
        print(f"Student Mark is {allMarks}")
  
        if mark > maxi :
            maxi = mark
            heighstMark = student['name']
    print(f"the Heighst Mark Got {heighstMark}")
    average = total / len(students.values())
    return average
    
        


print(analyze_students(studentss))