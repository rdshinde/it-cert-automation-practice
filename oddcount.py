def find_it(seq):
    for element in seq:
        count = seq.count(element)
    if count%2 != 0 :
        return element
