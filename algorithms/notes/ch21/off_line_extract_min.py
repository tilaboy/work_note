from unittest import TestCase
import logging

def _prepare_k_arr(input):
    i = 0
    k_arr = dict()
    curr_arr = list()
    for ele in input:
        if ele == 'E':
            k_arr[i] = list(curr_arr)
            curr_arr = list()
            i += 1
        else:
            curr_arr.append(ele)
    return k_arr

def _prepare_k_ll(input):
    i = 0
    k_arr = dict()
    curr_arr = list()
    for ele in input:
        if ele == 'E':
            if curr_arr:
                k_arr[i] = LinkedList(sorted(curr_arr))
            else:
                k_arr[i] = LinkedList(list())
            curr_arr = list()
            i += 1
        else:
            curr_arr.append(ele)
    return k_arr

class LinkedNode:
    def __init__(self, val, next=None, head=None):
        self.val = val
        self.next = None
        self.head = None


    def __str__(self):
        return '{}'.format(self.val)

class LinkedList:
    def __init__(self, arr):
        self.head = None
        prev = None
        for ele in arr:
            node = LinkedNode(ele)
            if prev:
                prev.next = node
            else:
                self.head = node
            node.head = self.head
            prev = node
        self.tail = prev

    def update_head(self, node):
        self.head = node
        prev_node = node
        while node is not None:
            node.head = self.head
            prev_node = node
            node = node.next
        self.tail = prev_node

    def __str__(self):
        repr = 'node:'
        if self.head:
            node = self.head
            while node:
                repr += ' {}'.format(node.val)
                node = node.next
        return repr

    def l_add(self, list2):
        start1 = self.head
        start2 = list2.head
        logging.debug("merging: ll1: head {}, tail {}, ll2: head {}, tail {}".format(
                         self.head, self.tail, list2.head, list2.tail))

        if not start1:
            self.head = list2.head
            self.tail = list2.tail

        elif not start2:
            pass

        else:
            self.head = start1 if start1.val <= start2.val else start2
            prev = None
            while start1 and start2:
                if start1.val <= start2.val:
                    start1.head = self.head
                    if prev:
                        prev.next = start1
                    prev = start1
                    start1 = start1.next
                else:
                    start2.head = self.head
                    if prev:
                        prev.next = start2
                    prev = start2
                    start2 = start2.next
            logging.debug("in merging: {}, and start1:{}, start2:{}".format(self.head, start1, start2))

            while start1:
                prev.next = start1
                start1.head = self.head
                prev = start1
                start1 = start1.next


            while start2:
                prev.next = start2
                start2.head = self.head
                prev = start2
                start2 = start2.next

            self.tail = prev
        logging.debug("finished merging: {} -> {}".format(self.head, self.tail))


