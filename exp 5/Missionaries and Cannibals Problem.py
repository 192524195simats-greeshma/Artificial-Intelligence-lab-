from collections import deque

def solve():
    start = (3, 3, 0)
    goal = (0, 0, 1)

    queue = deque([(start, [])])
    visited = {start}

    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]

    def safe(m, c):
        return (m == 0 or m >= c) and (m == 3 or (3-m) >= (3-c))

    while queue:
        state, path = queue.popleft()
        m, c, boat = state

        if state == goal:
            for s in path + [state]:
                print(s)
            return

        for dm, dc in moves:
            if boat == 0:
                new = (m-dm, c-dc, 1)
            else:
                new = (m+dm, c+dc, 0)

            nm, nc, nb = new

            if 0 <= nm <= 3 and 0 <= nc <= 3:
                if safe(nm, nc) and new not in visited:
                    visited.add(new)
                    queue.append((new, path + [state]))

solve()
