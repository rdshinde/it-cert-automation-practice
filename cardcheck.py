# Program to check whether the Bank card is valid or not.

cardNum = input('Enter your credit card number: ')
oddNum = cardNum[::2]
evenNum = cardNum[1::2]
multiOddNum = []
for num in oddNum:
    multiOddNum.append(int(num) * 2)
#print(multiOddNum)
sum_evenNum = sum(list(map(int,str(evenNum))))
#print(sum_evenNum)
sum_oddNum = 0
for num in multiOddNum:
    if num//10==1 and num!=0:
        sum_oddNum = sum_oddNum+1
    digit = num % 10
    sum_oddNum = sum_oddNum+digit
    num = num//10
#print(sum_oddNum)
first=int(cardNum[:1])
second=int(cardNum[1:2])
if (sum_oddNum+sum_evenNum)%10==0:
    if first==4 and (len(cardNum)==13 or len(cardNum)==16):
        print('\nCard is of VISA.')
    elif first==5 and len(cardNum)==16:
        print('\nCard is of MASTERCARD.')
    elif first==6 and len(cardNum)==16:
        print('\nCard is of DISCOVER.')
    elif first==3 and (second==4 or second==7) and len(cardNum)==15:
        print('\nCard is of AMERICAN EXPRESS.')
    elif first==3 and (second==0 or second==6 or second==8) and len(cardNum)==14:
        print('\nCard is of DINNER CLUB.')
else:
    print('Invalid Card Number')
