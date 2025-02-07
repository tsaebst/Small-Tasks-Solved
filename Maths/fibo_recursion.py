
def fibo_rec(f):
    if f <= 1:
        return f
    return(fibo_rec(f-1) + fibo_rec(f-2))
input_fibo = int(input("Порядковий номер в послідовності:"))
if input_fibo <= 0:
   print(-1)
else:
    print("Число:")
    print(fibo_rec(input_fibo))

