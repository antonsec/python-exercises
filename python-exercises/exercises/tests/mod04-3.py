phys = int(input("Enter your phsyics grade: "))
math = int(input("Enter your mathematics grade: "))
chem = int(input("Enter your chemistry grade: "))

if phys < 50 or math < 50 or chem < 50:
    print ("Scholarship not granted, due to grades(s) being below 50.")
elif chem > 95:
    print ("Congrats! Scholarship granted!")
elif phys > 90 and math > 90:
    print ("Congrats! Scholarship granted!")
else:
    print ("Scholarship not granted, due to grades being too low.")