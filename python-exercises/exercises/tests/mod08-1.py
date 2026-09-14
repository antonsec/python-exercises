fruits = {

}

fruit1 = input("Enter 1st fruit: ")
fruit2 = input("Enter 2nd fruit: ")
fruit3 = input("Enter 3rd fruit: ")


price1 = float(input(f"\nEnter {fruit1}'s kg: "))
price2 = float(input(f"Enter {fruit2}'s kg: "))
price3 = float(input(f"Enter {fruit3}'s /kg: "))

fruits[fruit1] = price1
fruits[fruit2] = price2
fruits[fruit3] = price3

print (fruits)