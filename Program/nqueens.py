print("Enter the number of queens")
n = int(input())

board = [['-']*n for i in range(n)]  # Generate NxN board


def is_valid(i, j):  # To check if placing queen in square is a valid move
    for k in range(0, n):
        # To check if a queen already exists in same row or column
        if board[i][k] == 'Q' or board[k][j] == 'Q':
            return False
    for k in range(0, n):
        for l in range(0, n):
            if (k+l == i+j) or (k-l == i-j):  # To check if a queen already exists along the diagonal
                if board[k][l] == 'Q':
                    return False
    return True


def solve(n1):
    if n1 == 0:  # If n1 is 0, then arrangement is valid
        return True
    for i in range(0, n):
        for j in range(0, n):
            # To check if placement of queen is valid and no queen exists at that position
            if (is_valid(i, j)) and (board[i][j] != 'Q'):
                board[i][j] = 'Q'
                # To check if we can put next queen with respect to placement of previous queen
                if solve(n1-1) == True:
                    return True
                board[i][j] = '-'

    return False


solve(n)
for i in board:
    print(i)
