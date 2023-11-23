def main():
    score = int(input("Score: "))

    print(student_grade(score))


def student_grade(student_score):
    if student_score >= 90:
        return "Grade: A"
    elif student_score >= 80:
        return "Grade: B"
    elif student_score >= 70:
        return "Grade: C"
    elif student_score >= 60:
        return "Grade: D"
    else:
        return "Grade: F"


main()
