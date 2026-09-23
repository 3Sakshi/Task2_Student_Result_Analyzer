from result_analyzer import (
    calculate_result,
    find_highest_subject,
    find_lowest_subject
)


def test_calculate_result():
    marks = {
        "Python": 90,
        "AI": 80,
        "Computer Networks": 70,
        "Mathematics": 60
    }

    result = calculate_result(marks)

    assert result["total"] == 300
    assert result["percentage"] == 75.0
    assert result["grade"] == "B"
    assert result["status"] == "Pass"


def test_fail_result():
    marks = {
        "Python": 80,
        "AI": 30,
        "Computer Networks": 75,
        "Mathematics": 90
    }

    result = calculate_result(marks)

    assert result["status"] == "Fail"


def test_highest_subject():
    marks = {
        "Python": 90,
        "AI": 80,
        "Computer Networks": 70,
        "Mathematics": 60
    }

    assert find_highest_subject(marks) == "Python"


def test_lowest_subject():
    marks = {
        "Python": 90,
        "AI": 80,
        "Computer Networks": 70,
        "Mathematics": 60
    }

    assert find_lowest_subject(marks) == "Mathematics"


def test_zero_marks():
    marks = {
        "Python": 0,
        "AI": 0,
        "Computer Networks": 0,
        "Mathematics": 0
    }

    result = calculate_result(marks)

    assert result["total"] == 0
    assert result["percentage"] == 0.0
    assert result["grade"] == "F"
    assert result["status"] == "Fail"