def from_n_to_zero(n):
    while n >= 0:
        yield n
        n -= 1
        
[print(x, end=' ') for x in from_n_to_zero(int(input()))]