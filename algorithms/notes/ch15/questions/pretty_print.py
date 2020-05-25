def pretty_print(token_lengths, start_id, end_id, penalty_m, line_break_m, max_line_length=10):
    '''
    print lines with least cubic of number of spaces

    param:
    tokens: a list of tokenized phrases

    output:
    xxx

    notes:
    - assume all token_length is less than max_line_length
    '''
    id = start_id
    total_length = token_lengths[id]
    best_penalty = float('inf')
    best_break = None
    if penalty_m[start_id] is not None:
        return penalty_m[start_id]

    while total_length <= max_line_length and id <= end_id:
        if id == end_id:
            best_penalty = 0
            best_break = id
            id = id + 1
        else:
            penalty = (max_line_length - total_length) ** 3 + \
                      pretty_print(token_lengths, id + 1, end_id,
                                   penalty_m, line_break_m)

            if penalty < best_penalty:
                best_penalty = penalty
                best_break = id
                print('best_penalty at: {} => {}, id {}, len {}, dis {}'.format(start_id, end_id, id, token_lengths[id], max_line_length - total_length))
            id += 1
            total_length = total_length  + 1 + token_lengths[id]

    penalty_m[start_id] = best_penalty
    line_break_m[start_id] = best_break

    return best_penalty

def pretty_print_bu(token_lengths, max_line_length=10):
    nr_tokens = len(token_lengths)

    penalty_m = [None] * nr_tokens
    line_break_m = [None] * nr_tokens

    penalty_m[nr_tokens - 1] = 0
    line_break_m[nr_tokens - 1] = nr_tokens

    for i in range(nr_tokens -2, -1, -1):
        # penalty at i = for any posible cut, penalty on the line + penalty_m[i-k]
        best_penalty = float('inf')
        best_line_break = None
        line_break = i
        total_length = token_lengths[i]

        while total_length <= max_line_length and line_break <= nr_tokens - 1:

            if line_break == nr_tokens - 1:
                penalty = 0
                line_break += 1

            else:
                penalty = (max_line_length - total_length) ** 3 + penalty_m[line_break + 1]
                line_break += 1
                total_length += token_lengths[line_break] + 1

            if penalty < best_penalty:
                best_penalty = penalty
                penalty_m[i] = best_penalty
                line_break_m[i] = line_break - 1

    print(penalty_m)
    print(line_break_m)

    return penalty_m, line_break_m

x = [3,4,5,2,3,4,1,2,3,2,3]
penalty_m = [None] * len(x)
line_break_m = [None] * len(x)
pretty_print(x, 0, len(x) - 1, penalty_m, line_break_m)
print(penalty_m)
print(line_break_m)

penalty_m, line_break_m = pretty_print_bu(x)

n = 0
print(x)
while n < len(x):
    penalty = penalty_m[n]
    line_break = line_break_m[n]
    print(x[n:line_break+1], penalty)
    n = line_break + 1
