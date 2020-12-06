def find_nb(m):
    s = 1
    i = 1
    while s < m:
        i += 1
        s += i * i * i
    if s == m:
        return(i)
    else:
        return(-1)
print(find_nb(2025))
