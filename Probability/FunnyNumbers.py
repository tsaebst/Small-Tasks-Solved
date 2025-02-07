first = str(input("first: "))
second = str(input("second: "))

def pattern_check(first, second):
    if len(first) != len(second):
        return False
    for a, b in zip(first, second):
        if first.index(a) != second.index(b):
            return False
    return True

print(pattern_check(first, second))