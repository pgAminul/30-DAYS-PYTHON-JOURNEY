# student_utils.py-তে calculate_grade(marks) Function থাকবে, যা Marks ৩৩ বা বেশি হলে "Pass", অন্যথায় "Fail" Return করবে। get_average(marks_list) Function Average Return করবে।


def calculate_grade(marks):
    if marks > 33:
        return "Pass"
    else:
        return "Fail"

def get_average(marks_list):
    total = 0
    for mark in marks_list:
        total += mark
        average = total / len(marks_list)
        return average