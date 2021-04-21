def _update_best(best, curr):
    curr += 1
    if curr > best:
        best = curr
    return best, curr

def get_longest(arr, n):
    if n <= 3:
        return len(arr)
    # compute the diff segments
    diffs = [arr[i] - arr[i + 1] for i in range(n - 1)]
    n_diff = n - 1
    i , nr_same, prev_diff= 0, 0, None
    diff_segs = list()
    while i < n_diff:
        if prev_diff is not None:
            if diffs[i] == prev_diff:
                nr_same += 1
            else:
                diff_segs.append( (prev_diff, nr_same) )
                nr_same = 1
                prev_diff = diffs[i]
        else:
            prev_diff = diffs[i]
            nr_same += 1
        i += 1
    diff_segs.append( (prev_diff, nr_same) )
    # compute the possible largest from current
    nr_segs, i, best_prog = len(diff_segs), 0, 2
    while i < nr_segs:
        for_len_prog = back_len_prog = 0
        if i + 2 < nr_segs:
            if diff_segs[i+1][1] == 1 \
            and (diff_segs[i+1][0] + diff_segs[i+2][0]) == 2 * diff_segs[i][0]:
                for_len_prog = diff_segs[i][1] + 2
                if i + 3 < nr_segs and diff_segs[i+2][1] == 1 and diff_segs[i][0] == diff_segs[i+3][0]:
                    for_len_prog += diff_segs[i + 3][1]
        if i > 1:
            if diff_segs[i-1][1] == 1 \
            and (diff_segs[i-1][0] + diff_segs[i-2][0]) == 2 * diff_segs[i][0]:
                back_len_prog = diff_segs[i][1] + 2
                if i > 2 and diff_segs[i-2][1] == 1 and diff_segs[i][0] == diff_segs[i-3][0]:
                     back_len_prog += diff_segs[i - 3][1]
        for_len_prog = max(diff_segs[i][1] + 1, for_len_prog)
        back_len_prog = max(diff_segs[i][1] + 1, back_len_prog)
        best_prog = max(best_prog, for_len_prog, back_len_prog)
        i += 1
    return min(best_prog + 1, n)





def use_testcase():
    cases = [
        [0],
        [5, 1],
        [8, 5, 3],
        [7, 7, 6, 5],
        [8, 6, 6, 5],
        [8, 7, 5, 5],
        [8, 7, 6, 6],
        [8, 7, 6, 5],
        [8, 6, 5, 5],
        [8, 6, 5, 2, 0],
        [10, 8, 6, 6, 2, 0],
        [10, 8, 8, 7, 7, 5, 5, 2, 1]
    ]

    for case_i in range(len(cases)):
        input = cases[case_i]
        longest_lens = get_longest(input, len(input))
        print("Case #{}: {}".format(input, longest_lens))


def use_input():
    total_case = int(input())
    for case_i in range(1, total_case + 1):
        n = int(input())
        arr = map(int(), input().split(" "))
        print(arr)

        longest_lens = get_longest(arr, n)
        print("Case #{}: {}".format(case_i, " ".join(map(str, longest_lens))))

if __name__ == '__main__':
    #use_input()
    use_testcase()
