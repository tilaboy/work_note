import sys

def _revers(arr):
    return arr[::-1]

def _comple(arr):
    return ''.join(['1' if ele=='0' else '0' for ele in arr])

def _both(arr):
    return _revers(_comple(arr))

def f_10(pos_f, pos_s):
    '''from the middle towards two sides'''
    first_half_feed = f_5(pos_f)
    secon_half_feed = f_5(pos_s)
    return first_half_feed + secon_half_feed

def f_5(pos):
    feedback = ''
    for i in range(pos, pos + 5):
        print(str(i), flush=True)
        feedback += input()
    return feedback

def get_valid_feedback(n, step, shift=1):
    feedback = ''
    for i in range(shift, n*5 + shift, step):
        print(str(i), flush=True)
        feedback += input()
    return feedback


def get_possible_validation(feedbacks):
    possible_valid = []

    for feedback in feedbacks:
        viaritions = [
            feedback,
            _revers(feedback),
            _comple(feedback),
            _both(feedback)
        ]
        possible_valid.append(viaritions)
    return possible_valid

def get_matched_index(valid_string, possible_strs, shift=0):
    possiblity = []
    for index, possible_str in enumerate(possible_strs):
        if possible_str[shift:].startswith(valid_string):
            possiblity.append(index)
    return possiblity

def possible_match_10(validation_feedback, possible_valid, shift):
    indices = []
    for i in range(len(possible_valid)):

        possible_i = get_matched_index(validation_feedback[i],
                                       possible_valid[i],
                                       shift)
        indices.append(possible_i)
    return indices


def possible_match_2(validation_feedback, possible_valid, use_bit):
    indices = []
    for i in range(len(possible_valid)):
        start = 5 * i
        indices.append(get_matched_index(validation_feedback[start:start+use_bit], possible_valid[i]))
    return indices


def restore_orig(arr):
    if not arr:
        return ''
    else:
        string = arr.pop(0)
        return string[:5] + restore_orig(arr) + string[5:]


total_case, length = map(int, input().split(" "))
nr_queries = 150

for case_i in range(total_case):
    pos_f = 1
    pos_s = length - 5 + 1

    feedbacks = []
    while pos_f < pos_s:
        feedbacks.append(f_10(pos_f, pos_s))
        pos_f += 5
        pos_s -= 5


    #print(feedbacks, file=sys.stderr)
    nr_pieces = len(feedbacks)
    if nr_pieces == 2:
        # send more and align

        validation_feedback = get_valid_feedback(2, 1)
        possible_valid = get_possible_validation(feedbacks)
        indices = possible_match_2(validation_feedback, possible_valid, 5)
        validated_string = [possible_valid[0][indices[0][0]], possible_valid[1][indices[1][0]]]
        guessed = restore_orig(validated_string)

    elif nr_pieces == 10:
        possible_valid = get_possible_validation(feedbacks)
        all_indices = []
        for shift in range(0,5):
            validation_feedback = get_valid_feedback(10, 5, shift + 1)
            indices = possible_match_10(validation_feedback, possible_valid, shift)
            all_indices.append(indices)
        validated_string = [possible_valid[i][indices[i][0]] for i in range(10)]
        guessed = restore_orig(validated_string)
    else:
        guessed = ''.join(feedbacks)
    print(guessed, flush=True)
    ok = input()
    #print(ok, file=sys.stderr)
