import re

line = input("Input a string: ")
x = re.sub(r"[\s,\.]", ":", line)

print(x)
