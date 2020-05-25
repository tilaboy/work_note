'''allocate object and free object from a free list'''

ARR = [[0] * 8] * 3
FREE = None

def get_next(x):
    return ARR[0][x]

def set_next(x, value):
    global ARR
    ARR[0][x] = value

def get_prev(x):
    return ARR[2][x]

def set_prev(x, value):
    global ARR
    ARR[2][x] = value

def get_value(x):
    return ARR[1][x]

def set_value(x, value):
    global ARR
    ARR[1][x] = value

def allocate_object():
    global FREE
    if FREE == None:
        raise ValueError('no space avaialble')
    else:
        x = FREE
        FREE = get_next(x)
        set_next(x, None)
    return x

def free_object(x):
    global FREE
    set_next(x, FREE)
    FREE = x

def insert(ll, value):
    x = allocate_object()
    set_next(x, ll)
    set_prev(x, None)
    set_prev(ll, x)
    set_value(x, value)
    ll = x
    return ll

def shift(ll):
    next_node = get_next(ll)
    free_object(ll)
    ll = next_node
    set_prev(ll, None)
    return ll

def print_ll(ll):
    print("free: {}\tll: {}".format(FREE, ll))
    print(ARR[0])
    print(ARR[1])
    print(ARR[2])

FREE = 3
ll = 6
ARR[0] = [None, 2, None, 7, 1, 0, 4, 5]
ARR[1] = [0, 3, 1, 0, 16, 0, 9, 0]
ARR[2] = [0, 4, 1, 0, 6, 0, None, 0]

print_ll(ll)
ll = shift(ll)
print_ll(ll)
ll = insert(ll, 20)
print_ll(ll)
ll = insert(ll, 25)
print_ll(ll)
ll = shift(ll)
print_ll(ll)
