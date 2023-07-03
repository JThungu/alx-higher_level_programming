#!/usr/bin/python3
"""Solves the N-queens puzzle.

Finds all possible solutions for placing N non-attacking queens on an NxN chessboard.

Example:
$ ./nqueens.py N

N must be an integer greater than or equal to 4.

Attributes:
board (list): A list of lists representing the chessboard.
solutions (list): A list of lists containing solutions.

Solutions are represented in the format [[r, c], [r, c], [r, c], [r, c]]
where r and c represent the row and column, respectively, where a
queen must be placed on the chessboard.
"""
import sys

def initialize_board(n):
"""Initialize an nxn sized chessboard with 0's."""
board = []
[board.append([]) for _ in range(n)]
[row.append(' ') for _ in range(n) for row in board]
return board

def deepcopy_board(board):
"""Return a deepcopy of a chessboard."""
if isinstance(board, list):
return list(map(deepcopy_board, board))
return board

def get_solution(board):
"""Return the list of lists representation of a solved chessboard."""
solution = []
for r in range(len(board)):
for c in range(len(board)):
if board[r][c] == "Q":
solution.append([r, c])
break
return solution

def xout_spots(board, row, col):
"""X out spots on a chessboard.

All spots where non-attacking queens can no
longer be placed are X-ed out.

Args:
    board (list): The current working chessboard.
    row (int): The row where a queen was last placed.
    col (int): The column where a queen was last placed.
"""
# X out all forward spots
for c in range(col + 1, len(board)):
    board[row][c] = "x"
# X out all backward spots
for c in range(col - 1, -1, -1):
    board[row][c] = "x"
# X out all spots below
for r in range(row + 1, len(board)):
    board[r][col] = "x"
# X out all spots above
for r in range(row - 1, -1, -1):
    board[r][col] = "x"
# X out all spots diagonally down to the right
c = col + 1
for r in range(row + 1, len(board)):
    if c >= len(board):
        break
    board[r][c] = "x"
    c += 1
# X out all spots diagonally up to the left
c = col - 1
for r in range(row - 1, -1, -1):
    if c < 0:
        break
    board[r][c] = "x"
    c -= 1
# X out all spots diagonally up to the right
c = col + 1
for r in range(row - 1, -1, -1):
    if c >= len(board):
        break
    board[r][c] = "x"
    c += 1
# X out all spots diagonally down to the left
c = col - 1
for r in range(row + 1, len(board)):
    if c < 0:
        break
    board[r][c] = "x"
