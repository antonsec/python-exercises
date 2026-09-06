# exnamples
# import math

# print(f"{"Vakio":6s}| {"Arvo":<6s}")
# print ("-----------")
# print(f"{"Pii":6s}: {math.pi:<6.2f}")

# text = '''
# Heres a cool thing
# You can use instead of print
# This is much easier.
# '''

# print (text)

# Practise

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

student1 = Student("Alex", 20, 4)
student2 = Student("Emma", 22, 5)

student1.grade += 1

print (f"{student1.name} is {student1.age} years old and has grade {student1.grade}.")
print (f"{student2.name} is {student2.age} years old and has grade {student2.grade}.")