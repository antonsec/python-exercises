number = int(input("Give any number:\n"))

prime = True

for i in range(2,number):
    if number % i == 0:
        prime = False

if number <= 1:
    prime = False
        
if not prime:
    print (f"{number} is NOT a prime number!")

elif prime == True:
    print (f"{number} is a a prime number!")