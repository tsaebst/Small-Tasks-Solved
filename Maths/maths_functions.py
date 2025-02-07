'''Create a new Python file called "math_functions.py".
Define a function called "is_prime" that takes one argument (an integer) and returns True if the number is prime, and False otherwise.
Define a function called "factorial" that takes one argument (an integer) and returns the factorial of that number.
Define a function called "fibonacci" that takes one argument (an integer) and returns the nth number in the Fibonacci sequence.
Define a function called "greatest_common_divisor" that takes two arguments (two integers) and returns their greatest common divisor.
Save the file.
Create a new Python file called "test_math_functions.py".
Import the math_functions module into this file.
Write test cases for each of the four functions, making sure to cover different input values and edge cases.
Run the test file and make sure all the tests pass.
Submit both files as your completed task.
Note: You can use any testing framework you like to write the test cases (e.g., unittest, pytest, etc.).'''

def is_prime(num):
    result = False
    if num == 1:
        result = False
        return result
    elif num == 2:
        result = True
        return result
    elif num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return result
    result = True
    return result


def factorial(num):
    if num < 0:
        return -1
    if num <= 1:
        return 1
    res = num * factorial(num - 1)
    return res


def fibonacci(num):
    if num <= 0:
        return None
    elif num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        fib0 = 0
        fib1 = 1
        i = 2
        while i < num:
            fibo = fib0 + fib1
            fib0 = fib1
            fib1 = fibo
            i = i + 1
        return fibo


def greatest_common_divisor(a, b):
    box = []
    if a < 0:
        a = -a
    for i in range(1, a+1):
        check1 = a % i == 0
        check2 = b % i == 0
        if check1 and check2:
                box.append(i)
    new = sorted(box)
    return new[-1]

