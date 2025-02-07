inpt = '''5 3
1 2 3 100 1000
'''
# n, k = map(int, input("Enter values from the condition:").split())
n, k = map(int, inpt.split())
m = list(map(int, inpt.split()))

def calc_interval(value):
    stall = 1
    length = 0
    for i in range(1, n):
        length += m[i] - m[i - 1]
        if length >= value:
            length = 0
            stall += 1
    return stall >= k

coord_min = 0
coord_max = 10**9

while coord_min <= coord_max:
    middle = (coord_min + coord_max) // 2
    if calc_interval(middle):
        coord_min = middle + 1
    else:
        coord_max = middle - 1

print("The distance should be:", coord_min - 1)
