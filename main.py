def make_board(n):
    """
    n is an integer between 3 and 9.  makes a board which is a list of n lists, each list representing a row in the board.  assigns a value from the (n*n - 1) to 0 to each tile.  if n is even, the 2 and 1 tiles are swapped.
    """
    board = []
    val = n*n-1
    for i in range(n):
        board.append([])
    for i in range(n):
        for j in range(n):
            board[i].append(val)
            val-=1
    if n % 2 == 0:
        board[n-1][n-3], board[n-1][n-2] = board[n-1][n-2], board[n-1][n-3]
        

def display_board():
    n = len(board)
    for i in range(n):
        for j in range(n):
            num = board[i][j]
            if num == 0: print("  ", end = " ")
            elif num < 10: print(" " + str(num), end = " ")
            else: print(str(num), end = " ")
        print()


def find_blank():   
    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[i][j]==0:
                return[i, j]
def find_tile(tile):
    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[i][j]==tile:
                return(i, j)
def valid_move(blank_row, blank_col, tile_row, tile_col):
    if blank_col == tile_col:
        if abs(blank_row - tile_row) == 1:
            return True
        return False
    if blank_row == tile_row:
        if abs(blank_col - tile_col) == 1:
            return True
    return False

def check_win():
    n = len(board)
    max_val = n*n-1
    count = 1
    for row in range(n):
        for col in range(n):
            if board[row][col] != count:
                return False
            if max_val == count:
                return True
            count += 1
    return True

     
def swap_tile(blank_row, blank_col, tile_row, tile_col):
    board[blank_row][blank_col] = board[tile_row][tile_col]
    board[tile_row][tile_col] = 0
    

def check_win(blank_row, blank_col, tile_row, tile_col):
    board[blank_row][blank_col] = board[tile_row][tile_col]
    board[tile_row][tile_col] = 0

board = [[15, 14, 13, 12], [11, 10, 9, 8], [7, 6, 0, 4], [3, 1, 2, 5]]
num_rows = 3

#num_rows = valid_input()
make_board(num_rows)
display_board()


while True:
    tile = int(input("Tile: "))
    blank = find_blank()
    tile = find_tile(tile)
    if valid_move(blank[0], blank[1], tile[0], tile[1]) == True:
        swap_tile(blank[0], blank[1], tile[0], tile[1])
    else:
        print("not a valid move")
    display_board()
    if check_win():
        print("Yay!!!")
