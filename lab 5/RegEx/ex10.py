import re

line = input("Input a camel case: ")
reline = re.findall(r"[A-Z][a-z]*", line)
print('_'.join(reline).lower())
