n = int(input())

def last_digit(n):
    a, b = 0, 1
    for i in range(n+2):
        a, b = b, a + b
    return (a-1) % 10

print(last_digit(n))
