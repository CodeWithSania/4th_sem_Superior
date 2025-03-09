def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

def position(board, row, column, size):
    for i in range(column):
        if board[row][i] == 'Q':
            return False

    for i, j in zip(range(row, -1, -1), range(column, -1, -1)):
        if board[i][j] == 'Q':
            return False

    for i, j in zip(range(row, size), range(column, -1, -1)):
        if board[i][j] == 'Q':
            return False

    return True

def solvequeensproblem(board, column, size, solutions):
    if column >= size:
        solutions.append(["".join(row) for row in board])
        return

    for row in range(size):
        if position(board, row, column, size):
            board[row][column] = 'Q'
            solvequeensproblem(board, column + 1, size, solutions)

            board[row][column] = '.'

def solvequeensproblem(size):
    board = [['.' for _ in range(size)] for _ in range(size)]
    solutions = []
    solvequeensproblem(board, 0, size, solutions)

    if not solutions:
        print("No solution exists")
    else:
        print(f"Found {len(solutions)} solutions:")
        for i, solution in enumerate(solutions):
            print(f"Solution {i+1}:")
            print_board(solution)

solvequeensproblem(6)