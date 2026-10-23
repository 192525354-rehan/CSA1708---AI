from collections import deque

def water_jug(a, b, target):
    q = deque([((0, 0), [])])
    visited = {(0, 0)}

    while q:
        (x, y), path = q.popleft()

        if x == target or y == target:
            for p in path + [(x, y)]:
                print(p)
            return

        states = [
            (a, y),
            (x, b),
            (0, y),
            (x, 0),
            (x - min(x, b-y), y + min(x, b-y)),
            (x + min(y, a-x), y - min(y, a-x))
        ]

        for s in states:
            if s not in visited:
                visited.add(s)
                q.append((s, path + [(x, y)]))

a = int(input("Enter jug A capacity: "))
b = int(input("Enter jug B capacity: "))
target = int(input("Enter target: "))

water_jug(a, b, target)
