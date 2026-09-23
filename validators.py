def validate_student_name(name):
    if not name.strip():
        raise ValueError("Student name cannot be empty.")

    if not all(char.isalpha() or char.isspace() for char in name):
        raise ValueError("Student name must contain only letters and spaces.")

    return name.strip()


def validate_marks(mark):
    if not isinstance(mark, int):
        raise ValueError("Marks must be an integer.")

    if mark < 0 or mark > 100:
        raise ValueError("Marks must be between 0 and 100.")

    return mark