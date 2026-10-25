# Assignment 1 — Smart Age Checker (20 Marks) 


age = int(input("Write our Age"))
# age 1 to  18 child
if age < 18 and age >=1:
    print("You are child")
    # age 19 20 Teeneger
elif age >=18 and age <=20:
    print("you are Teenager")
    #  age 21 to over Adult
elif age >=21:
    print("You are Adult")
    #  age below 0 invalid age
else:
    print("Invalid Age")


# Assignment 2 — Grade Calculator (20 Marks)
# # Grad = 1 to below 33 Fail, upto 33 to equal 50 C , upto 50 to equal 60 B, upto 61 to equal 80 A, upto 81 to equal 100 A+,

mark = int(input("Write Mark For Grade Calculation"))
if mark >= 1 and mark <= 33:
    print("You are Fail")
elif mark >=34 and mark <= 50:
    print("Your Grad (C)")
elif mark >=51 and mark <= 60:
    print("Your Grad (B)")
elif mark >=61 and mark <= 80:
    print("Your Grad (A)")
elif mark >=81 and mark <= 100:
    print("Your Grad (A+)")
elif mark < 1 or mark > 100:
    print("Invalid Marks")
else:
    ("Invalid Input")



# Assignment 3 — Secure Login System (20 Marks) 

Username = "Aminul"
Password = "Amin12"

userNameInput= input('Write Your User Name')
passwordInput= input('Write Your Password')

if userNameInput != Username:
    print("Invalid Username")

if userNameInput == Username:
    if passwordInput == Password:
        print("Loging Successful")
if userNameInput == Username:
    if passwordInput != Password:
        print("Wrong Password")


# Assignment 4 — ATM Withdrawal (20 Marks) 


Balance = int(input("Write Your Balance: "))
Withdraw = int(input("Write Your Withdrawal Amount: "))

if Balance <= 0 or Withdraw <= 0:
    print("Wrong Amount")

elif Withdraw % 500 != 0:
    print("Withdrawal Amount Must Be a Multiple of 500")

elif Balance < Withdraw:
    print("Insufficient Balance")

else:
    Remaining = Balance - Withdraw
    print("Withdrawal Successful")
    print(f"Remaining Balance: {Remaining}")


# Assignment 5 — Shopping Discount (20 Marks) 


WaterBill = int(input("Write Your Water Bill"))
if WaterBill >=5000 :
    discount= (WaterBill * 20) / 100
    pay = WaterBill - discount
    print (f"Hurrry! You Got 20% {discount} Amount, Just Pay {pay} amount")
elif WaterBill >=2000 :
    discount= (WaterBill * 10) / 100
    pay = WaterBill - discount
    print (f"Hurrry! You Got 10% {discount} Amount, Just Pay {pay} amount")
elif WaterBill < 2000 and WaterBill > 0 :
    print (f"You didn't Get any Discount, You Need To Pay {WaterBill} amount")
else:
    print('Invalid Water Bill')