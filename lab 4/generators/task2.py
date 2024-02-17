def even(n):
    x = 0
    while x <= n:
        yield x
        x += 2

[print(x, end=', ') for x in even(int(input()))]