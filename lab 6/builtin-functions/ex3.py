string = input()
print(all([True if string[x] == string[-(x + 1)] else False for x in range(len(string))]))
