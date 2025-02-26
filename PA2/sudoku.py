import sys


def is_valid_move(grid, row, col, num):
    # Checks the row for conflicts
    for i in range(9):
        if num == grid[row][i]:
            return False

    # Checks the column for conflicts
    for i in range(9):
        if num == grid[i][col]:
            return False

    # Checks the 3x3 subgrid for conflicts
    subgrid_start_row, subgrid_start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(subgrid_start_row, subgrid_start_row + 3):
        for j in range(subgrid_start_col, subgrid_start_col + 3):
            if num == grid[i][j]:
                return False

    return True


def find_empty_cell(grid):

    # Finds the first empty cell on the grid
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                # Check possible values for the empty cell
                possible_values = [num for num in range(1, 10) if is_valid_move(grid, i, j, num)]
                # If there is only one possible value, return the cell position and the value
                if len(possible_values) == 1:
                    return i, j, possible_values[0]
    return None


def sudoku_solver(grid, output_file, step_num):
    """
    Solve the Sudoku puzzle using a basic backtracking algorithm.
    """
    empty_cell = find_empty_cell(grid)

    if not empty_cell:
        return True

    (row, col) = (0, 0)

    for num in range(1, 10):
        if is_valid_move(grid, row, col, num):
            grid[row][col] = num
            step_num = step_num + 1
            # Prints the current step of the grid
            output_file.write("------------------\n")
            output_file.write(f"Step {step_num} - Placed {num} at R{row + 1}C{col + 1}\n")
            output_file.write("------------------\n")
            for r in grid:
                output_file.write(" ".join(map(str, r)) + "\n")
            # Calls sudoku_solver to solve the puzzle
            if sudoku_solver(grid, output_file, step_num):
                return True

            # Backtracks if the current placement leads wrong output
            grid[row][col] = 0
            step_num = step_num - 1

    return False


def main():
    input_file_1 = sys.argv[1]
    output_file_1 = sys.argv[2]
    grid = []

    # Reads sudoku puzzle from the input_txt
    with open(input_file_1, "r") as input_file:
        for line in input_file:
            grid.append(list(map(int, line.strip().split())))

    with open(output_file_1, 'w') as output_file:
        step_num = 0
        while True:
            empty_cell = find_empty_cell(grid)
            if not empty_cell:
                break

            row, col, num = empty_cell
            grid[row][col] = num
            step_num = step_num+1
            # Writes  the current state of the grid to the output.txt
            output_file.write('-'*18)
            output_file.write("\n")
            output_file.write(f"Step {step_num} - {num} @ R{row + 1}C{col + 1}")
            output_file.write("\n")
            output_file.write("-"*18)
            output_file.write("\n")
            for r in grid:
                output_file.write(" ".join(map(str, r)) + "\n")

        output_file.write("-"*18)


if __name__ == "__main__":

    main()
