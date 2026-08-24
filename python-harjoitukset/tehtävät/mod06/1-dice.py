import random
times = int(input("How many dice do we roll? "))

total = 0
for i in range(times):
    i = random.randint(1,6)
    #checking if porgram actually works: print (i)
    total += i
print (total)