# Task2_Student_Result_Analyzer

A Python-based Student Result Analyzer developed as part of the Skyrovix Python Development Internship.

## 📌 Project Overview

The Student Result Analyzer is a command-line application designed to analyze student academic results.

It accepts student details and subject marks, validates the input, calculates total marks and percentage, assigns a grade, determines pass/fail status, and identifies the highest and lowest scoring subjects.

## 🚀 Features

- Accept student details
- Accept subject-wise marks
- Input validation
- Calculate total marks
- Calculate percentage
- Grade calculation
- Pass/Fail detection
- Find highest scoring subject
- Find lowest scoring subject
- Error handling
- Automated testing with pytest

## 🛠️ Technologies Used

- Python
- Pytest

## 📂 Project Structure

```text
Task2_Student_Result_Analyzer/
│
├── main.py
├── result_analyzer.py
├── validators.py
├── models.py
├── test_result_analyzer.py
└── README.md

▶️ How to Run
Run the application using:
python main.py
The application will ask for the student's name, roll number, and subject-wise marks.
🧪 Testing
Automated tests are included using pytest.
Run the tests with:
pytest -q
Test result:
5 passed
📊 Example Result
Student Name: Sakshi Tayade
Roll Number: 101

Subject Marks:
Python: 90
AI: 87
Computer Networks: 85
Mathematics: 95

Total Marks: 330
Percentage: 82.5%
Grade: A
Status: Pass
Highest Marks: Python (90)
Lowest Marks: Mathematics (75)
🎯 Learning Outcomes
Through this project, I practiced:
Python modules and functions
Object-oriented programming concepts
Input validation
Exception handling
Data processing
Result analysis
Automated testing with pytest
Modular project structure
👩‍💻 Author
Sakshi Tayade
