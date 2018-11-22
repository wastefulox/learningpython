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

# 08.84 -