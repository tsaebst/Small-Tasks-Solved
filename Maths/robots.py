def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    merged = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i][0] < right[j][0] or (left[i][0] == right[j][0] and left[i][1] < right[j][1]):
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    while i < len(left):
        merged.append(left[i])
        i += 1

    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged


# Reading input data
N = int(input())
robots = []
for _ in range(N):
    main, auxiliary = map(int, input().split())
    robots.append((main, auxiliary))

# Sorting the list of robots
sorted_robots = merge_sort(robots)

# Output the sorted list
for robot in sorted_robots:
    print(robot[0], robot[1])
