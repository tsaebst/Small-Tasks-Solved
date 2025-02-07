def exp(x, ep):
    s = 1
    n = 1
    diff = ep + 1
    while diff >= ep:
        term = x**n / math.factorial(n)
        s_old = s
        s = s+term
        diff = abs(s - s_old)
        n = n+1
    return s

x = float(input("x: "))
ep = 0.0001
result = exp(x, ep)
print("e^x =" , result)


def exp_recursive(y, ep, s=1, n=1):
    term = y**n / math.factorial(n)
    s_old = s
    s += term
    diff = abs(s - s_old)
    if diff < ep:
        return s
    else:
        return exp_recursive(y, ep, s, n+1)

y = float(input("x(recursive): "))
ep = 0.0001
result = exp_recursive(y, ep)
print("e^x(recursive): " , result)