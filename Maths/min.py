print("Spitkovska Vladyslava AM BP-1")


def minimum():
    stack = []
    num_list = input().split()
    nums = int(num_list[0])
    num1, num2, num3, x0 = map(int, num_list[1:])
    for i in range(nums):
        m_num = ((num1 * x0 * x0 + num2 * x0 + num3) // 100) % (10**6)
        if m_num % 5 < 2:
            if stack:
                stack.pop()
        else:
            stack.append(m_num)
        x0 = m_num
    print(sum(stack))


minimum()
