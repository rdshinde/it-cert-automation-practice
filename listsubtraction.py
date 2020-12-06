def list_diff(a,b):
    for element in a:
        if element in b:
            a.remove(element)
            continue
    return a
print(list_diff([1,2,3,4,2,3,5],[2,3]))
