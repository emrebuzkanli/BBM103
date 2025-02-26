import sys

grid = []  # Initializes the grid
score = 0  # Initializes the score


def take_input():
    while True:
        # Gets user input for row and column
        input_1 = input("Please enter a row and a column number: ")
        print()
        row, column = map(int, input_1.split())

        # Checks if the input is within the correct size
        if 1 <= row <= len(grid) and 1 <= column <= len(grid[0]):
            return row - 1, column - 1
        else:
            print("Please enter a correct size!")
            print()


def is_valid_move(board, row, column):
    target_value = board[row][column]
    connected_cells = set()

    def search(r, c):
        # Uses recursive function to find connected cells
        if (0 <= r < len(board)
                and 0 <= c < len(board[0])
                and board[r][c] == target_value
                and (r, c) not in connected_cells):
            connected_cells.add((r, c))

            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for r1, c1 in directions:
                search(r + r1, c + c1)

    search(row, column)

    return len(connected_cells) >= 2


def remove_connected_cells(board, start_row, start_column, target_value):
    if board[start_row][start_column] == target_value:
        connected_cells = set()

        def search(row, column):

            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            if (0 <= row < len(board)
                    and 0 <= column < len(board[0])
                    and board[row][column] == target_value
                    and (row, column) not in connected_cells):

                connected_cells.add((row, column))

                for r1, c1 in directions:
                    #  Calls the search function
                    search(row + r1, column + c1)

        search(start_row, start_column)

        if len(connected_cells) >= 2:
            global score
            score += len(connected_cells) * int(target_value)
            # Marks connected cells with "x"
            for r, c in connected_cells:
                board[r][c] = "x"


def shift_down(board):
    for c in range(len(board[0])):
        # Shifts non-empty cells down
        non_empty_cells = [
            row for row in range(len(board) - 1, -1, -1) if board[row][c] != "x"
        ]

        for i in range(len(non_empty_cells)):
            empty_row = len(board) - 1 - i
            if empty_row != non_empty_cells[i]:
                board[empty_row][c] = board[non_empty_cells[i]][c]
                board[non_empty_cells[i]][c] = "x"


def remove_empty_columns(board):
    # Removes empty columns to shift other elments
    for c in range(len(board[0]) - 1, -1, -1):
        if all(board[r][c] == "x" for r in range(len(board))):
            for r in range(len(board)):
                del board[r][c]


def shift_up(board):
    while all(cell == "x" for cell in board[0]) and any(
        cell != "x" for row in board for cell in row
    ):
        # Shifts cells up
        for r in range(1, len(board)):
            for c in range(len(board[0])):
                board[r - 1][c] = board[r][c]
                board[r][c] = "x"


def display_board(board):
    # Displays the current state of the board
    for number in board:
        row_str = " ".join(map(lambda a: " " if a == "x" else str(a), number))
        print(row_str)
    print()
    print("your score is:", score)
    print()


def has_valid_moves(board):
    # Checks if there are any valid moves left on the board
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] != "x" and is_valid_move(board, r, c):
                return True
    return False


def is_grid_empty(board):
    # Checks if the entire grid is empty
    return all(all(cell == "x" for cell in row) for row in board)


def main():
    global score
    # Read the initial state of the board from the input file
    with open(sys.argv[1], "r") as input_txt:
        for line in input_txt:
            grid.append(list(map(str, line.split())))

    while True:
        # Displays the current state of the board
        display_board(grid)

        # Checks if there are valid moves left
        if not has_valid_moves(grid):
            print("Game Over")
            break

        # Gets user input for the next move
        row, column = take_input()
        selected_value = grid[row][column]

        # Checks if the selected move is valid
        if is_valid_move(grid, row, column):
            # Removes connected cells and update the score
            remove_connected_cells(grid, row, column, selected_value)
            # Shifts cells down and up
            shift_down(grid)
            shift_up(grid)
            # Removes empty columns
            remove_empty_columns(grid)
        else:
            print("No movement happened try again")
            print()

        # Checks if the entire grid is empty
        if is_grid_empty(grid):
            print()
            print("Your score is:", score)
            print("Game Over")
            break


if __name__ == "__main__":
    main()