class TestExtractMin(TestCase):
    def setUp(self):
        self.cases = [
            {
                'input': [4, 8, 'E', 3, 'E', 9, 2, 6, 'E', 'E', 'E', 1, 7, 'E', 5],
                'output': [4, 3, 2, 6, 8, 1],
                'name': 'case 1'
            },
            {
                'input': [14, 8, 'E',
                          23, 'E',
                          9, 12, 6, 'E',
                          'E',
                          'E',
                          1, 17, 'E',
                          5, 4, 3, 'E',
                          2, 10, 'E',
                          'E'],
                'output': [8, 14, 6, 9, 12, 1, 3, 2, 4],
                'name': 'case 2'
            },
            {
                'input': [14, 8, 23, 9, 12, 6, 1, 17, 5, 4, 3, 2, 10, 'E'],
                'output': [1],
                'name': 'case 3'
            },
            {
                'input': [14, 8, 23, 9, 12, 6, 1, 17, 5, 4, 3, 2, 10, 'E',
                          15, 19, 7, 'E',
                          11, 13, 'E'
                          ],
                'output': [1, 2, 3],
                'name': 'case 4'
            }
        ]


    def test_list_method(self):

        for case in self.cases:
            result = list()
            curr_list = list()
            print(case['input'] )
            for ele in case['input'] :
                if ele == 'E':
                    if curr_list:
                        result.append(curr_list.pop(0))
                    else:
                        result.append(None)
                else:
                    i = len(curr_list) - 1
                    while i >= 0 and ele < curr_list[i]:
                        i -= 1
                    curr_list.insert(i + 1, ele)
            #print('list_method: {}'.format(result))
            self.assertEqual(result, case['output'] , 'list method: {}'.format(case['name'] ))


    def test_heap_sort(self):
        f_left = lambda x: x * 2 + 1
        f_right = lambda x: x * 2 + 2
        f_parent = lambda x : (x + 1) // 2 - 1 if x > 0 else 0

        def max_heapify(a_heap, i_ele, len_heap):
            l = f_left(i_ele)
            r = f_right(i_ele)
            if l < len_heap and a_heap[l] < a_heap[i_ele]:
                minimal = l
            else:
                minimal = i_ele
            if r < len_heap and a_heap[r] < a_heap[minimal]:
                minimal = r

            if minimal != i_ele:
                a_heap[i_ele], a_heap[minimal] = a_heap[minimal], a_heap[i_ele]
                max_heapify(a_heap, minimal, len_heap)

        def add_ele(a_heap, ele):
            a_heap.append(ele)
            len_heap = len(a_heap)
            parent_node = f_parent(len(a_heap) - 1)
            for i in range(parent_node, -1, -1):
                max_heapify(a_heap, i, len_heap)

        def extract_ele(a_heap):
            min = a_heap[0]
            a_heap[0], a_heap[-1] = a_heap[-1], a_heap[0]
            a_heap.pop()

            max_heapify(a_heap, 0, len(a_heap))
            print("pop:", min, 'left:', a_heap)
            return min

        for case in self.cases:
            curr_list = list()
            result = list()
            for ele in case['input'] :
                if ele == 'E':
                    if curr_list:
                        minimal = extract_ele(curr_list)
                        result.append(minimal)
                    else:
                        result.append(None)
                else:
                    add_ele(curr_list, ele)
                    print(curr_list)
            print('heap_method: {}'.format(result))
            self.assertEqual(result, case['output'] , 'heap method: {}'.format(case['name'] ))

    def test_join_sets(self):
        for case in self.cases:
            max_ele = max([ele for ele in case['input'] if isinstance(ele, int)])
            k_arr = _prepare_k_arr(case['input'])
            nr_e = len(k_arr)
            result = [None] * nr_e
            for i in range(max_ele):
                # check which j is i in
                for j in sorted(k_arr.keys()):
                    if i in k_arr[j]:
                        break
                else:
                    continue
                result[j] = i

                # looking for next l
                l = j + 1
                while l < nr_e:
                    if l in k_arr:
                        break
                    l += 1
                if l < nr_e:
                    for ele in k_arr[j]:
                        k_arr[l].append(ele)
                #print(i, j, l, k_arr, result)
                del(k_arr[j])
            self.assertEqual(result, case['output'] , 'join sets method: '.format(case['name'] ) )

    def test_join_sets_linked_list(self):
        for case in self.cases:
            logging.debug('working on case: {}'.format(case['name']))
            max_ele = max([ele for ele in case['input'] if isinstance(ele, int)])
            k_ll = _prepare_k_ll(case['input'])
            for ele in k_ll:
                logging.debug("{}: {}".format(ele, k_ll[ele]))
            nr_e = len(k_ll)
            result = [None] * nr_e
            for i in range(max_ele):
                # check which j is i in
                for j in k_ll.keys():
                    if k_ll[j].head and k_ll[j].head.val == i:
                        node = k_ll[j].head.next
                        logging.debug('update head {}'.format(k_ll[j]))
                        k_ll[j].update_head(node)
                        logging.debug('updated {}'.format(k_ll[j]))
                        break
                else:
                    continue
                logging.debug('extract i={} at j={}'.format(i, j))
                result[j] = i

                # looking for next l
                l = j + 1
                while l < nr_e:
                    if l in k_ll:
                        break
                    l += 1
                if l < nr_e:
                    logging.debug("merge {}={}  with {}={}".format(j, k_ll[j], l, k_ll[l]))

                    k_ll[l].l_add( k_ll[j])
                    # TODO: merge k_ll[l] with k_ll[j]
                    logging.debug("merged {}".format(k_ll[l]))

                del(k_ll[j])
            self.assertEqual(result, case['output'] , 'join sets method: '.format(case['name'] ) )
