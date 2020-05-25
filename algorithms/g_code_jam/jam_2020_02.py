def add_parent(str, cur_min):
    if not str:
        return ''

    new_max = max(str)
    if new_max == cur_min:
        return str
    new_min = min(str)
    diff = int(new_min) - int(cur_min)

    new_str = new_min.join([add_parent(sub_str, new_min)
                            for sub_str in str.split(new_min)])
    return right_n(diff) + new_str + left_n(diff)

def right_n(n):
    return '(' * n

def left_n(n):
    return ')' * n

total_case = int(input())

for case_i in range(total_case):
    str = input()
    str = add_parent(str, 0)
    print("Case #{}: {}".format(case_i + 1, str))
