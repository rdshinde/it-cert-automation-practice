def sum_two_smallest_numbers(numbers):
    a = 0
    b = 1
    mini = []

    for i in numbers:
        while len(mini)<2:
            mini.append(min(lst))
            numbers.remove(min(lst))
    return(mini[0]+mini[1])
