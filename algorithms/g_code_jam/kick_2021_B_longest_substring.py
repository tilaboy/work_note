def get_longest(my_str, n):
    i = 0
    longest_lens = [1]
    sub_len = 1
    i += 1
    while i < n:
        if ord(my_str[i]) > ord(my_str[i-1]):
            sub_len += 1
        else:
            sub_len = 1
        longest_lens.append(sub_len)
        i += 1
    return longest_lens


total_case = int(input())
for case_i in range(1, total_case + 1):
    n = int(input())
    my_str = input()

    longest_lens = get_longest(my_str, n)
    print("Case #{}: {}".format(case_i, " ".join(map(str, longest_lens))))
