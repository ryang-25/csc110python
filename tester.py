# tester.py
# Roland Yang
# 5/6/24
# On my honor I have neither given nor received unauthorized aid on this
# assignment

from people import *

def main():
    person = People("John Smith", 12, "1234567890")
    assert person.getName() == "John Smith"
    assert person.getAge() == 12
    assert person.getSsn() == "1234567890"

    faculty = Faculty("John Smith", 12, "1234567890",
        "Underwater Ceramics Technician", 10)
    assert faculty.getJobTitle() == "Underwater Ceramics Technician"
    assert faculty.getExperience() == 10
    assert faculty.getName() == "John Smith"

    student = Student("John Smith", 12, "1234567890", 3.0, 11, "Dishwashing")
    assert student.getGpa() == 3.0
    assert student.getGlevel() == 11
    assert student.getMajor() == "Dishwashing"
