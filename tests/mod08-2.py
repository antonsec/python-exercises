old_list = []
while True:
    n = int(input("Enter number: "))

    if n == 0:
        break

    old_list.append(n)

new_list = sorted(set(old_list))

print (new_list)