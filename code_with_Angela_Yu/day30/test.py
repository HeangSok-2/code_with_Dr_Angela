d = [3, 4 ,5 ,6]

try:
    print(d[4])
except KeyError as meow:
    print(f"the {meow} does not exist")