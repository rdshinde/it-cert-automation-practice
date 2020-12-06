
def maxProduct(length,lst):
    if len(lst) == length:
        a = 0
        b = 1
        maxi = []

        for i in lst:
            while len(maxi)<2:
                maxi.append(max(lst))
                lst.remove(max(lst))
        return(maxi[0]*maxi[1])

length = int(input())
lst = list(map(int,input().split()))
print(maxProduct(length,lst))
