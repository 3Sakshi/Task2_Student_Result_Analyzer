from models import Student
from result_analyzer import (
    calculate_result,
    find_highest_subject,
    find_lowest_subject
)
from validators import validate_student_name, validate_marks


def get_marks(subject):
    while True:
        try:
            mark = int(input(f"Enter marks for {subject} (0-100): "))
            return validate_marks(mark)
        except ValueError as error:
            print(f"Error: {error}")


def display_result(student):
    result = calculate_result(student.marks)

    student.display_info()

    print("\n--- Result Summary ---")
    print(f"Total Marks: {result['total']}")
    print(f"Percentage: {result['percentage']}%")
    print(f"Grade: {result['grade']}")
    print(f"Status: {result['status']}")

    highest = find_highest_subject(student.marks)
    lowest = find_lowest_subject(student.marks)

    print(f"Highest Marks: {highest} ({student.marks[highest]})")
    print(f"Lowest Marks: {lowest} ({student.marks[lowest]})")


def main():
    print("====== Student Result Analyzer ======")

    while True:
        try:
            name = validate_student_name(
                input("Enter student name: ")
            )
            break
        except ValueError as error:
            print(f"Error: {error}")

    while True:
        roll_number = input("Enter roll number: ").strip()
        if roll_number:
            break
        print("Error: Roll number cannot be empty.")

    subjects = ["Python", "AI", "Computer Networks", "Mathematics"]

    marks = {}

    for subject in subjects:
        marks[subject] = get_marks(subject)

    student = Student(name, roll_number, marks)

    display_result(student)


if __name__ == "__main__":
    main()