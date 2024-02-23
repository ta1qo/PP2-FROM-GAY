import re

line = input("Input a snake case: ")
reline = re.split(r"[_]+", line)
[print(x.capitalize(), end="") for x in reline]

# this_is_snake_case
# ThisIsCamelCase
