"""
Exercise 1
Continue
"""

students_names = [
    "Andre",
    "Mattew",
    "Kolin"
]

for name in students_names:
    if name =="Andre":
        continue
        print ("Found him! " + name)
    print ("Currently testing " + name)


"""
Break
"""

students_names = [
    "Andre",
    "Mattew",
    "Kolin"
]

for name in students_names:
    if name =="Andre":
        break
        print ("Found him! " + name)
    print ("Currently testing " + name)