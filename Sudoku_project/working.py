def main():
    sudoku_board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]

    #We use this function to visulize the board
    def print_board(board):
        for i in range(len(board)):
            if i == 3 or i == 6:
                print("- - - - - - - - - - - ")
            for j in range(len(board)):
                if j == 3 or j == 6:
                    print("| ", end = "")
                if j == 8:
                    print(str(board[i][j]))
                else:
                    print(str(board[i][j])+" ", end="")

    #This function is used to find the empty slots and return their locations within the board.
    def find_empty(board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 0:
                    return (i, j)

        return None

    #Use this function to check if our original sudoku board is a valid board to play with
    def valid(board, num, empty_position):

        #check row
        for i in range(len(board[0])):
            if board[empty_position[0]][i] == num and empty_position[1] != i:
                return False
        #check column
        for i in range(len(board)):
            if board[i][empty_position[1]] == num and empty_position[0] != i:
                return False

        #check cube
        box_x = empty_position[1] // 3
        box_y = empty_position[0] // 3

        for i in range(box_y*3, box_y*3 + 3):
            for j in range(box_x * 3, box_x* 3 + 3):
                if board[i][j] == num and (i,j) != empty_position:
                    return False

        return True

    def solve_sudoku(board):
        find = find_empty(board)
        if not find:
            return True
        else:
            row, col = find

        for i in range(1, 10):
            if valid(board, i, (row, col)):
                board[row][col] = i

                if solve_sudoku(board):
                    return True

                #if we find out that the last call stack return false, set the current [row][col] to 0, try the next value in loop
                board[row][col] = 0

        return False





    print_board(sudoku_board)
    print(find_empty(sudoku_board))
    solve_sudoku(sudoku_board)
    print_board(sudoku_board)

main()
