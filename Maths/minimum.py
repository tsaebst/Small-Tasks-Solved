def calculate_stack_sum(n, a, b, c, x0):
    stack = []
    sequence = generate_sequence(n, a, b, c, x0)
    stack_sum = 0

    for num in sequence:
        if num % 5 < 2:
            if stack:
                stack.pop()
        else:
            stack.append(num)
            stack_sum += min(stack)

    return stack_sum


def generate_sequence(n, a, b, c, x0):
    sequence = [x0]

    for _ in range(n - 1):
        x = (a * sequence[-1] * sequence[-1] + b * sequence[-1] + c) % 1000000
        sequence.append(x)

    return sequence


n = int(input())
a, b, c, x0 = map(int, input().split())

result = calculate_stack_sum(n, a, b, c, x0)
print(result)
