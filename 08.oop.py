# Chapter 8 - Object Oriented Programming

# 08.81 - The First Steps in Object Orientation
students = ["Max", "Monika"]
students.append("Eric")
print(students)

class Student():
    def getName(self):
        print(self.firstname + " " + self.lastname)

eric = Student()
eric.firstname = "Eric"
eric.lastname = "Miller"

monica = Student()
monica.firstname = "Monika"
monica.lastname = "Fischer"

class Company():
    def getName(self):
        print(self.legalName + " " + self.legalType)

c = Company()
c.legalName = "MTJ Design"
c.legalType = "LLC"

c.getName()
eric.getName()
monica.getName()

def name5x(o):
    o.getName()
    o.getName()
    o.getName()
    o.getName()
    o.getName()

name5x(eric)
name5x(c)