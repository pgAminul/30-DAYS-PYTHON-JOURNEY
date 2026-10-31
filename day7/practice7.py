# Project: Mini Student Result Tracker

def Marks_Calculate():
    name = input('Enter Your Name')
    age = int(input('Enter Your Age'))
    Marks = [30, 50, 60 , 65, 20]
    total = 0
    grades = ("Fail", "D", "C", "B", "A", "A+")
    for Mark in Marks:
        total += Mark
        if Mark <= 33 and Mark >= 0 :
            print(f"{name} Your Bangla Grade Is {grades[0]}")
                 
        elif Mark >= 40 and Mark < 50:
            print(f"{name} Your English Grade Is {grades[1]}")
                
        elif Mark >= 50 and Mark < 60:
            print(f"{name} Your Math Grade Is {grades[2]}")
                
        elif Mark >= 60 and Mark < 70:
            print(f"{name} Your Science Grade Is {grades[3]}")
                
        elif Mark >= 70 and Mark < 80:
            print(f"{name} Your Social Science Grade Is {grades[4]}")
                
        elif Mark >= 80 and Mark <= 100:
            print(f"{name} Your (ICT) Grade Is {grades[5]}")
                 
        elif Mark <0 or Mark > 100:
            grade = ("Invalid Number")
            print(f"{name} You Put {grade}")
                
        else:
            return "Nothing"
    average = f"Your Total Average Mark is {total / len(Marks) } And Your Total Mark Is {total} "
    return average

print(Marks_Calculate())



    
