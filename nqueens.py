def nqueens(n):
    return nqueens_helper((), n)


def nqueens_helper(board, n):
    if len(board) == n:
        return board
    for i in range(n):
        if is_valid(board, i):
            new_board = board + (i,)
            solution = nqueens_helper(new_board, n)
            if solution:
                return solution
        else:
            continue
    return False


def is_valid(board, current_row):
    valid_counter = 0
    current_col = len(board)
    for past_col in range(len(board)):
        past_row = board[past_col]
        if current_row == past_row or current_col == past_col:
            return False
        else:
            slope = abs((current_col - past_col) / (current_row - past_row))
            if slope == 1:
                return False
            else:
                valid_counter += 1
    if valid_counter == len(board):
        return True
