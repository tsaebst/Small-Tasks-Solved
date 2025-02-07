print("Spitkovska Vlada AM BP-1")
n = int(input("number of months n (0 ≤ n ≤ 100): "))
k = int(input("number of rabbits k (0 ≤ k ≤ 10000): "))

def rabbits(n, k):
    if n == 0:
        return 1
    elif n == 1:
        return 2
    elif n < 0 or k < 0:
        pr = "Wrong integer."
        return pr
    else:
        return rabbits(n-1, k) + rabbits(n-1, k) - k

result = rabbits(n, k)
print(result)
