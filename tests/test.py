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


# Largest number
# n1 = int(input("Enter 1st number: "))
# n2 = int(input("Enter 2nd number: "))
# n3 = int(input("Enter 3rd number: "))

# if n1 >= n2 and n1 >= n3:
#     print (f"Largest number: {n1}")
# elif n2 >= n1 and n2 >= n3:
#     print (f"Largest number: {n2}")
# else:
#     print (f"Largest number: {n3}")


# Positive number loop with points
# points = 0
# while True:
#     n = int(input("Enter number: "))
#     if n == 0:
#         break
#     elif n > 0:
#         points += 1
# print (f"Positive numbers: {points}")


# Cities with Lists and reverse print using for x in reversed(y)
# cities = []
# for i in range(5):
#     city = input("Enter city: ")
#     cities.append(city)

# print ("")

# for city in reversed(cities):
#     print (city)


# average funciton
# def average(n1, n2, n3):
#     sum = n1 + n2 + n3
#     average = sum / 3
#     return average

# n1 = int(input("Enter first number: "))
# n2 = int(input("Enter second number: "))
# n3 = int(input("Enter third number: "))

# sum = average(n1, n2, n3)
# print (f"Average: {sum}")


# smalles/biggest/sum
# n1 = int(input("Enter number: "))
# n2 = int(input("Enter number: "))
# n3 = int(input("Enter number: "))
# n4 = int(input("Enter number: "))
# n5 = int(input("Enter number: "))
# n6 = int(input("Enter number: "))

# sum_of_numbers = (n1, n2, n3, n4, n5, n6)
# biggest = max(n1, n2, n3, n4, n5, n6)
# smallest = min(n1, n2, n3, n4, n5, n6)
# x = sum(sum_of_numbers)

# print (f"Smallest: {smallest}\nLargest: {biggest}\nSum: {x}")


# names using dict
# names = []

# for i in range(5):
#     name = input("Enter name: ")
#     names.append(name)

# search = input(("Serach name: "))

# if search not in names:
#     print ("Name not found:")
# else:
#     print ("Name found")


# even function
# def is_even(number):
#     if number % 2 == 0:
#         return True
#     else:
#         return False


# n = int(input("Enter number: "))

# even_odd = is_even(n)

# if even_odd == True:
#     print ("Even")
# else:
#     print ("Odd")

# products using dictionary
# products = {
#     "milk" : 1.29,
#     "bread" : 2.49,
#     "eggs" : 3.99,
#     "apple" : 0.69
# }

# product_name = input("Enter product: ")

# if product_name not in products:
#     print ("Product not found.")
# else:
#     product = products[product_name]
#     print (f"Price: {product} €")


# stopping words with loop and using set for lists
# words = []
# while True:
#     word = input("Enter word: ")
#     if word == "stop":
#         break
#     words.append(word)

# print ("\nWords: ")

# new_words = set(words)

# for word in new_words:
#     print (word)


# student and grades using dict
# students = {
# }

# while True:
#     name = input("Enter student name: ")
#     if name == "stop":
#         break
#     score = int(input("Enter score: "))

#     if score > 50:
#         students[name] = score

# print ("Passed students: ")
# for name in students:
#     print (f"{name}: {students[name]}")


# count_even function
# def count_even(old_list):
#     count = 0
#     for i in old_list:
#         if i % 2 == 0:
#             count += 1
#     return count

# numbers = [3, 8, 12, 5, 7, 10]

# result = count_even(numbers)
# print(result)


# finding smaller number without min()
# def find_smallest(old_list):
#     smallest = old_list[0]
#     for number in old_list:
#         if number < smallest:
#             smallest = number
#     return smallest

# numbers = [8, 3, 12, -4, 7]
# result = find_smallest(numbers)
# print(result)


# list manipulation
# numbers = []
# new_list = []

# for number in range(5):
#     n = int(input("Enter number: "))
#     numbers.append(n)

# number = (numbers)

# sum_of_numbers = sum(number)

# average = sum_of_numbers / 5

# for i in numbers:
#     if i > average:
#         new_list.append(i)
# print (new_list)


# countries using dict
# contries = {
#     'Finland' : 'Helsinki',
#     'Sweden' : 'Stockholm',
#     'Norway' : 'Oslo'
# }

# search = input("Enter coutnry: ")

# if search not in contries:
#     print ("Country not found.")
# else:
#     print (f"Capital: {contries[search]}")


# tuple and set
# person = ("Pierre", 20, "Helsinki")


# print (f"Name: {person[0]}\nAge: {person[1]}\nCity: {person[2]}")


# final boss
# students = {
# }

# while True:
#     name = input("Enter student name: ")
#     if name == "stop":
#         break
#     score = int(input("Enter score: "))

#     students[name] = score

# print ("")

# for name in students:
#     print (f"{name}: {students[name]}")

# count = 0

# for name in students:
#     if students[name] >= 50:
#         count += 1

# print (F"Passed: {count}")


# Study

class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
        
    
class Car(Vehicle):
    def __init__(self, brand, year, doors):
        super().__init__(brand, year)
        self.doors = doors

    def print_information(self):
        print (f"Car:\n{self.brand}\n{self.year}\n{self.doors}")

class Motorcycle(Vehicle):
    def __init__ (self, brand, year, engine_size):
        super().__init__(brand, year)
        self.engine_size = engine_size

    def print_information(self):
        print (f"Motorcycle:\n{self.brand}\n{self.year}\n{self.engine_size}")

car = Car("Toyota", 2022, "4 doors")
motorcycle = Motorcycle("Yamaha", 2024, "689 cc")

car.print_information()
print ("")
motorcycle.print_information()