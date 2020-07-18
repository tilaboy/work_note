# avl tree

## height

### height of the tree

the longest path from the root down to a leaf

### height of a node

the longest path from the node down to a leaf

node.height = max(node.left.height, node.right.height) + 1

## AVL tree

for any node, the difference between the height of its left and right child at most 1

## sorting cost:

- insert all n numbers: n * h
- inter-travers: O(n)

h is height of tree, in case of AVL tree, h = log(n)

## insert(delete) node

- add node to the right place in BT O(h)
- fix the AVL property from the parent of added node, and check upwards O(1)

## fix AVL property:

- rotation, always rotation if need to fix
- line: one time left/right rotation on child
- zigzag: two time rotation, first on parent, then on child
