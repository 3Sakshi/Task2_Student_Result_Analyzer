def calculate_result(marks):
    total = sum(marks.values())
    maximum = len(marks) * 100
    percentage = (total / maximum) * 100

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    status = "Pass" if all(mark >= 35 for mark in marks.values()) else "Fail"

    return {
        "total": total,
        "percentage": round(percentage, 2),
        "grade": grade,
        "status": status
    }


def find_highest_subject(marks):
    return max(marks, key=marks.get)


def find_lowest_subject(marks):
    return min(marks, key=marks.get)