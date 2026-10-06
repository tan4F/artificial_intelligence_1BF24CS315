import heapq

GOAL = (1, 2, 3, 8, 0, 4, 7, 6, 5)
MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]  

def manhattan_distance(state):
    distance = 0
    for i, val in enumerate(state):
        if val != 0:  
            goal_row, goal_col = divmod(val - 1, 3)
            current_row, current_col = divmod(i, 3)
            distance += abs(current_row - goal_row) + abs(current_col - goal_col)
    return distance

def is_valid_move(blank_pos, move):
    r, c = divmod(blank_pos, 3)
    new_r, new_c = r + move[0], c + move[1]
    return 0 <= new_r < 3 and 0 <= new_c < 3

def get_new_state(state, blank_pos, move):
    r, c = divmod(blank_pos, 3)
    new_r, new_c = r + move[0], c + move[1]
    new_state = list(state)
    new_state[blank_pos], new_state[new_r * 3 + new_c] = new_state[new_r * 3 + new_c], new_state[blank_pos]
    return tuple(new_state), new_r * 3 + new_c

def a_star(start_state):
    blank_pos = start_state.index(0)
    open_list = []
    visited = set()
    g_start = 0
    h_start = manhattan_distance(start_state)
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
                    h_new = manhattan_distance(new_state)  
                    f_new = g_new + h_new 
                    new_path = path + [state]  
                    heapq.heappush(open_list, (f_new, g_new, new_state, new_blank_pos, new_path))
    return None 

def solve_puzzle(start_state):
    solution = a_star(start_state)
    if solution:
        print(f"Solution found in {len(solution) - 1} steps!")
        for step in solution:
            print(step)
    else:
        print("No solution found.")

if __name__ == "__main__":
    initial_state = (2, 8, 3, 1, 6, 4, 0, 7, 5)
    solve_puzzle(initial_state)
