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

usage = float(input("What is your electricty usage? Please enter in (kWh)\n"))

if usage <= 50:
    price = usage * 50
    print (f"The price of the electricty is {price} cents.")