kwh = float(input("Enter kWh usage: "))

if kwh <= 50:
    price = kwh * 0.10
    print (f"Price is : {price}€")

elif kwh <= 200:
    price1 = 50 * 0.10
    kwh -= 50
    price2 = kwh * 0.08
    print (f"Price is : {price1 + price2}€")

elif kwh > 200:
    price1 = 50 * 0.10
    kwh -= 50
    price2 = 150 * 0.08
    kwh -= 150
    price3 = kwh * 0.06
    print (f"Price is : {price1 + price2 + price3}€")