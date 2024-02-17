def squares(n):
    x = 1
    while x <= n:
        yield x**2
        x += 1
    
[print(x, end=' ') for x in squares(int(input()))]