def converter(gallons): # were making a program that requires 1 parameter (gallons)
    gasoline = gallons * 3.78541 # converting gallons to liters
    return gasoline # returning gallons to liters

while True:
    gallons = input("How many gallons do you want to convert? ") # asking in str because we need to check if user inputs empty string
    if gallons == "": # if user inputs empty string == ends program
        break
    liters = converter(float(gallons)) # converting gallons from str to float and adding it to liters
    print(f"{liters:.2f} liters") # printing dice with a .2 decimal range