banana = float(input("Enter the amount of bananas (kg).\n"))
apple = float(input("Enter the amount of bananas (kg).\n"))
orange = float(input("Enter the amount of bananas (kg).\n"))

result1 = 2.85 * banana
result2 = 3.15 * apple
result3 = 4.05 * orange

total = result1 + result2 + result3

print ("Shopping summary:")
print (f"Bananas: €{result1:>.3f}\nApples: €{result2:>.3f}\nOranges: €{result3:>.3f}\nTotal: €{total:>.2f}")