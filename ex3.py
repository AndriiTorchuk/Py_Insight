"""
Exercise 1
=== Open, Read, Write ===
"""

students = []

def get_st_title():
    st_title = []
    for student in students:
        st_title.append(student["name"].title())
    return st_title

def print_st_title():
    st_title = get_st_title()
    print(st_title)

def add_st(name, id):
    student = {"name": name, "id": id}
    students.append(student)
"""
=== Writing and reading functions ===
"""

def save_file (student):
    try:
        f = open("Students.txt", "a")
        f.write(student + "\n")
        f.close()
    except Exception():
        print(" Could not save file")

def read_file():
    try:
        f = open("Students.txt", "r")
        for student in f.readlines():
            add_st(student, id)
        f.close()
    except Exception():
        print("Could not read file")

"""
===========
"""

read_file()
print_st_title()

st_name = input("Enter student name: ")
st_id = input("Enter student id: ")

add_st(st_name, st_id)
save_file(st_name)
