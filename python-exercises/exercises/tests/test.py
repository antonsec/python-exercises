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


class Koira:
    def __init__(self, rotu, nimi, vuosi):
        self.rotu = rotu
        self.nimi = nimi
        self.vuosi = vuosi
k1 = Koira('Bichon', 'Bianco', 2006)

print (f"{k1.nimi} on {k1.rotu}. Hän on synytnyt {k1.vuosi}.")