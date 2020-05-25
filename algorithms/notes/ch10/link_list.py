'''single linked list'''

class ListNode():
    def __init__(self, value, next_node=None):
        self.val = value
        self.next_node = next_node

    def __str__(self):
        return str(sel.val)

class FreeNode():
    def __init__(self, index, next_node=None):
        self.index = index
        self.next_node = next_node


class ListNodeXor():
    def __init__(self, value, next_node=None, prev_node=None):
        self.val = value
        if next_node == None:
            next = 0
        if prev_node == None:
            prev = 0
        self.nn = next_node ^ prev_node

    def __str__(self):
        return str(sel.val)


class SingleLinkedList():
    def __init__(self, arr):
        next_node = None
        for element in range(len(arr) - 1, -1, -1):
            next_node = ListNode(arr[element], next_node)
        self.head = next_node

    def __str__(self):
        arr = []
        x = self.head
        while x is not None:
            arr.append(str(x.val))
            x = x.next_node
        return "head -> " + " -> ".join(arr) + " -> None"

    def reverse(self):
        x = self.head
        x_prev = None
        while x is not None:
            # get the next one, assign as x
            # point the current one to x_prev
            # assign x_prev with current x
            # assign head to the last elements
            x_next = x.next_node
            x.next_node = x_prev
            x_prev = x
            x = x_next
        self.head = x_prev






class SingleLinkedListStack:
    def __init__(self, arr):
        next_node = None
        for element in range(len(arr) - 1, -1, -1):
            next_node = ListNode(arr[element], next_node)
        self.head = next_node

    def pop(self):
        if self.head is not None:
            value = self.head.val
            self.head = self.head.next_node
            return value
        else:
            raise ValueError('empty')

    def push(self, value):
        self.head = ListNode(value, self.head)

    def __str__(self):
        arr = []
        x = self.head
        while x is not None:
            arr.append(x.val)
            x = x.next_node
        return str(arr)

class SingleLinkedListQueue:
    def __init__(self, arr):
        if arr:
            next_node = ListNode(arr[-1], None)
            self.tail = next_node
        else:
            next_node = None
            self.tail = next_node

        for element in range(len(arr) - 2, -1, -1):
            next_node = ListNode(arr[element], next_node)
        self.head = next_node

    def dequeue(self):
        if self.head is not None:
            value = self.head.val
            self.head = self.head.next_node
            return value
        else:
            raise ValueError('empty')

    def enqueue(self, value):
        self.tail.next_node = ListNode(value, None)
        self.tail = self.tail.next_node

    def __str__(self):
        arr = []
        x = self.head
        while x is not None:
            arr.append(x.val)
            x = x.next_node
        return str(arr)

class FreeLinkedNodes:
    def __init__(self, length):
        next = None
        for i in range(self.length-1, -1, -1):
            free_node = FreeNode(i, next)
            next = i

        self.free = i

    def insert(self, index):
        self.free = FreeNode(index, self.free.next)



class DoubleHeadList:
    def __init__(self, length):
        self.length = length
        arr = [0] * self.length
        # three array
        # 0: value
        # 1: next
        # 2: prev
        self.arr = [arr[:], arr[:], arr[:]]
        self.free = 0
        for i in range(self.length - 1):
            self.arr[1][i] = i + 1
        self.arr[1][self.length - 1] = None

    def __str__(self):
        str = 'free from: {}\n'.format(self.free)
        str += '\t{}\n'.format(self.arr[0])
        str += '\t{}\n'.format(self.arr[1])
        str += '\t{}\n'.format(self.arr[2])
        return str

    def insert(self, linkedlist, value):
        # get index from free
        index = self.free
        self.free = self.arr[1][self.free]

        # set value on index array position
        # set next to original next
        self.arr[0][index] = value
        self.arr[1][index] = linkedlist
        self.arr[2][index] = None
        # set next.prev to index
        if linkedlist is not None:
            self.arr[2][linkedlist] = index

        str = '\t{}\n'.format(self.arr[0])
        str += '\t{}\n'.format(self.arr[1])
        str += '\t{}\n'.format(self.arr[2])
        print(str)

        # assign to ll
        linkedlist = index
        return linkedlist

    def build_linkedlist_from_arr(self, arr):
        ll = None
        for value in arr[::-1]:
            ll = self.insert(ll, value)
        return ll

    def search(self, linkedlist, key_value):
        index = linkedlist
        while index is not None:
            if self.arr[0][index] == key_value:
                return index
            index = self.arr[1][index]
        return None


class DoubleHeadXORList:
    def __init__(self, seq):
        self.length = len(seq)
        arr = [0] * self.length
        # three array
        # 0: value
        # 1: nn
        self.arr = [arr[:], arr[:]]
        self.free = seq[0]
        for index, seq_pos in enumerate(seq[:self.length - 1]):

            self.arr[1][seq_pos] = seq[index + 1]
        self.arr[1][seq[-1]] = None

    def __str__(self):
        str = 'free from: {}\n'.format(self.free)
        str += '\t{}\n'.format(self.arr[0])
        str += '\t{}\n'.format(self.arr[1])
        return str

    def insert(self, linkedlist, value):
        # get index from free
        index = self.free
        self.free = self.arr[1][self.free]

        # set value on index array position
        # set next to original next
        self.arr[0][index] = value
        next_value = 0 if linkedlist is None else linkedlist
        prev_value = 0


        self.arr[1][index] = next_value
        # set next.prev to index
        if linkedlist is not None:
            self.arr[1][linkedlist] = index ^ self.arr[1][linkedlist]

        str = '\t{}\n'.format(self.arr[0])
        str += '\t{}\n'.format(self.arr[1])
        print(linkedlist, index)
        print(str)

        # assign to ll
        linkedlist = index
        return linkedlist

    def build_linkedlist_from_arr(self, arr):
        ll = None
        for value in arr[::-1]:
            ll = self.insert(ll, value)
        return ll

    def search(self, linkedlist, key_value):
        index = linkedlist
        prev = 0
        while index is not None:
            if self.arr[0][index] == key_value:
                return index
            nn = self.arr[1][index]
            next = nn ^ prev
            prev = index
            print("current: {}, value: {} => next {}".format(index, self.arr[0][index], next))
            index = next
        return None


sequence=[6,3,2,9,5,7,1,8,0,4]
dll = DoubleHeadXORList(sequence)
print(dll)
l1 =dll.build_linkedlist_from_arr([1,2,3,4,5,6,7,8,9])
print(dll)
print(l1, '\n\n')

prev = 0
cur = l1
for i in range(1,10):
    np = dll.arr[1][cur]
    next = np ^ prev
    print(dll.arr[0][cur])
    prev = cur
    cur = next

dll.search(l1, 7)
