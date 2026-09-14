old_list = []
while True:
    n = input("Enter a number: ")

    if n == "":
        print ("\nEnding program..")
        break

    old_list.append(int(n))

new_list = set(old_list)

for i in new_list:
    if i > 100:
        print (i)