# Task 1 — Smart Calculator (20)

Addition = lambda a,b: a+b
print(Addition(5,5))
Subtraction = lambda a,b: a-b
print(Subtraction(5,4))
Multiplication = lambda a,b: a*b
print(Multiplication(5,5))
Division = lambda a,b : a/b
print(Division(4,2))

# Task 2 — Employee Salary Processor (20)

salaries = [15000, 25000, 18000, 35000, 12000, 40000]
salaryBounus = list(map(lambda b: b*10/100, salaries))
print(salaryBounus)
increase = list(zip(salaries, salaryBounus))
aaa=[]
for a in increase:
   bounus = int(a[0]+ a[1])
   print(bounus)
   aaa.append(bounus)
print(aaa)
filterData = list(filter(lambda x: x > 20000, aaa))
print(filterData)

# Task 3 — Student Information Merger (20)

names = ["Rahim", "Karim", "Sakib", "Nabil"]
ages = [22, 25, 21, 24]
departments = ["IT", "HR", "IT", "Finance"]

studentInformation = list(zip(names, ages, departments))
studentDatas = list(
   map(
      lambda student: {
         "name": student[0],
         "age": student[1],
         "department": student[2]
      },studentInformation
   )
)
print(studentDatas)

# Task 4 — Smart Student Result Analyzer (20)

students = [("Rahim", 85),("Karim", 35),("Sakib", 72), ("Nabil", 90),("Hasan", 45),("Jamal", 28)]
passStudents = list(filter(lambda student: student[1] >=  40 , students))
print(f"passed: {passStudents}")
grade = list(map(
    lambda x: {
       
       "name": x[0],
       "marks": x[1],
       "grade": "A" if x[1] >= 80 else "B" if x[1] >= 60 else "C" if x[1] >= 40 else "F"
        
    },students
))

print(grade)

from functools import reduce

highest = reduce(
    lambda a, b: a if a[1] > b[1] else b,
    students
)

print(highest)
