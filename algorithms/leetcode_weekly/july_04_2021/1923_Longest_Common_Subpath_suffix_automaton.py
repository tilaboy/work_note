import sys
from typing import List
import time
from examples import get_cases

'''
why need to clone a new node to get link(x):

last = x - 1, cur = x,
e.g. baba
bab + a, since last b(3)'s parent is b(1) => 'b'
a(4) extended from b(3), will have the same mapping from a(2) extended from b(1) => 'ba', 'ba'
no need to clone
{
    endpos('baba'): {4},
    endpos('aba'): {4},
    endpos('ba'): {2,4},
    endpos('a'): {2,4},
    endpos('bab'): {3},
    endpos('ab'): {3},
    endpos('b'): {1,3}
}

otherwise, e.g. babca, there is a "c" in between and the endpos class 'ba' and 'ca'
not the same, need to clone 'a' from link(x-1).next[a],
{
    endpos('babca'): {5},
    endpos('abca'): {5},
    endpos('bca'): {5},
    endpos('ca'): {5},
    endpos('ba'): {2},
    endpos('a'): {2,5},
    endpos('babc'): {4},
    endpos('abc'): {4},
    endpos('bc'): {4},
    endpos('c'): {4},
    endpos('bab'): {3},
    endpos('ab'): {3},
    endpos('b'): {1,3},
}

so for "baba", b => ba, "{1,3} => {2,4}", no need to clone
for "babca", b => ba is different from b => ca

from https://codeforces.com/blog/entry/20861

Assume that u and v are the shortest and longest words in their common equivalence class.
Then deleting the first letter of u will result in a larger set of possible endpoints,
and adding a letter to the front of v will result in a smaller set.
The words in the equivalence class are exactly those that are between u and v.
The choice of the letter one can add in front of v induces a tree structure on the nodes of the suffix automaton.
The removal of the first letter of u then means moving to the parent in this tree.

- In the first case we may simply add a new equivalence class r containing
  the remaining new suffixes that could not be found in the tree.
  It will have a suffix link to q.
- In the second case we will have to add two new equivalence classes.
  For instance consider adding 'c' to the end of "abcb".
  In the original tree when we start following the letters from the back of the new string "abcbc",
  we will come to the equivalence class q with longest string "abc".
  The search will terminate at "bc" since the next letter we would try is 'c',
  which is different from 'a'. Thus we add the equivalence classes q' and r with longest strings "bc" and "abcbc" respectively.

# links
the class q' becomes the parent of q and r in the suffix tree, and the parent of q' is the old parent of q

# edges
edges to r: add edges to the new class r from every class of every suffix of the original string that does not have an edge labeled with the added letter x.
These can be found by starting from the class of the whole original string and following the suffix links until a class p with edge labeled x appears.
Following the edge from p also gives us the class q.

If we have to split q, there will be additional changes to the edges.
edges from q: will stay the same, and these will also be copied to be the edges from q'.
edges to q: those from p and its parents by following suffix links to q, now should point to the shorter strings in q' instead
'''


class NodeState:
    def __init__(self, length=0, link=-1, next_char=dict()):
        self.length = length
        self.link = link
        self.next_char = next_char

    def __repr__(self):
        return f'{self.length}, link: {self.link}, next => {self.next_char}'

def build_sa(arr):
    sa = [NodeState(0, -1, dict())]
    last = i_state = 0
    for cur_c in arr:
        i_state += 1
        sa.append(NodeState(sa[last].length + 1, 0, dict()))
        p, cur = last, i_state
        while p != -1 and cur_c not in sa[p].next_char:
            sa[p].next_char[cur_c] = cur
            p = sa[p].link
        if p != -1:
            q = sa[p].next_char[cur_c]
            if sa[p].length == sa[q].length - 1:
                sa[cur].link = q
            else:
                # clone q
                i_state += 1
                clone = i_state
                sa.append(NodeState(sa[p].length + 1, sa[q].link, dict(sa[q].next_char)))
                while p != -1 and sa[p].next_char.get(cur_c, None) == q:
                    sa[p].next_char[cur_c] = clone
                    p = sa[p].link
                sa[q].link = sa[cur].link = clone
        last = cur
    return sa

sa_abcbc = build_sa('abbb')
for i_ele, ele in enumerate(sa_abcbc):
    print (i_ele, ele.length, ele.link, ele.next_char)

sys.exit()

class Solution:
    def longestCommonSubpath(self, n: int, paths: List[List[int]]) -> int:
        pass

sol = Solution()
cases = get_cases()
K = 1
expects = [case['expect'] for case in cases[:K]]
start = time.perf_counter_ns()
#print(sol.longestCommonSubpath(5, [[0,1,2,3,4], [2,3,4], [4,0,1,2,3]]))
solutions = [sol.longestCommonSubpath(case["n"], case["input"]) for case in cases[:K]]
#print("durantion: {}".format((time.perf_counter_ns() - start)/1e9))
#assert solutions == expects
