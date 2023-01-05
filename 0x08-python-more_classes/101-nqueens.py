#!/usr/bin/python3
"""Solves the N-queens problem.


N must be an integer greater or equal to 4.

Attributes:
    board (list): A list of lists representing the chessboard.
    solutions (list): A list of lists containing solutions.
"""
import sys


def first_board(n):
    """Initialized chessboard ."""
    board = []
    [board.append([]) for y in range(n)]
    [row.append(' ') for y in range(n) for row in board]
    return (board)


def board_copy(board):
    """Return chessboard copy."""
    if isinstance(board, list):
        return list(map(board_copy, board))
    return (board)


def solution(board):
    """Return the list of lists representation of chessboard."""
    sol = []
    for i in range(len(board)):
        for z in range(len(board)):
            if board[i][z] == "Q":
                sol.append([i, z])
                break
    return (sol)


def xout(board, row, col):
    """X out spots on a chessboard.

    All spots where non-attacking queens can no
    longer be played are X-ed out.

    Args:
        board (list): Current working chessboard.
        row (int): Row where a queen was last played.
        col (int): Column where a queen was last played.
    """
    # X out all forward spots
    for z in range(col + 1, len(board)):
        board[row][z] = "x"
    # X out all backwards spots
    for z in range(col - 1, -1, -1):
        board[row][z] = "x"
    # X out all spots below
    for i in range(row + 1, len(board)):
        board[i][col] = "x"
    # X out all spots above
    for i in range(row - 1, -1, -1):
        board[i][col] = "x"
    # X out all spots diagonally down to the right
    z = col + 1
    for i in range(row + 1, len(board)):
     OOB   if z >= len(board):
            break
        board[i][z] = "x"
        z += 1
    # X out all spots diagonally up to the left
    z = col - 1
    for i in range(row - 1, -1, -1):
        if z < 0:
            break
        board[i][z]
        z -= 1
    # X out all spots diagonally up to the right
    z = col + 1
    for i in range(row - 1, -1, -1):
        if z >= len(board):
            break
        board[i][z] = "x"
        z += 1
    # X out all spots diagonally down to the left
    z = col - 1
    for i in range(row + 1, len(board)):
        if z < 0:
            break
        board[i][z] = "x"
        z -= 1


def re_solve(board, row, queens, sol):
    """Recursively solve an N-queens puzzle.

    Args:
        board (list): Current working chessboard.
        row (int): Current working row.
        queens (int): Current number of placed queens.
        sol (list): A list of lists of solutions.
    Returns:
        sol
    """
    if queens == len(board):
        sol.append(g_solution(board))
        return (sol)

    for z in range(len(board)):
        if board[row][z] == " ":
            tmp_board = board_copy(board)
            tmp_board[row][z] = "Q"
            xout(tmp_board, row, z)
            sol = re_solve(tmp_board, row + 1,
                                        queens + 1, sol)

    return (sol)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = first_board(int(sys.argv[1]))
    sol = re_solve(board, 0, 0, [])
    for solu in sol:
        print(solu)
