def cut_down_list(numbers):
    new_list = []
    
    for i in numbers:
        new_list.append(i)

    for i in new_list:
        if i % 2 != 0:
            new_list.remove(i)
        elif i % 2 == 0:
            new_list.append(i)
            break

    return new_list

old_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
new_list = cut_down_list(old_list)
print (new_list)