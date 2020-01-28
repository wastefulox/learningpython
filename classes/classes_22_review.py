class SortedList(list):
  def append(self, value):
    super().append(value)
    self.sort()

students = SortedList(['john','james','jordon'])
print(students)
students.append('jamie')
print(students)