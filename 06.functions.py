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
with open("read.txt", "r") as file:
    # for line in file:
    #     print(line.strip())




