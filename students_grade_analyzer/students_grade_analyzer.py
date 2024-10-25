def student_grade(grade):
    if grade.isdigit():
        grade = int(grade)
        if 0 < grade < 100:
            return True
    else:
        return False

while True:
    grade = (input("Please enter the grade of the student: "))
    if student_grade(grade):
        break
    else:
        print("Invalid characters. Please enter a valid grade.")


