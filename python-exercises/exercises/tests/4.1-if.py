
usage = float(input("What is your electricty usage? Please enter in (kWh)\n"))
price = 0

if usage <= 50:
    price <= usage * 50
    
elif usage <= 200:
    price = 50 * 10
    price = price + (usage - 50) * 8

else:
    price = 50 * 10 + 150 * 8 + (usage - 200) * 6

print (f"Electrictys price: {price//100:.0f},{price%100:.0f}")