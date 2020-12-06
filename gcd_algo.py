import math
def calcgcd(a,b):
    return math.gcd(a,b)
a = list(map(int,input().split()))
print(calcgcd(a[0],a[1]))
