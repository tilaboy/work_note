class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class TreeNode:
    def __init__(self, value, l, r, p):
        self.value = value
        self.l = l
        self.r = r
        self.p = p


class LinkedList:
    def __init__(self, arr):
        self.length = len(arr)
        next = None
        for index in range(self.length - 1, -1, -1):
            next = ListNode(arr[index], next)
        self.head = next

class Heap:
    def __init__(self, list):
        self.length = list.length
        self.heap =  list

    def _build_max_heap(self):
        for index in range(self.length//2, 0, -1):
            self.max_heapify(index)

    def __str__(self):
        return "{}".format(self.heap[1:self.length+1])


    def _parent(self, ele):
        return ele//2

    def _left(self, ele):
        left = ele*2
        return left if left <= self.length else None

    def _right(self, ele):
        right = ele*2 + 1
        return right if right <= self.length else None

    def max_heapify(self, ele):
        #print(self.heap, ele)
        left = self._left(ele)
        right = self._right(ele)

        if left is not None and self.heap[left] > self.heap[ele]:
            largest = left
        else:
            largest = ele
        if right is not None and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != ele:
            #print("switch {} {}, switch value {} {}".format(largest, ele, self.heap[ele], self.heap[largest]))
            self.heap[ele], self.heap[largest] = self.heap[largest], self.heap[ele]
            self.max_heapify(largest)

    def max_sort(self):
        for index in range(self.length, 1, -1):
            print(self.heap[1])
            self.heap[1], self.heap[index] = self.heap[index], self.heap[1]
            self.length -= 1
            self.max_heapify(1)
            #print(self.heap)

    def insert(self, x):
        self.length += 1
        index = self.length
        self.heap.append(x)
        parent = self._parent(index)
        print("{}, {}: {}, {}".format(index, parent, self.heap[index], self.heap[parent]))
        while parent is not None and self.heap[index] > self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = self._parent(index)

arr = [8, 14, 6, 11, 9, 5, 1, 10, 3, 7, 16, 2, 4, 17]
heap = Heap(arr)
print(heap)
heap._build_max_heap()
print(heap)
#heap.max_sort()
#print(heap.heap[1])

heap.insert(13)
print(heap)
