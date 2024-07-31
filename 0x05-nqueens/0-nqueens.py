#!/usr/bin/python3
"""
The N queens puzzle is the challenge of placing N
non-attacking queens on an N×N chessboard.

TODO:
    * Write a program that solves the N queens problem.
"""

import sys


def is_safe(board, row, col, N):
    # Check this column on upper rows
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(N):

    def solve(row, board):
        if row == N:
            solutions.append(board[:])
            return
        for col in range(N):
            if is_safe(board, row, col, N):
                board[row] = col
                solve(row + 1, board)
                board[row] = -1

    solutions = []
    board = [-1] * N
    solve(0, board)
    return solutions


def print_solutions(solutions):
    for solution in solutions:
        formatted_solution = [[i, col] for i, col in enumerate(solution)]
        print(formatted_solution)


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(N)
    print_solutions(solutions)


if __name__ == "__main__":
    main()
