class Board:
    def __init__(self, size=5):
        self.board = []
        for row in range(size): # The row of the board
            self.board.append([]) # appends an empty list to the list
            for column in range(size): # the column of the board
                self.board[row].append(0) # appends 0 size amount of times

x = Board()
for row in x.board:
    print(row)

