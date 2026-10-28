# Task 1: Smart Calculator Function — 20 Marks

def calculator(a, b, operator):
    if operator == "+":
        result = a + b
        return result
    elif operator == "-":
        result = a-b
        return result
    elif operator == "*":
        result =a * b
        return result
    elif operator == "/":
        if a == 0 or b  == 0:
            result ="invalid input"
            return result
        result = a/b
        return result

            
print(calculator(4, 5, "+"))
print(calculator(10, 5, "-"))
print(calculator(4, 5, "*"))
print(calculator(10, 2, "/"))
print(calculator(10, 0, "/"))
print(calculator(10, 5, "%"))



# Task 2: Student Result Analyzer — 20 Marks

def student_result(name, mark):
    if mark <= 40 and mark >= 0 :
        return f"hello {name} Your Grade Is F"
         
    elif mark >= 40 and mark < 50:
        return f"hello {name} Your Grade Is D"
        
    elif mark >= 50 and mark < 50:
        return f"hello {name} Your Grade Is C"
        
    elif mark >= 60 and mark < 70:
        return f"hello {name} Your Grade Is B"
        
    elif mark >= 70 and mark < 80:
        return  f"hello {name} Your Grade Is A"
        
    elif mark >= 80 and mark <= 100:
        return f"hello {name} Your Grade Is A+"
         
    elif mark <0 or mark > 100:
        return f"hello {name} Your Grade Is Invalid Input"
        
    else:
        return "Nothing"

print(student_result('Aminul', 50))


# Task 3: Salary & Savings Analyzer — 20 Marks

def analyze_finance(income, expense, savings_rate=10):
    if income < expense or savings_rate > 100 or savings_rate <0:
        return "Error"
    else:
        balance = float(income - expense)
        savings_rate= float(income * savings_rate / 100)
        own_money = balance - savings_rate
        if own_money > balance:
            return "nagative value"
        return balance , savings_rate, own_money

print(analyze_finance(5000, 1010, 10))


# number_statistics(start, end) Function তৈরি করুন।



def number_statistics(start, end):
    even_number = 0
    odd_number = 0
    even_count = 0
    odd_count = 0
    if start > end:
        return "your starting number gatter then ending number"
    for i in range(start, end + 1):
        if i % 2 ==0:
            even_number += i
            even_count += 1

        elif i % 2 == 1:
            odd_number += i
            odd_count += 1
        else:
            return "something wrong"
    return even_number, even_count , odd_number, odd_count

print(number_statistics(1, 10))