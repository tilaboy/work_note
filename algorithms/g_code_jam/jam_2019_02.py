def _get_case():
    size = input()
    steps = input()
    return int(size), steps

def _rev(steps):
    rev_steps = ['E' if step=='S' else 'S' for step in steps]
    return ''.join(rev_steps)

total_case = int(input())

for i in range(total_case):
    size, steps = _get_case()
    if size < 2:
        print("Case #{}: {}".format(i+1, ''))
    else:
        print("Case #{}: {}".format(i+1, _rev(steps)))
