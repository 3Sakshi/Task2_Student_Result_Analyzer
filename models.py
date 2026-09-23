class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def display_info(self):
        print(f"\nStudent Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")

        print("\nSubject Marks:")
        for subject, mark in self.marks.items():
            print(f"{subject}: {mark}")