def get_intervals(total_intervals):
    intervals = []
    for interval in range(total_intervals):
        start, end = map(int, input().split(" "))
        intervals.append([start, end, interval])
    return intervals

total_case = int(input())

for case_i in range(total_case):
    total_intervals = int(input())
    intervals = get_intervals(total_intervals)
    sort_intervals = sorted(intervals, key=lambda ele: ele[0])

    Cameron = 0
    Jamie = 0
    impossible = False
    for interval in sort_intervals:
        if interval[0] >= Cameron:
            Cameron = 0
        if interval[0] >= Jamie:
            Jamie = 0

        if Cameron == 0:
            interval.append('C')
            Cameron = interval[1]
        elif Jamie == 0:
            interval.append('J')
            Jamie = interval[1]
        else:
            impossible = True
            break

    if impossible:
        print("Case #{}: {}".format(case_i + 1, 'IMPOSSIBLE'))
    else:
        seq = [ele[3] for ele in sorted(sort_intervals, key=lambda ele: ele[2])]
        print("Case #{}: {}".format(case_i + 1, ''.join(seq)))
