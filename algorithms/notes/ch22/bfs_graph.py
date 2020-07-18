n = 13
g = {
    0: [9, 1],
    1: [8],
    2: [],
    3: [2, 4, 5],
    4: [],
    5: [6],
    6: [7],
    7: [10, 3, 6],
    8: [7, 1],
    9: [8],
    10: [11],
    11: [7],
    12: [],

}
visited = [False] * n

def dfs(at):

    if visited[at]:
        print('backtrack: {}'.format(at))
        return

    print('visit: {}'.format(at))
    visited[at] = True
    neighbours = g[at]
    for next in neighbours:
        dfs(next)

start_node = 0
dfs(start_node)
