# 1. Basic Calculator

number_one = int(input("Enter Your First Number"))
number_two = int(input("Enter Your Second Number"))
print(number_one + number_two)
print(number_one - number_two)
print(number_one * number_two)
print(number_one // number_two)
print(number_one % number_two)


# 2. Comparison Checker

check_first_number = int(input("Enter First Number"))
check_second_number = int(input("Enter Second Number"))

print(check_first_number > check_second_number)
print(check_first_number < check_second_number)
print(check_first_number == check_second_number)
print(check_first_number != check_second_number)


# 3. Money Manager
# শুরুতে balance ভ্যারিয়েবলে ১০০০ রাখুন। এরপর += দিয়ে ৫০০ যোগ করুন, -= দিয়ে ২৫০ বিয়োগ করুন এবং *= দিয়ে ২ গুণ করুন। প্রতিটি ধাপের পরে বর্তমান balance প্রিন্ট করুন।

money = 1000
money += 500 
print(money)
money -= 250
print(money)
money *= 2
print(money)


# 4. Logical Checker


age = 20
has_ticket = True
has_id = False

print(age and has_ticket and has_id)
print(age or has_ticket or has_id)
print(not has_ticket )



# 5. Shopping Bill Project



check_product_name = input("Enter product name")
check_product_price = int(input("Enter first Number"))
check_product_quantity = int(input("Enter Second Number"))

total_price = (check_product_price * check_product_quantity) 
discount = (total_price * 10) / 100
after_discount= (total_price - discount) 

print(f"Product Name: {check_product_name}, total price: {total_price}, After 10% discount You need to pay {after_discount}")



    