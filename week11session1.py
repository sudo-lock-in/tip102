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

print(next_moves(position_1, grid))
print(next_moves(position_2, grid))
print(next_moves(position_3, grid))



