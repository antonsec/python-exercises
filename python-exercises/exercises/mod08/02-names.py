names = set()

while True:
    name = input("Enter the number of a names: ")
    if name == "":
        print ("Ending program")
        break

    elif name in names:
        print (f"Existing name..")

    elif name not in names:
        names.add(name)
        print ("New name..")

print (f"Current names:")
for i in names:
    print (i)