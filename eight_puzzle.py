from collections import deque

def solve(start, goal):
    q = deque([(start, [])])
    visited = {start}

    moves = {
        0: [1, 3],
        1: [0, 2, 4],
        2: [1, 5],
        3: [0, 4, 6],
        4: [1, 3, 5, 7],
        5: [2, 4, 8],
        6: [3, 7],
        7: [4, 6, 8],
        8: [5, 7]
    }

    while q:
        state, path = q.popleft()

        if state == goal:
            return path + [state]

        zero = state.index(0)

        for pos in moves[zero]:
            new_state = list(state)
            new_state[zero], new_state[pos] = new_state[pos], new_state[zero]
            new_state = tuple(new_state)

            if new_state not in visited:
                visited.add(new_state)
                q.append((new_state, path + [state]))

    return None


start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

solution = solve(start, goal)

if solution:
    print("Solution:")
    for state in solution:
        print(state[0:3])
        print(state[3:6])
        print(state[6:9])
        print()
else:
    print("No solution")
