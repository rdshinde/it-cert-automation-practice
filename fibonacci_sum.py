def fib_last_digit(n):
    lst = []
    sum = 0
    if n < 2: return n
    else:
        a, b = 0, 1
        for i in range(1,n):
            a, b = b, (a+b)
            lst.append(b)
            for element in lst:
                sum = sum + element
                lst.remove(element)
        print(sum % 10)
n = int(input())
fib_last_digit(n)
