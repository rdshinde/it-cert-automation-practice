cash = int(input())
coins = 0
while cash>=0:
        if cash//10 != 0:
            coins = coins + (cash // 10)
            cash = cash%10
        if cash//5 != 0:
            coins = coins + (cash // 5)
            cash = cash%5
            if cash = 0:
                break
        if cash//1 != 0:
            if cash == 1:
                coins = coins + 1
                break
            coins = coins + (cash // 1)
            cash =cash%1


print(cash,coins)
