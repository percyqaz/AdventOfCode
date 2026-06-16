# Conway's game of life implementation in Python
# Read the starting state from input.txt, where # represents a live cell and . represents a dead cell.
# Run the game for 100 steps, then count the number of live cells and print the result.

STEPS = 100

def parse_grid(lines):
    return [[cell == "#" for cell in line.strip()] for line in lines if line.strip()]

def count_neighbors(grid, row, col):
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1),
    ]
    count = 0
    max_row = len(grid)
    max_col = len(grid[0])
    for dr, dc in directions:
        r, c = row + dr, col + dc
        if 0 <= r < max_row and 0 <= c < max_col and grid[r][c]:
            count += 1
    return count

def step(grid):
    rows = len(grid)
    cols = len(grid[0])
    new_grid = [[False] * cols for _ in range(rows)]

    for r in range(rows):
        for c in range(cols):
            alive = grid[r][c]
            neighbors = count_neighbors(grid, r, c)
            if alive:
                new_grid[r][c] = neighbors == 2 or neighbors == 3
            else:
                new_grid[r][c] = neighbors == 3

    return new_grid

def turn_on_corners(grid):
    rows = len(grid)
    cols = len(grid[0])
    grid[0][0] = True
    grid[0][cols - 1] = True
    grid[rows - 1][0] = True
    grid[rows - 1][cols - 1] = True
    return grid


def count_live_cells(grid):
    return sum(sum(1 for cell in row if cell) for row in grid)

with open("input.txt", encoding="utf-8") as f:
    grid = parse_grid(f.readlines())

grid = turn_on_corners(grid)

for _ in range(STEPS):
    grid = step(grid)
    grid = turn_on_corners(grid)

print(count_live_cells(grid))