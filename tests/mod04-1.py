age = int(input("How old are you? "))

if age >= 18:
    print ("Congrats! You can vote!")
else:
    age = 18 - age
    print (f"You're too young to vote.. You must wait {age} year(s) to vote!")