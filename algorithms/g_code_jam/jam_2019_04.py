import sys

total_case = int(input())
for case_i in range(total_case):
    nr_works, nr_brokens, nr_calls = map(int, input().split(" "))
    # nr of works can't be zero
    bin_strings = [format(work_i, '05b')[-5:] for work_i in range(nr_works)]
    output = []
    for i_call in range(5):
        test_store = "".join([bin_string[i_call] for bin_string in bin_strings[:nr_works+1]])
        print(test_store, flush=True)
        feedback = input()
        output.append(feedback)

    nr_avai_workers = nr_works - nr_brokens
    number_strings = [''.join([string[char_i] for string in output])
                     for char_i in range(nr_avai_workers)]
    workers = [int(number, 2) for number in number_strings]
    broken = []
    i_block = 0
    block = []
    prev_worker = -1
    expected = list(range(32))
    for worker in workers:
        if worker < prev_worker:
            broken.extend([w + 32 * i_block for w in expected if w not in block])
            i_block += 1
            block = []
        block.append(worker)
        prev_worker = worker
    broken.extend([w + 32 * i_block for w in expected if w not in block])
    print(" ".join([str(worker) for worker in sorted(broken) if worker < nr_works]))
    result = input()
