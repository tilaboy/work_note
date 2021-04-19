class LinkNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return '({} => {})'.format(self.val, self.next.val if self.next else None)

def init_from_list(arr):
    head = None
    prev_node = None
    for ele in arr:
        node = LinkNode(ele)
        if head is None:
            head = node
            prev_node = node
        else:
            prev_node.next = node
            prev_node = node
    return head

def nodes_to_arr(node):
    arr = list()
    while node is not None:
        arr.append(node.val)
        node = node.next
    return arr

def print_ll(node):
    print(nodes_to_arr(node))

def rev_ll(head):

    if head is None:
        return head
    node = head.next
    prev_node = head
    print('      ', '  head ', 'head.next', '  node ', 'node.next')
    while node is not None:
        print('before', head, head.next, node, node.next)
        # 1 2 3 4 5
        node, head, head.next, prev_node.next = node.next, node, head, node.next


        # 2 1 3 4 5
        print('after ', head, head.next, node, node.next if node is not None else None)
        print('')
    return head


arr = [1,2,3,4,5]
head = init_from_list(arr)

print_ll(head)
head = rev_ll(head)
print_ll(head)
