class TreeNode:
    def __init__(self, value, left=None, right=None, parent=None, rank=0):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent
        self.rank = rank
        self.color = 'w'

    def __str__(self):
        return '{}'.format(self.value)

def make_set(x):
    x.parent = x
    x.rank = 0

def union_set(x, y):
    link_set(find_set(x), find_set(y))

def link_set(x, y):
    if x.rank > y_rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1

def find_set(x):
    if x != x.parent:
        x.parent = find_set(x.parent)
    return x.parent


# [1, 2, 3, N, 4, 5, None, 6, 7, 8, 9, 10]
#           1
#      2        3
#    N   4    N    5
#      6   7     8   9
#    10
def _build_tree(arr):
    stack = list()
    node = TreeNode(arr[0])
    head = node
    stack = [node]
    i = 1
    status = 'l'
    papa = None
    while i < len(arr):
        node = None
        if status == 'l':
            papa = stack.pop(0)

        if arr[i] is not None:
            node = TreeNode(arr[i])
            stack.append(node)
            node.parent = papa

        if status == 'l':
            papa.left = node
        else:
            papa.right = node

        status = 'r' if status == 'l' else 'l'
        i += 1

    return head



def _top_transverse(head):
    stack = [head]
    while stack:
        node = stack.pop(0)
        print(node.value)
        if node.left is not None:
            print('l: {}'.format(node.left.value))
            stack.append(node.left)
        if node.right is not None:
            print('r: {}'.format(node.right.value))
            stack.append(node.right)

def find_node(head, value):
    stack = [head]
    while stack:
        node = stack.pop(0)
        if node.value == value:
            return node
        if node.left is not None:
            stack.append(node.left)
        if node.right is not None:
            stack.append(node.right)


#tree = _build_tree([1,2,3,None,4,5,None,6,7,8,9,10,11,12,13])
#_top_transverse(tree)
