import re

line = input("Input a string: ")
x = re.findall(r"[A-Z][a-z]*", line)
print(" ".join(x))
