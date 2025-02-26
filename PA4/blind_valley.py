import sys


# Check if the grid  satisfies the given constraints
def is_constraints_valid(grid, constraints):
    high_col = constraints[2]
    base_col = constraints[3]
    # Check constraints for each row
    for r in range(len(grid)):
        if constraints[0][r] != -1 and grid[r].count('H') != constraints[0][r]:
            return False

        elif constraints[1][r] != -1 and grid[r].count('B') != constraints[1][r]:
            return False
        else:
            continue
    # Check constraints for each column
    for c in range(len(grid[0])):
        b_counter = []

        h_counter = []

        for r in range(len(grid)):
            if grid[r][c] == 'B':
                b_counter.append('B')
            elif grid[r][c] == 'H':
                h_counter.append('H')

        if high_col[c] != -1 and h_counter.count('H') != high_col[c]:
            return False
        elif base_col[c] != -1 and b_counter.count('B') != base_col[c]:
            return False
        else:
            continue

    return True


# Check if the given cell can be placed without violating  neighbor rule
def can_place_tiles(row, col, grid):
    neighbors = [(row - 1, col), (row, col - 1), (row, col + 1), (row, col - 1)]

    if grid[row][col] == 'B':

        for r, c in neighbors:
            if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == 'B':
                return False
        return True

    elif grid[row][col] == 'H':
        for r, c in neighbors:
            if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == 'H':
                return False
    return True


# Recursive function to place tiles on the grid based on the given constraints with Backtracking
def place_tiles(grid, row, col, constraints):
    if col >= len(constraints[2]):
        # If we have reached the end of the grid
        if row >= len(constraints[0])-1:
            # Check if the grid  satisfies all constraints with is_constraints_valid function
            if is_constraints_valid(grid, constraints):
                return True
            else:
                return False
        else:
            # Move to the next row and start from the first column
            row = row + 1
            col = 0

    cell = grid[row][col]
    # If the current cell is a horizontal tile  attempt placing the tile horizontally
    if cell in 'L':
        (grid[row][col], grid[row][col + 1]) = ('H', 'B')

        if can_place_tiles(row, col, grid):
            if place_tiles(grid, row, col + 1, constraints):
                return True
        (grid[row][col], grid[row][col+1]) = ('B', 'H')

        if can_place_tiles(row, col, grid):
            if place_tiles(grid, row, col+1, constraints):
                return True
        (grid[row][col], grid[row][col+1]) = ('N', 'N')

        if place_tiles(grid, row, col+1, constraints):
            return True
        (grid[row][col], grid[row][col+1]) = ('L', 'R')

        if place_tiles(grid, row, col + 1, constraints):
            return True
    # If the current cell is a vertical tile  attempt placing the tile vertically
    elif cell in 'U':
        (grid[row][col], grid[row+1][col]) = ('H', 'B')

        if can_place_tiles(row, col, grid):
            if place_tiles(grid, row, col + 1, constraints):
                return True
        (grid[row][col], grid[row+1][col]) = ('B', 'H')
        if can_place_tiles(row, col, grid):
            if place_tiles(grid, row, col + 1, constraints):
                return True
        (grid[row][col], grid[row+1][col]) = ('N', 'N')
        if place_tiles(grid, row, col + 1, constraints):
            return True
        (grid[row][col], grid[row+1][col]) = ('U', 'D')

        if place_tiles(grid, row, col + 1, constraints):
            return True
    else:
        if can_place_tiles(row, col, grid):
            return place_tiles(grid, row, col + 1, constraints)
        else:
            return False


# Main function to read input, process, and write output
def main():
    take_input = sys.argv[1]
    write_output = sys.argv[2]
    with open(take_input, "r") as file:
        lines = file.readlines()
    # Get constraints from input.txt
    constraints = []
    for line in lines[:4]:
        constraints.append(list(map(int, line.strip().split())))
    # Get grid from input.txt
    grid = []
    for line in lines[4:]:
        grid.append([cell for cell in line.strip().split()])
    # Attempt to place tiles on the grid
    if place_tiles(grid, 0, 0, constraints):
        table = "\n".join([" ".join(row) for row in grid])
        # Write the result to the output file
        with open(write_output, "w") as out_file:
            out_file.write(table)
    else:
        with open(write_output, "w") as out_file:
            out_file.write("No solution!")


if __name__ == "__main__":
    main()
