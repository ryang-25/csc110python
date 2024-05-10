# people.py
# Roland Yang
# 5/6/24
# On my honor I have neither given nor received unauthorized aid on this
# assignment

class People():
    def __init__(self, name, age, ssn):
        self.myName = name
        self.myAge = age
        self.mySsn = ssn

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getSsn(self):
        return self.ssn

class Faculty(People):
    def __init__(self, name, age, ssn, jobTitle, experience):
        super.__init__(self, name, age, ssn)
        self.myJobTitle = jobTitle
        self.myExperience = experience

    def getJobTitle(self):
        return self.myJobTitle

    def getExperience(self):
        return self.myExperience

class Student(People):
    def __init__(self, name, age, ssn, gpa, gLevel, major):
        super.__init__(self, name, age, ssn)
        self.myGpa = gpa
        self.myGLevel = gLevel
        self.myMajor = major

    def getGpa(self):
        return self.myGpa

    def getGLevel(self):
        return self.myGLevel

    def getMajor(self):
        return self.myMajor
