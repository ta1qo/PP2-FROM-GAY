import re

line = input("Input a string: ")
x = re.search(r"[A-Z][a-z]+", line)

if x == None:
    print("Not found!")
else:
    print(f"Found at {x.span()} as {x.group()}")
