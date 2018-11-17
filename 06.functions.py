# 06.02 - Functions 01
## This is calling the standard "print" function
# print("Hello World")
# print("\n")

## Creating our own functions
def multiPrint():
    print("Hello")
    print("World")

# multiPrint()
# multiPrint()
# print("\n")

## Building a function with parameters
def multiPrint2(name):
    print("Hello " + name)

# multiPrint2("Mat")
# multiPrint2("Jon")
# print("\n")

# 06.03 - Functions 02
def multiPrint3(name, count):
    for i in range(0, count):
        print(name)

# multiPrint3("Mat", 10)
# print("\n")

## Functions calling functions
def anotherFunction():
    multiPrint3("Hello", 3)
    multiPrint3("World", 3)

# anotherFunction()
# print("\n")

## comparing values within a function
def maximum(a,b):
    if a > b:
        print("The greater value is " + str(a))
    elif a < b:
        print("The greater value is " + str(b))
    else:
        print("The values are the same")

# maximum(30,14)
# print("\n")

# 06.04 - Quick Look @ Objects
list1 = [1,2,3]
# print(list1)

list1.append(4)
# print(list1)
# print("\n")
#
# print("Hello, world".split(","))

# 06.06 - Opening Files
# file = open("read.txt", "r")
# for line in file:
#     # strip gets rid of line breaks in files
#     print(line.strip())

# 06.08 - Write Files
## "w" writes to a new file or overwrites everything in the file.
# file = open("write.txt", "w")
## "a" appends the file and adds content to it.
file = open("write.txt", "a")
# file.write("pseudo text content\n")
# file.write("More pseudo text content\n")
# students = ["Max", "Erik", "Monika", "Franziska"]
# for student in students:
#     file.write(student + "\n")
file.close()

# 06.09 - With Construct
## prevents excessive resource usage
# with open("read.txt", "r") as file:
    # for line in file:
    #     print(line.strip())

# 06.10 - Read a CSV

# with open("file.csv") as file:
#     for line in file:
#         ## takes each line and creates a list from it, splitting on the semicolon. USEFUL
#         data = (line.strip().split(";"))
#         print(data[0] + " Population: " + data[1] + " / Airport Shortcut: " + data[2])
# print("\n")

# 06.11 Read CSV and Skip Data
# with open("file.csv") as file:
#     for line in file:
#         data = (line.strip().split(";"))
#         if int(data[1]) < 2000000:
#             continue
#         if data[2] == "BUD":
#             continue
#         print(data)

#matplotlib inline
# import matplotlib.pyplot as plt
#
#
# xs = [1,2,3]
# ys = [4,7,5]
#
# plt.plot(xs, ys)
# plt.show()


# 06.15 - Birth Statistics Graphic

name = "Max"
beginYear = 1950
endYear = 2000
gender = "M"
state = "CA"

with open("../CourseMaterial/data/names.csv", "r") as file:
    totalBirths = 0
    for line in file:
        lineSplit = (line.strip().split(","))
        #
        if lineSplit[1] == name and lineSplit[3] == gender and lineSplit[4] == state and int(lineSplit[2]) >= beginYear and int(lineSplit[2]) <= endYear:
            totalBirths = totalBirths + int(lineSplit[5])
    print(totalBirths) # for max, it returns 6385