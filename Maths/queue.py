def queue():
    input_count_and_cshregister = input("Enter the number of people and number of cash registers: ")
    string_list = input_count_and_cshregister.split()
    input_count_and_cshregister = [int(x) for x in string_list]
    time_for_all = []
    groups = []
    maximum_time = 0

    for i in range(input_count_and_cshregister[0]):
        serving_time = int(input(f"Enter the serving time for customer no. {i+1}: "))
        time_for_all.append(serving_time)

    time_for_all.sort()

    for i in range(input_count_and_cshregister[1]):
        group = time_for_all[i::input_count_and_cshregister[1]]
        groups.append(group)

    for group in groups:
        group_sum = sum(group)
        if group_sum > maximum_time:
            maximum_time = group_sum

    print(maximum_time)

queue()