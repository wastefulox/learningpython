# Task 1: complete the class, FileReader, so that when calling the lines() method, the file is accessed line by line. The lines() method should then return a list of the lines in the file.

# Task 2: create the class, CsvReader, so that the FileReader is extended to read a csv file instead. It should return a multidimentional list.

# Important: Leave the reading of the file to FileReader, and extend the lines() method in the CsvReader class by the functionality, which is needed, so that the multidimentional list is returned.

class FileReader():
    def __init__(self, fileLoc):
        self.fileLoc = fileLoc

    def lines(self):
        return self.fileLoc
        # with (self.fileLoc, "r") as file:
        #     for line in file:
        #         lineSplit = line.strip().split(";")
        #         return lineSplit

class CsvReader():
    pass

f = FileReader("./file.csv")
print(f.lines())

# expected output:
# [surname, first_name, Doe, John, Miller, Monica]

# f = CsvReader("./file.csv")
# print(f.lines())

# expected output
# [['surname', 'first_name'], ['Doe', 'John'], ['Miller', 'Monica']]