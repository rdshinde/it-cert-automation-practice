#Bubble Sort Program
def bubble_sort(arr):
     for i in range(len(arr)-1):
         for j in range(0, len(arr)-i-1):
             if arr[j] > arr[j+1]:
                (arr[j], arr[j+1]) = (arr[j+1], arr[j])
     return arr
a = list(map(int,input().split()))
print('Bubble Sorted Array:\n',bubble_sort(a))
