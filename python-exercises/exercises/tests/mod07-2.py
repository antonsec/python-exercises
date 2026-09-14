def update(change):
    new_list = []
    for i in change:
        if len(i) > 5:
            new_list.append(i)
    return new_list

list = ["cat", "dog", "elephant", "lion", "giraffe"]

updated_list = update(list)
print (f"Original list: {list}\nUpdated list: {updated_list}")