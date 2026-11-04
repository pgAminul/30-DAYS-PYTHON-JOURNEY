try:
    # name = input("Enter Your Name").strip()
    # age = int(input("Enter Your Age"))
    monthly_income = int(input("Enter Your Monthly income"))
except ValueError:
    print("Age and Monthly income Give Number")


try:
    category_list = []
    for i in  range (0,5):
        foodCategory= input("write category name").strip()
        foodPrice= int(input("write category  price"))
        categoryDirectory = {f"{foodCategory}" : f"{foodPrice}"}
        category_list.append(categoryDirectory)
except ValueError:
    print("food price Give Number")


def finance_calculator():
    total_expense = 0
    remining = 0
    heighst = 0
    lowest = float("inf")

    for expense in category_list:
        for food, price in expense.items():
            pricee = int(price)
            total_expense += pricee

            if pricee > heighst:
                heighst = pricee

            if pricee < lowest:
                lowest = pricee
    if total_expense > monthly_income:
        print("Warning! You Under bank Load")
    remining = monthly_income - total_expense
    average = total_expense / len(category_list)


    message = f"total expense is {total_expense}\n remining balance is {remining}\n average is {average}\n Heighst Expense is {heighst}\n Lowest expense {lowest}"

    try:
        with open ("finance.txt", "a") as file:
         file.write(f"{category_list} \n{message}")
        with open ("day1-10/finance.txt" , "r") as readFile:
            readFile.read()
    except FileNotFoundError:
        print("file not found")
    return message

print(finance_calculator())