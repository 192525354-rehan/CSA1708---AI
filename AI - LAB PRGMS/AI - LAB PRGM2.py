def solve(board, row):
    if row == 8:
        print("+---" * 8 + "+")
        for i in range(8):
            print("|", end="")
            for j in range(8):
                if board[i] == j:
                    print(" Q |", end="")
                else:
                    print("   |", end="")
            print()
            print("+---" * 8 + "+")
        return True

    for col in range(8):
        if all(board[i] != col and
               abs(board[i] - col) != row - i
               for i in range(row)):

            board.append(col)

            if solve(board, row + 1):
                return True

            board.pop()

    return False

solve([], 0)
