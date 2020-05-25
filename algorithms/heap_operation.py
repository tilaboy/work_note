


# the index of the heap, start counting with 1

def left_child(node_index):
    return node_index * 2


def right_child(node_index):
    return node_index * 2 + 1

def parent(node_index):
    return int(node_index / 2)

def heap_swap(Heap, index_1, index_2):
    temp = Heap[index_1]
    Heap[index_1] = Heap[index_2]
    Heap[index_2] = temp

def max_heapify(Heap, n, current_root):
    left_child_i = left_child(current_root)
    right_child_i = right_child(current_root)
    #print(current_root, left_child_i, Heap[left_child_i], right_child_i, Heap[right_child_i])
    if left_child_i > n and right_child_i > n:
        return

    if left_child_i <= n and Heap[left_child_i] > Heap[current_root]:
        max_index = left_child_i
    else:
        max_index = current_root

    if right_child_i <= n and Heap[right_child_i] > Heap[max_index]:
        max_index = right_child_i

    if current_root != max_index:
        heap_swap(Heap, max_index, current_root)
        max_heapify(Heap, n, max_index)

def build_heap(Heap, n):

    for i in range(parent(n), 0, -1):
        max_heapify(Heap, n, i)


def heap_sort(arr):
    nr_elements = len(arr)
    arr.insert(0, None)

    build_heap(arr, nr_elements)
    for i in range(nr_elements, 0, -1):
        heap_swap(arr, 1, i)
        max_heapify(arr, i - 1, 1)


def test_max_heapify():
    example = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
    nr_elements = len(example)
    example.insert(0, None)
    max_heapify(example, nr_elements, 2)
    example.pop(0)
    assert example == [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]


def test_build_heapify():
    example = [4, 10, 7, 9, 1, 3, 16, 2, 14, 8]
    nr_elements = len(example)
    example.insert(0, None)
    build_heap(example, nr_elements)
    example.pop(0)
    assert example == [16, 14, 7, 10, 8, 3, 4, 2, 9, 1]



def test_heap_sort():
    example = [27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0]

    heap_sort(example)
    assert example == [None, 0, 1, 3, 4, 5, 7, 8, 9, 10, 12, 13, 16, 17, 27]

test_max_heapify()
test_build_heapify()
test_heap_sort()
