talent = float(input("Enter talents:\n"))
pound = float(input("Enter pounds:\n")) 
lot = float(input("Enter lots:\n"))

talent = talent * 8512
lot = lot * 13.3
pound = pound * 425.6

sum = talent + lot + pound


print(f"Total weight in modern units: \n{int (sum / 1000)} kilograms and {round((sum % 1000),2)} grams.")