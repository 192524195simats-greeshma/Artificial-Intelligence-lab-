from collections import deque

def water_jug(cap1, cap2, target):
    q = deque([(0, 0)])
    visited = set()
    parent = {}

    while q:
        a, b = q.popleft()

        if (a, b) in visited:
            continue

        visited.add((a, b))

        if a == target or b == target:
            path = []
            state = (a, b)

            while state != (0, 0):
                path.append(state)
                state = parent[state]

            path.append((0, 0))
            return path[::-1]

        states = [
            (cap1, b),          # Fill Jug 1
            (a, cap2),          # Fill Jug 2
            (0, b),             # Empty Jug 1
            (a, 0),             # Empty Jug 2
            (a - min(a, cap2-b), b + min(a, cap2-b)),  # Jug 1 -> Jug 2
            (a + min(b, cap1-a), b - min(b, cap1-a))   # Jug 2 -> Jug 1
        ]

        for state in states:
            if state not in visited:
                parent[state] = (a, b)
                q.append(state)

    return None


cap1 = 4
cap2 = 3
target = 2

solution = water_jug(cap1, cap2, target)

if solution:
    print("Solution:")
    for state in solution:
        print(state)
else:
    print("No solution")
