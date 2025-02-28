import random
import pygame

class Board:
    def __init__(self, size=5):
        self.board = []
        self.size = size
        self.num_empty = size**2
        self.highest_piece = 0
        for row in range(size): # The row of the board
            self.board.append([]) # appends an empty list to the list
            for column in range(size): # the column of the board
                self.board[row].append(0) # appends 0 size amount of times
    
    def weightedChoice(self):
        choice = random.randint(1, 100)
        if choice <= 60:
            return 1
        elif choice <= 90:
            return 2
        else:
            return 3

    def place_new_random(self):
        placed = False
        if self.num_empty == 0:
            return -1, -1
        else:
            while not placed:
                row = random.randint(0, self.size-1)
                column = random.randint(0, self.size-1)
                if self.board[row][column] == 0:
                    self.board[row][column] = self.weightedChoice()
                    self.num_empty -= 1
                    placed = True
            return row, column
        
    def place_new_set(self, row, column, choice=-1):
        if choice == 0 and self.board[row][column] != 0:
            self.num_empty += 1
        elif choice == -1:
            choice = self.weightedChoice()
        self.board[row][column] = choice
        return row, column
    
    def compare_square(self, row1, column1, row2, column2):
        if self.board[row1][column1] == self.board[row2][column2]:
            return True
        else:
            return False
    
    def check_neighbors(self, row, column):
        equal_neighbors = []
        # check right
        if self.check_horiz_edge(column) != 2:
            if self.compare_square(row, column, row, column+1):
                equal_neighbors.append([row, column+1])
        # check left
        if self.check_horiz_edge(column) != 1:
            if self.compare_square(row, column, row, column-1):
                equal_neighbors.append([row, column-1])
        # check up
        if self.check_vert_edge(row) != 1:
            if self.compare_square(row, column, row-1, column):
                equal_neighbors.append([row-1, column])
        # check down
        if self.check_vert_edge(row) != 2:
            if self.compare_square(row, column, row+1, column):
                equal_neighbors.append([row+1, column])
        return equal_neighbors
                
    def check_horiz_edge(self, column):
        # 0 = no edge, 1 = left edge, 2 = right edge
        if column == 0:
            return 1
        elif column == self.size - 1:
            return 2
        else:
            return 0
            
    def check_vert_edge(self, row):
        # 0 = no edge, 1 = top edge, 2 = bottom edge
        if row == 0:
            return 1
        elif row == self.size - 1:
            return 2
        else:
            return 0
        
    def display_board(self):
        print ("  ", end="")
        for x in range(self.size):
            print(" ", end="")
            print(x, end=" ")
        print("")
        row_num = 0
        for row in self.board:
            print(row_num, end=" ")
            print(row)
            row_num += 1

    def print_equal_neighbors(self, row, column):
        print("Equal Neighbors of " + str(row) + ", " + str(column) + ":")
        print(self.check_neighbors(row, column))
    
    def merge(self, row1, column1, row2, column2):
        # merges [row1, column1] into [row2, column2]
        # ex: board[0][0] has "1" and board[0][1] has "1" -> [becomes "0" and board[0][1] becomes "2"
        if self.compare_square(row1, column1, row2, column2):
            self.board[row2][column2] += 1
            self.board[row1][column1] = 0
            self.num_empty += 1
            return True
        
    def can_win(self):
        for row in range(self.size): # The row of the board
            for column in range(self.size): # the column of the board
                if len(self.check_neighbors(row, column)) > 0:
                    return True
        return False
    

        
        
