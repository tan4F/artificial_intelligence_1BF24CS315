initial_state = (
    (1, 2, 3),
    (0, 4, 6),
    (7, 5, 8)
)

goal_state = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 0)
)

DEPTH_LIMIT = 10  


def print_puzzle(state):
    for row in state:
        print(*row)
    print()


def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j


def get_neighbors(state):
    row, col = find_blank(state)

    moves = [
        (1, 0),   # Down
        (0, 1),   # Right
        (-1, 0),  # Up
        (0, -1)   # Left
    ]

    neighbors = []

    for dr, dc in moves:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_state = [list(r) for r in state]

            new_state[row][col], new_state[new_row][new_col] = \
                new_state[new_row][new_col], new_state[row][col]

            neighbors.append(tuple(tuple(r) for r in new_state))

    return neighbors


def dfs(state, goal, visited, path, depth, limit):
    path.append(state)
    visited.add(state)

    if state == goal:
        return True

    if depth < limit:
        for next_state in get_neighbors(state):
            if next_state not in visited:
                if dfs(next_state, goal, visited, path, depth + 1, limit):
                    return True


    path.pop()
    visited.remove(state)
    return False


visited = set()
path = []

print("INITIAL STATE:")
print_puzzle(initial_state)

print("GOAL STATE:")
print_puzzle(goal_state)


if dfs(initial_state, goal_state, visited, path, 0, DEPTH_LIMIT):
    print("DFS SOLUTION PATH")
    print("------------------")

    for depth, state in enumerate(path):
        print("Depth", depth)
        print_puzzle(state)

    print("Goal State Reached!")
    print("Total moves:", len(path) - 1)
else:
    print("No solution found within depth limit", DEPTH_LIMIT)
