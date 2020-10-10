from disjoint_set import _build_tree, TreeNode, find_node


def make_set(x):
    x.parent = x
    x.rank = 0

def union(x, y):
    link_set(find_set(x), find_set(y))

def link_set(x, y):
    x.parent = y

def find_set(x):
    if x != x.parent:
        node_set = find_set(x.parent)
        x.parent = node_set
    return x.parent

def lca(node, queries):
    print('check node: {} with child: left {} right {}'.format(node.value,
        node.left.value if node.left else None, node.right.value if node.right else None))
    make_set(node)
    node_set = find_set(node)
    node_set.parent = node
    #print('\tset {} ancestor to {}'.format(node.value, node_set.parent.value))
    for child in [node.left, node.right]:
        if child is not None:

            lca(child, queries)
            #print('\tunion child {} with node {}'.format(child.value, node.value))
            #print('\t\tchild set {}'.format(find_set(child)))
            #print('\t\tnode set {}'.format(find_set(node)))
            union(child, node)
            find_set(node).parent = node

    print('\tset {} to black'.format(node.value))
    node.color = 'b'

    for (u, v) in queries:
        print('\tcheck query: {}, {}'.format(u.value, v.value))
        if node.value == u.value:
            #print('\tmet: {} = {} and color of v {}'.format(node.value, u.value, v.color))
            if v.color == 'b':
                print("LCA of {} and {} is {}".format(u.value, v.value, find_set(v).parent.value))
        elif node.value == v.value:
            #print('\tmet: {} = {} and color of u {}'.format(node.value, v.value, u.color))
            if u.color == 'b':
                print("LCA of {} and {} is {}".format(u.value, v.value, find_set(u).parent.value))
    #print('finished node: {}'.format(node.value))

my_tree = _build_tree([1,2,3,None,4,5,None,6,7,8,9,10,11,12,13])
queries = [#(find_node(my_tree, 6), find_node(my_tree, 9)),
           #(find_node(my_tree, 11), find_node(my_tree, 2)),
           #(find_node(my_tree, 8), find_node(my_tree, 9)),
           (find_node(my_tree, 13), find_node(my_tree, 6))
        ]
lca(my_tree, queries)
