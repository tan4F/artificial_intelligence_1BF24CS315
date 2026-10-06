import heapq

GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)
MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def misplaced_tiles(state):
    """Calculate the number of misplaced tiles from the goal."""
    count = 0
    for i, val in enumerate(state):
        if val != 0 and val != GOAL[i]:
            count += 1
    return count

def is_valid_move(blank_pos, move):
    """Check if the move is valid based on the position of the blank tile."""
    r, c = divmod(blank_pos, 3)
    new_r, new_c = r + move[0], c + move[1]
    return 0 <= new_r < 3 and 0 <= new_c < 3

def get_new_state(state, blank_pos, move):
    """Return a new state after applying the move to the current state."""
    r, c = divmod(blank_pos, 3)
    new_r, new_c = r + move[0], c + move[1]
    new_state = list(state)
    new_state[blank_pos], new_state[new_r * 3 + new_c] = new_state[new_r * 3 + new_c], new_state[blank_pos]
    return tuple(new_state), new_r * 3 + new_c

def a_star(start_state):
    """A* search algorithm for solving the 8-puzzle using Misplaced Tiles."""
    blank_pos = start_state.index(0)
    open_list = []
    visited = set()
    g_start = 0
    h_start = misplaced_tiles(start_state)
    f_start = g_start + h_start
    heapq.heappush(open_list, (f_start, g_start, start_state, blank_pos, []))
    
    while open_list:
        f, g, state, blank_pos, path = heapq.heappop(open_list)
        if state == GOAL:
            return path + [state]
        
        if state in visited:
            continue
        visited.add(state)
        
        for move in MOVES:
            if is_valid_move(blank_pos, move):
                new_state, new_blank_pos = get_new_state(state, blank_pos, move)
                if new_state not in visited:
                    g_new = g + 1
                    h_new = misplaced_tiles(new_state)
                    f_new = g_new + h_new
                    new_path = path + [state]
                    heapq.heappush(open_list, (f_new, g_new, new_state, new_blank_pos, new_path))
    return None

def solve_puzzle(start_state):
    """Solve the 8-puzzle using the A* search algorithm."""
    solution = a_star(start_state)
    if solution:
        print(f"Solution found in {len(solution) - 1} steps!")
        for step in solution:
            print(step)
    else:
        print("No solution found.")


if __name__ == "__main__":
    initial_state = (1, 5, 3, 2, 6, 0, 7, 8, 4)  
    solve_puzzle(initial_state)
