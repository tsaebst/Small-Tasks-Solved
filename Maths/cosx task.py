
print("За умови |x|<= p /4 ")
x = float(input("Введіть число:"))
n = int(input("Введіть n:"))
def cosx(x, n):
    if n == 0:
        return 1
    elif n < 0:
        return False
    else:
        switcher = (-1)**n
        step = 1
        for i in range(2, 2*n+1, 2):
            step = step * i
        return switcher * (x**(2*n) / step) + cosx(x, n-1)  #записуємо n! рекурсивно

if x <= (3.14/4):
    print("Результат обчислення:", cosx(x, n))
else:
    print("Число x не входить до заданого інтервалу (-p/4, p/4)")