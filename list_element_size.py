def friend(x):
    lst = []
    for elements in x:
        if len(elements) == 4:
            lst.append(elements)
    return lst

print(friend(["Ryan", "Kieran", "Mark",]))
