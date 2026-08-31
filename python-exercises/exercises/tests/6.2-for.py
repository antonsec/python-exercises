list = []
# new_list = []
while True:
    number = input("Give this program a number: ")

    if number == "":
        print ("Ending program..")
        break 

    list.append(int(number)) 

    for i in list:
        if i > 100:
            continue
        else:
            list.remove(i)

list.sort(reverse=True)
myset = set(list)

print (myset)