#Selection Sort Program
def Selection_Sort(arr):
    for i in range(len(arr)):
         middle = i
         for j in range(i+1, len(arr)):
             if arr[middle] > arr[j]:
                 middle = j
         (arr[i], arr[middle]) = (arr[middle], arr[i])
    return arr
a = list(map(int,input().split()))
print('Selection Sorted Array:\n',Selection_Sort(a))
