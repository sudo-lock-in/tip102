from collections import deque

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

def nearest_zombie(grid):
    rows, cols = len(grid), len(grid[0])

    queue = deque()


    distances = [[-1] * cols for _ in range(rows)]
    visited = set()

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 0:
                queue.append((row, col))
                distances[row][col] = 0
                visited.add((row, col))


    while queue:
        curr_row, curr_col = queue.popleft()
        for next_row, next_col in next_moves((curr_row, curr_col), grid, visited):
            distances[next_row][next_col] = distances[curr_row][curr_col] + 1
            visited.add((next_row, next_col))
            queue.append((next_row, next_col))

    return distances


grid_1 = [
    [0,0,0],
    [0,1,0],
    [0,0,0]
    ]

grid_2 = [
    [0,0,0],
    [0,1,0],
    [1,1,1]
    ]

grid_3 = [
    [0,0,0],
    [0,1,0],
    [1,1,1],
    [1,1,1]
    ]

# print(nearest_zombie(grid_1))
# print(nearest_zombie(grid_2))
# print(nearest_zombie(grid_3))

# helper
def has_path(city):
    rows, cols = len(city), len(city[0])

    if city[0][0] == 0 or city[rows - 1][cols - 1] == 0:
        return False
   

    queue = deque((0,0))

    visited = set()
    visited.add((0,0))

    while queue:
        curr_row, curr_col = queue.popleft()
        

def can_disconnect_safehouse(city):
    return False

city_1 = [
    [1, 1, 1],
    [0, 0, 1],
    [1, 1, 1]
]

city_2 = [
    [1, 0, 0],
    [1, 1, 0],
    [0, 1, 1]
]

print(can_disconnect_safehouse(city_1))  
print(can_disconnect_safehouse(city_2))  

