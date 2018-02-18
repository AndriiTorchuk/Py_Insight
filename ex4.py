
students = []

def read_file ():
    try:
        f = open("Students.txt", "r")
        for student in f.readlines():
            students.append(student)
        f.close()
    except Exception:
        print("Can't read file")

"""def read_students(f):
    for line in f:
        yield line"""

read_file()
print(students)