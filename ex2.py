"""
Exercise 2
Exceptions
"""

student = {
    "name": "Andre",
    "id": 17,
    "feedback": None
}

student["lastname"] = "Sanki"
try:
    lastname = student["lastname"]
    number_lastname = 5 + lastname
except KeyError:
    print("Error lastname")
except TypeError as Error:
    print("Cant add this two together")
    print(Error)

print("This code end!")