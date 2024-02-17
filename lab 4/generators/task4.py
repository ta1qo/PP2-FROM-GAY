def squares(start, stop):
    while start <= stop:
        yield start**2
        start += 1

[print(x, end=' ') for x in squares(int(input()), int(input()))]

# def ss(start, stop):
#     yield [x**2 for x in range(start, stop)]

# [print(*x) for x in ss(int(input()), int(input()))]