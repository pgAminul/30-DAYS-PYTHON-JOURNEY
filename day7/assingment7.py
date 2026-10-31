# Task 1: Student List Manager

Student = ["Aminul", "jisan", "parvej", "mahi", "nine"]
print(f"First Student is {Student[0]}, Last Student is {Student[-1]}, The Student Length is {len(Student)}")

# Task 2: Shopping List

Product = ['shoes', 'apple', 'orange']
Product.append('banana')
Product.insert(1,'mango')
Product.remove("mango")
Product.pop(1)
print(Product)

# Task 3: Marks Analyzer

Marks = [20, 30, 50, 60, 90]
total = 0
for mark in Marks:
  total += mark
  average = total / len(Marks)
  print(f"Average Is {average}")
  
print(f"The Total Marks is {total}, The Highest Mark is {max(Marks)}, The Lowest Mark is {min(Marks)}")

# Task 4: Tuple Explorer

countries = ('bangladesh', 'india', 'nepal', 'malaysia', 'america')
print(f"first country is {countries[0]}, the last country is {countries[-1]}, the total country is {len(countries)}, first 3 country is {countries[0:3]}")

# Task 5: Number Filter Function

evenNumber = []
def filter_even(numbers):
  for nmbr in numbers:
    if nmbr % 2 == 0:
        evenNumber.append(nmbr)
  return evenNumber


print(filter_even([1, 2, 3, 4, 5, 6, 8]))