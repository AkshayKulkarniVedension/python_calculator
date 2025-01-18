def add(*args):
    return sum(args)

# print(add(10,20,30))

# help(sum)

def sub(a, b):
    return (a - b)

def multiply(*args):
    total = 1
    for i in args:
        total = total * i
    return total

# print(multiply(2,2,2))

def divide(a, b):
    return a/b
