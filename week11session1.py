def next_moves(position, grid):
    safe = []
    rows = len(grid)
    cols = len(grid[0])
    row_pos, col_pos = position

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for row_move, col_move in directions:
        new_row, new_col = row_pos + row_move, col_pos + col_move
        if (0 <= new_row < rows) and 0 <= new_col < cols:
            if grid[new_row][new_col] == 1:
                safe.append((new_row, new_col))
    return safe


grid = [
    [0, 0, 0, 1, 1], # Row 0
    [0, 0, 0, 1, 1], # Row 1
    [1, 1, 1, 0, 0], # Row 2
    [1, 1, 1, 1, 0], # Row 3
    [0, 0, 0, 1, 0]  # Row 4
]

position_1 = (3, 2)
position_2 = (0, 4)
position_3 = (0, 1)

# print(next_moves(position_1, grid))
# print(next_moves(position_2, grid))
# print(next_moves(position_3, grid))

# helper
def next_moves(position, grid, visited):
    safe = []
    rows = len(grid)
    cols = len(grid[0])
    row_pos, col_pos = position

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for row_move, col_move in directions:
        new_row, new_col = row_pos + row_move, col_pos + col_move
        if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == 1 and (new_row, new_col) not in visited:
                safe.append((new_row, new_col))
    return safe

def can_move_safely(position, grid):
    start_row, start_col = position
    rows = len(grid)
    cols = len(grid[0])
    target = (rows - 1, cols - 1)

    if grid[rows - 1][cols - 1] == 0:
        return False

    visited = set()

    def dfs(curr_row, curr_col):
        if (curr_row, curr_col) == target:
            return True
        
        visited.add((curr_row, curr_col))

        for next_move in next_moves((curr_row, curr_col), grid, visited):
            if dfs(next_move[0], next_move[1]):
                return True
            
        return False
    

    return dfs(start_row, start_col)

# Example Usage:

grid = [
    [1, 0, 1, 1, 0], # Row 0
    [1, 1, 1, 1, 0], # Row 1
    [0, 0, 1, 1, 0], # Row 2
    [1, 0, 1, 1, 1]  # Row 3
]

position_1 = (0, 0)
position_2 = (0, 4)
position_3 = (3, 0)

# print(can_move_safely(position_1, grid))
# print(can_move_safely(position_2, grid)) # ex 2
# print(can_move_safely(position_3, grid))
# True
# Example 2 Explanation: Although we start in an unsafe position, we can immediately
# arrive in a safe position and from there safely travel to the bottom right corner (3, 4).
# ^ doesnt match w/ codepath's solution, so mine is fixed to it (removing the started in an infected space edge case)



def list_all_escape_routes(grid):
    out = []
    rows = len(grid)
    cols = len(grid[0])
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1 and can_move_safely((row, col), grid):
                out.append((row, col))
    return out
 

# Example Usage:

grid = [
    [1, 0, 1, 0, 1], # Row 0
    [1, 1, 1, 1, 0], # Row 1
    [0, 0, 1, 0, 0], # Row 2
    [1, 0, 1, 1, 1]  # Row 3
]

# print(list_all_escape_routes(grid))


def safe_zone_size(row, col, grid, visited):
    visited.add((row, col))
    size = 1 # count current position
    for next_row, next_col in next_moves((row, col), grid, visited):
        if (next_row, next_col) not in visited: # codepath forgot this in their solution
            size += safe_zone_size(next_row, next_col, grid, visited)
    return size



def largest_safe_zone(grid):
    rows, cols = len(grid), len(grid[0])
    visited = set()

    largest_size = 0
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1 and (row, col) not in visited:
                visited.add((row, col))
                curr_size = safe_zone_size(row, col, grid, visited)
                largest_size = max(largest_size, curr_size)
    return largest_size


grid = [
    [0, 0, 0, 1, 1], # Row 0
    [0, 0, 0, 1, 1], # Row 1
    [1, 1, 1, 0, 0], # Row 2
    [1, 1, 1, 1, 0], # Row 3
    [0, 0, 0, 1, 0]  # Row 4
]

# print(largest_safe_zone(grid))

from collections import deque

# helper
def next_moves(position, grid):
    safe = []
    rows = len(grid)
    cols = len(grid[0])
    row_pos, col_pos = position

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for row_move, col_move in directions:
        new_row, new_col = row_pos + row_move, col_pos + col_move
        if (0 <= new_row < rows) and 0 <= new_col < cols:
            if grid[new_row][new_col] == 1:
                safe.append((new_row, new_col))
    return safe

def time_to_infect(grid):
    hours = 0
    
    rows = len(grid)
    cols = len(grid[0])

    queue = deque()
    
    safe = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 2:
                queue.append((row, col))
            elif grid[row][col] == 1:
                safe += 1
    
    while queue:
        for _ in range(len(queue)):
            col, row = queue.popleft()
            for next_row, next_col in next_moves((row, col), grid):
                grid[next_row][next_col] = 2
                queue.append((next_row, next_col))
                safe -= 1
        hours += 1
                                        


    return hours - 1 if safe == 0 else -1

grid_1 = [
        [2,1,1],
        [1,1,0],
        [0,1,1]]

grid_2 = [
        [2,1,1],
        [0,1,1],
        [1,0,1]]

grid_3 = [[0,2]]

print(time_to_infect(grid_1))
print(time_to_infect(grid_2))
print(time_to_infect(grid_3))