
from student import Student

def test_student_details():
    s = Student("Chetan", "01FE25BCA001", "ABC College", "Hubli")

    assert s.name == "Chetan"
    assert s.usn == "01FE25BCA001"
    assert s.college == "ABC College"
    assert s.city == "Hubli"
