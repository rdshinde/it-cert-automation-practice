import re
fileOpen= open('regex_sum_829582.txt')
lst=list()
for line in fileOpen:
    a = re.findall('[0-9]+',line)
    lst = lst + a
sum = 0
for num in lst:
    sum = sum+ int(num)
print(sum)
