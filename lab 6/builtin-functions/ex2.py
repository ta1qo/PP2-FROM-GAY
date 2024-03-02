string = input()
print("number of upper case letters:", len([ch for ch in string if ch.isupper()]))
print("number of lower case letters:", len([ch for ch in string if ch.islower()]))
