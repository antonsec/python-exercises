import math

def pizza(cm, euro):
    radius = cm / 2
    area = math.pi * radius ** 2
    m2 = area * 10**-4
    price = euro / m2

    return price

diameter1 = float(input("Enter the diameter of the pizza: "))
price_of_pizza1 = float(input("The price of the 1st pizza: "))

diameter2 = float(input("Enter the diameter of the pizza: "))
price_of_pizza2 = float(input("The price of 2nd pizza: "))

result1 = pizza(diameter1, price_of_pizza1)

result2 = pizza(diameter2, price_of_pizza2)


if result1 < result2:
    print (f"First pizza is cheaper at: {result1:1.2f}€/m2")
elif result2 < result1:
    print (f"Second pizza is cheaper at: {result2:1.2f}€/m2")
elif result1 == result2:
    print ("Both pizzas cost the same!")