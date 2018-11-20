# 07.65 - Intro to Working with Lists
# from typing import List
#
# print("Intro to Working with Lists\n")
# students = ['Max', 'Monika', 'Erik', 'Franziska']
#
# ## Popping off the last value in a list
# last_student = students.pop()
# print(last_student)
# print(students)
#
#
# ## Removing items from a list
# students: List[str] = ['Max', 'Monika', 'Erik', 'Franziska'] + ["Frank"]
# print(students)
#
# ## Delete a certain index item.
# del students[3]
# print(students)
#
# ## Delete a specific value
# students.remove("Monika")
# print(students)
#
# # 07.66 - List Slicing
# print("\nList Slicing\n")
# students = ['Max', 'Monika', 'Erik', 'Franziska']
# print(students)
# ## print second element in list
# print(students[1])
#
# ## List Slicing with Students
# ## print everything but the first student in the list
# print(students[1:])
# ## print the last item in the list.
# print(students[-1:])
# ## print everything but the last element in the list
# print(students[0:-1])
#
# ## Slicing works with Strings
# ## Prints the last 5 characters
# print("\n")
# print("Hello World"[-5:])
# ## Prints the first 5 characters
# print("Hello World"[:5])
#
# # List Comprehensions
# xs = [1,2,3,4,5,6,7,8]
# ## for every element (x) in xs, multiple that element by itself and add it to ys.
# ys = [x * x for x in xs]
# # ys = []
# #
# # for x in xs:
# #     ys.append(x*x)
# print("\n")
# print(xs)
# print(ys)
#
# ## Working with Strings
# students = ['Max', 'Monika', 'Erik', 'Franziska']
#
# ## for every student in students, get the length of the string and append the lengths list.
# lengths = [len(student) for student in students]
# print("\n")
# print(students)
# print(lengths)
#
# #matplotlib inline
# import matplotlib.pyplot as plt
#
# xs = [x/10 for x in range(0,100)]
# # print(xs)
# ys = [x * x for x in xs]
# # print(ys)
#
#
# # plt.plot(xs, ys)
# # plt.show()
#
# # 7.70 Dictionaries in Python
# print("\n")
# d = {"Berlin":"BER", "Helsinki":"HEL","Saigon":"SGN"}
# print(d["Helsinki"])
# ## add value to the dictionary
# d["Budapest"] = "BUD"
# print(d)
# ## remove value from the dictionary
# del d["Budapest"]
# print(d)
# print("\n")

## Query: Is there an element in the dictionary
# if "Budapest" in d:
#     print("Budapest is included in the dictionary")
# if "Saigon" in d:
#     print("Saigon is included in the dictionary")
# print("\n")

## Access elements in the dictionary
# print(d["Saigon"])
# print(d.get("Saigon"))
### this method (w/o get) can error out if value isn't available. use get
# print(d["Hong Kong"])
# print(d.get("Hong Kong"))
# print("\n")

# 7.72 Tuples: Immutable objects
t = (1,2,3)
# print(t)
## cannot append tuples
# print("\n")

## This is a list and is mutable, or changeable. Max Muller can become Max Mustermann.
# person = ["Max Muller", 55]
person = ("Max Muller", 55)

## tuple objects do not support item assignments. AKA you cannot change values in tuples.
# def doSomething(p):
#     p[0] = "Max Mustermann"

# doSomething(person)
# print(person)
# print("\n")

# 7.73 - Working with Tuples
student = ("John Doe", 22, "Informatics")

# name = student[0]
# age = student[1]
# subject = student[2]
# name, age, subject = student
#
# print(subject)
# print("\n")

## tuples as a return type for functions
# def getStudent():
#     return("John Doe", 22, "Informatics")
#
# name, age, subject = getStudent()
#
# print(getStudent())
# print(age)
# print("\n")
#
# students = [("Max Muller", 22),
#             ("Monika Fischer", 27),
#             ("Erik Schrenker", 23)
#             ]
#
# for name, age in students:
#     print(name)
#     print(age)
#
# print("\n")

# 7.74 - Dictionaries and Loops
# d = {"Munich": "MUC", "Budapest": "BUD", "Helsinki":"HEL"}
#
# for key in d:
#     value = d[key]
#     print(key, value)
#
# ## How to turn pairs into tuples
# print(d.items())
#
# ## How to divide up those tuples
# for key, value in d.items():
#     print(key + ": " + value)

# 07.75 - The Dictionary Exercise
# with open("../CourseMaterial/data/names.csv", "r") as file:
#     # count = 0
#     d = {}
#     for line in file:
#         lineSplit = line.strip().split(",")
#         # count = count + 1
#         # print(lineSplit)
#         if lineSplit[1] == "Name":
#             continue
#
#         if lineSplit[1] in d:
#             d[lineSplit[1]] = d[lineSplit[1]] + int(lineSplit[5])
#         else:
#             d[lineSplit[1]] = int(lineSplit[5])
#
#         # if count >= 1500000:
#         #     break
#
# name = ""
# maxOccurances = 0
# for key, value in d.items():
#     if value > maxOccurances:
#         name = key
#         maxOccurances = value
#     else:
#         continue
#

# print("The most popular name is " + name + " with " + str(maxOccurances) + " people named " + name)
# print(d)




# list1 = ["Hello", "Hello", "World", "Hello", "Mars"]

# d = {}
# for element in list1:
#     if element  in d:
#         d[element] = d[element] + 1
#     else:
#         d[element] = 1
#
# print(d)

# 07.77 - Exercise - Dictionaries
## Read the ../data/names.csv file and calculate which name was assigned most often in the whole USA.

# with open("../CourseMaterial/data/names.csv", "r") as file:
#     # create the dictionary for which every name and count will live.
#     d = {}
#     for line in file:
#         # break each line apart into its own list
#         lineSplit = line.strip().split(",")
#         # femove the first line, which has a value of Name
#         if lineSplit[1] == "Name":
#             continue
#
#         name = lineSplit[1]
#         count = int(lineSplit[5])
#
#         # if the Name in the list is already in the dictionary.d, add the value of the births that year to the value field in the dictionary
#         if name in d:
#             d[name] = d[name] + count
#         else:
#             # if not, create the dictionary key with the value of the count that year.
#             d[name] = count
#
# # field to capture the name
# name = ""
# # field to capture the maximum occurances
# maxOccurances = 0
#
# # look at each value in dictionary d
# for key, value in d.items():
#     if value > maxOccurances:
#         name = key
#         maxOccurances = value
#     else:
#         continue
#
#
# print("The most popular name is " + name + " with " + str(maxOccurances) + " people named " + name)


# 07.78 - Nesting Lists
list1 = [["New York", "Chicago", "Los Angeles"], ["Berlin", "Hamburg", "Frankfurt"]]
print(list1[0][1])

students = {
    "Informatics":["Max", "Monika"],
    "History":["Erik", "Franzeska"]
}

print(students["Informatics"][1])