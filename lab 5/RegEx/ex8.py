import re

line = input("Input a string: ")
reline = re.split("[A-Z]", line)
[print(x, end="") for x in reline if x != ""]