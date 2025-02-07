
from maths_functions import *

def checker():
    while True:
        try:
            a = int(input("Enter the number:"))
        except:
            print("Try to input an integer")
        ask = input('''
What  we can check:
Prime numbers
Factorial
Fibonacci number
The greatest common divisor
Quit
>>>''').lower()
        try:
            if ask.startswith("p"):
                check = is_prime(a)
                if a < 0:
                    error = int(str("this line will break this part of code"))
                if not check:
                    print("Number is not prime")
                else:
                    print("The number is prime. ")
            elif ask.startswith("fa"):
                check = factorial(a)
                if check == None:
                    print("You can not take the factorial of this number.")
                else:
                    print(check)
            elif ask.startswith("fi"):
                check = fibonacci(a)
                if check == None:
                    error = int(str("this line will break this part of code"))
                print(f"The fibonacci nimber with index {a} is: ",check)
            elif ask.startswith("t"):
                b = int(input("Enter the second number: "))
                print(greatest_common_divisor(a, b))
            elif ask.startswith("q"):
                break
        except:
            print("Wrong number was set.")


checker()