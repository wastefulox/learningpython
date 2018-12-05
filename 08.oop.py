# Chapter 8 - Object Oriented Programming

# 08.81 - The First Steps in Object Orientation
# students = ["Max", "Monika"]
# students.append("Eric")
# print(students)
#
# class Student():
#     def getName(self):
#         print(self.firstname + " " + self.lastname)
#
# eric = Student()
# eric.firstname = "Eric"
# eric.lastname = "Miller"
#
# monica = Student()
# monica.firstname = "Monika"
# monica.lastname = "Fischer"
#
# class Company():
#     def getName(self):
#         print(self.legalName + " " + self.legalType)
#
# c = Company()
# c.legalName = "MTJ Design"
# c.legalType = "LLC"
#
# c.getName()
# eric.getName()
# monica.getName()
#
# def name5x(o):
#     o.getName()
#     o.getName()
#     o.getName()
#     o.getName()
#     o.getName()
#
# name5x(eric)
# name5x(c)

# 08.82 - Object Orientation - Constructors and Changing Properties
# how do we make sure every object has all required attributes - use constructors!

# class Student():
#     # this constructor ensures all attributes and will error out if it is missing an attribute.
#     def __init__(self, firstName, lastName, term):
#         self.firstname = firstName
#         self.lastname = lastName
#         self.term = term
#     def increaseTerm(self):
#         self.term = self.term + 1
#     def getInfo(self):
#         print(self.firstname + " " + self.lastname + ", Semester: " + str(self.term))
#
# eric = Student("Eric", "Miller", 3)
# eric.increaseTerm()
# eric.getInfo()
#
# monica = Student("Monika", "Fischer", 5)
# monica.getInfo()

# 08.84 - Private Properties and Values within Classes
# class Student():
#     def __init__(self, firstname, lastname):
#         self.firstname = firstname
#         self.lastname = lastname
#         # creating a double underscore makes an attribute private
#         self.__term = 1
#
#     def increaseTerm(self):
#         if self.__term >= 9:
#             return
#         self.__term = self.__term + 1
#
#     # allows user to see value without ability to edit it.
#     def getTerm(self):
#         return self.__term
#
#     def info(self):
#         print(self.firstname + " " + self.lastname + ", Semester: " + str(self.__term))
#
#     # functions with underscore should not be used outside of the class. This is developer etiquette.
#     def _doSomething(self):
#         print("doSomething")
#
# eric = Student("Eric", "Johnson")
# eric.increaseTerm()
# print(eric.getTerm())
# # we should not do this...
# eric._doSomething()
# eric.info()

# 08.85 - Encapsulating Data
# Learning why it can worth encapsulating data with object orientation

class Phonebook():
    def __init__(self):
        self.__entries = {}

    def add(self, name, phoneNumber):
        self.__entries[name] = phoneNumber

    def getNumber(self, name):
        if name in self.__entries:
            return self.__entries[name]
        else:
            return None

# book = Phonebook()
# book.add("Miller", "1234567")
# book.add("Fischer", "2345678")

# print(book.getNumber("Fischer"))

# 08.86 - Special Methods that Classes can Implement
# Use the data from 08.85
#
#     def __str__(self):
#         # makes a string out of an object
#         return "Phonebook(" + str(self.__entries) + ")"
#
#     # used when there is no __str__ method.
#     def __repr__(self):
#         return "Phonebook(" + str(self.__entries) + ")"
#
#     def __len__(self):
#         return len(self.__entries)
#
# book = Phonebook()
# book.add("Doe", "1234567")
# book.add("Miller", "3456789")
# print(book)
# print(len(book))

# 08.87 - Inheritance in Python
class Student():
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.term = 1

    def name(self):
        return self.firstname + " " + self.lastname

# workingStudent inherits the name function from Student
class workingStudent(Student):
    def __init__(self, firstname, lastname, company):
        # super class goes back to Student and inherits firstname and lastname
        super().__init__(firstname,lastname)
        self.company = company

    def name(self):
        return "Working Student: " + super().name() + ", " + self.company

student = workingStudent("John","Doe", "ABC Company")
print(student.name())

students = [
    workingStudent("Max","Miller","ABC Company"),
    Student("Monika","Fischer"),
    Student("Erik","Beric"),
    workingStudent("Franziska","Brewer","Beer Company")
]

for student in students:
    print(student.name())