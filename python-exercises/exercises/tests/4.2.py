phys = int(input("What was your perfomance for Physics? "))
math = int(input("What was your perfomance for Mathematics? "))
chem = int(input("What was your perfomance for Chemistry? "))

if phys < 50 or math < 50 or chem < 50:
    print ("Scholatship denied, because a certain grade is not over 50.")

elif chem > 95:
    print ("Congrats! Scholarship granted!")

elif (phys >= 90) and (math >= 90):
    print ("Congrats! Scholarship granted!")

else:
    print ("Scholatship denied, because grades too low")