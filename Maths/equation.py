print("Spitkovska Vladyslava")

example = "(1+((2+3)*(4*5)))"

def calc(example):
    nums = []
    curlss_stack = []

    def main():
        curls = curlss_stack.pop()
        num1 = nums.pop()
        num2 = nums.pop()

        if curls == '+':
            result = num1 + num2
        elif curls == '-':
            result = num1 - num2
        elif curls == '*':
            result = num1 * num2
        elif curls == '/':
            result = num1 / num2

        nums.append(result)

    for curl in example:
        if curl.isdigit():
            nums.append(int(curl))
        elif curl == '(':
            curlss_stack.append(curl)
        elif curl == '+' or curl == '-' or curl == '*' or curl == '/':
            while curlss_stack and curlss_stack[-1] != '(' and (
                    curl == '*' or curl == '/' or curlss_stack[-1] == '+' or curlss_stack[-1] == '-'):
                main()
            curlss_stack.append(curl)
        elif curl == ')':
            while curlss_stack and curlss_stack[-1] != '(':
                main()
            curlss_stack.pop()
    while curlss_stack:
        main()

    return nums.pop()


result = calc(example)
print(result)
