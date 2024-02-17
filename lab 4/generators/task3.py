def div_by_3and4(n):  #If a number is divisible by 3 and 4, then it is also divisible by 12.
    x = 12
    while x <= n:
        yield x
        x += 12

[print(x, end=' ') for x in div_by_3and4(int(input()))]
