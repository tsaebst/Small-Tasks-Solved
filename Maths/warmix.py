def katka(n, k, tasks):
    dp = [[float('inf')] * (n + 1) for _ in range(k + 1)]
    for i in range(n + 1):
        dp[0][i] = 0

    for i in range(1, k + 1):
        for j in range(1, n + 1):
            if tasks[j - 1][0] <= i:
                dp[i][j] = min(dp[i][j - 1], dp[i - tasks[j - 1][0]][j - 1] + tasks[j - 1][1])
            else:
                dp[i][j] = dp[i][j - 1]

    if dp[k][n] == float('inf'):
        return -1
    else:
        return dp[k][n]


n, k = map(int, input().split())
tasks = []
for i in range(n):
    a, t = map(int, input().split())
    tasks.append((a, t))

min_time = katka(n, k, tasks)
print(min_time)
