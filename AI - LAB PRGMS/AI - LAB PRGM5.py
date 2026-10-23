from collections import deque

def safe(m, c):
    return (m == 0 or m >= c) and (3-m == 0 or 3-m >= 3-c)

def solve():
    q = deque([((3, 3, 1), [])])
    visited = {(3, 3, 1)}

    while q:
        state, path = q.popleft()
        m, c, boat = state

        if state == (0, 0, 0):
            for s in path + [state]:
                print(s)
            return

        moves = [(1,0), (2,0), (0,1), (0,2), (1,1)]

        for dm, dc in moves:
            if boat == 1:
                ns = (m-dm, c-dc, 0)
            else:
                ns = (m+dm, c+dc, 1)

            if 0 <= ns[0] <= 3 and 0 <= ns[1] <= 3:
                if safe(ns[0], ns[1]) and ns not in visited:
                    visited.add(ns)
                    q.append((ns, path + [state]))

solve()
