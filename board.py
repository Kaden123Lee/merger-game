import random

class Board:
    def __init__(self, size=4):
        """
        Initializes a square game board with the specified size (default 5x5).
        Attributes:
            board (2D list): A size x size grid initialized with 0s.
            size (int): The dimension of the board.
            num_empty (int): Tracks the number of empty cells (0s) on the board.
            highest_piece (int): Tracks the highest value piece on the board (initialized to 0).
        """
        self.board = [] 

        self.size = size
        self.num_empty = size**2  # All cells start empty
        self.highest_piece = 0    # No pieces initially
        # Initialize each cell to 0 (empty)
        for row in range(size): 
            self.board.append([]) 
            for column in range(size): 
                self.board[row].append(0) 

    def convert_to_1D(self):
        oneD = []
        for i in self.board:
            for j in i:
                oneD.append(j)
        return oneD
    
    def getBoard(self):
        return self.board

    def weightedChoice(self):
        """
        Generates a random piece value with weighted probabilities.
        Returns:
            1 with 60% probability, 2 with 30%, and 3 with 10%.
        """
        choice = random.randint(1, 100)
        if choice <= 60:
            return 1
        elif choice <= 90:  # 90-60=30% chance
            return 2
        else:               # 10% chance
            return 3

    def place_new_random(self):
        """
        Places a new piece (via weightedChoice) in a random empty cell.
        Returns:
            (row, column) of the placed piece, or (-1, -1) if the board is full.
        """
        placed = False
        if self.num_empty == 0:
            return -1, -1
        else:
            # Keep searching until an empty cell is found
            while not placed:
                row = random.randint(0, self.size-1)
                column = random.randint(0, self.size-1)
                if self.board[row][column] == 0:
                    # Place the new piece and update empty count
                    self.board[row][column] = self.weightedChoice()
                    self.num_empty -= 1
                    placed = True
            return row, column
        
    def place_new_set(self, row, column, choice=-1):
        """
        Sets a specific cell to a given value or a random weighted value.
        Args:
            row, column: Position to place the piece.
            choice: Value to place. If -1, uses weightedChoice. If 0, clears the cell.
        Returns:
            (row, column) where the piece was placed.
        """
        # If setting to 0 and the cell wasn't empty, increment empty count
        if choice == 0 and self.board[row][column] != 0:
            self.num_empty += 1
        elif choice == -1:  # Use weighted random choice if not specified
            choice = self.weightedChoice()
        self.board[row][column] = choice
        return row, column
    
    def compare_square(self, row1, column1, row2, column2):
        """
        Checks if two cells have the same non-zero value.
        Returns:
            True if the cells are equal and non-zero, False otherwise.
        """
        return self.board[row1][column1] == self.board[row2][column2] and self.board[row1][column1] != 0
    
    def check_neighbors(self, row, column):
        """
        Finds all adjacent cells (up, down, left, right) with the same value as the given cell.
        Returns:
            List of [row, column] pairs of matching neighbors.
        """
        equal_neighbors = []
        # Check right neighbor if not on the right edge
        if self.check_horiz_edge(column) != 2:
            if self.compare_square(row, column, row, column+1):
                equal_neighbors.append([row, column+1])
        # Check left neighbor if not on the left edge
        if self.check_horiz_edge(column) != 1:
            if self.compare_square(row, column, row, column-1):
                equal_neighbors.append([row, column-1])
        # Check upper neighbor if not on the top edge
        if self.check_vert_edge(row) != 1:
            if self.compare_square(row, column, row-1, column):
                equal_neighbors.append([row-1, column])
        # Check lower neighbor if not on the bottom edge
        if self.check_vert_edge(row) != 2:
            if self.compare_square(row, column, row+1, column):
                equal_neighbors.append([row+1, column])
        return equal_neighbors
                
    def check_horiz_edge(self, column):
        """
        Determines if a column is on the left or right edge.
        Returns:
            1 for left edge, 2 for right edge, 0 otherwise.
        """
        if column == 0:
            return 1
        elif column == self.size - 1:
            return 2
        else:
            return 0
            
    def check_vert_edge(self, row):
        """
        Determines if a row is on the top or bottom edge.
        Returns:
            1 for top edge, 2 for bottom edge, 0 otherwise.
        """
        if row == 0:
            return 1
        elif row == self.size - 1:
            return 2
        else:
            return 0
        
    def display_board(self):
        """Prints the board with row and column indices."""
        print ("  ", end="")
        # Print column headers
        for x in range(self.size):
            print(" ", end="")
            print(x, end=" ")
        print("")
        # Print each row with its row number
        row_num = 0
        for row in self.board:
            print(row_num, end=" ")
            print(row)
            row_num += 1

    def print_equal_neighbors(self, row, column):
        """Helper to print the equal neighbors of a cell."""
        print(f"Equal Neighbors of {row}, {column}:")
        print(self.check_neighbors(row, column))

    def merge(self, row1, column1, row2, column2):
        """
        Merges the piece at (row1, column1) into (row2, column2).
        The target cell's value increases by 1, and the source cell becomes 0.
        Returns:
            True if merge was successful, False otherwise.
        """
        if self.compare_square(row1, column1, row2, column2):
            self.board[row2][column2] += 1
            self.board[row1][column1] = 0
            self.num_empty += 1  # Source cell is now empty
            return True
        return False  # Cells were not mergeable
    
    def can_win(self):
        """
        Checks if any merges are possible on the board.
        Returns:
            True if at least one cell has mergeable neighbors, False otherwise.
        """
        for row in range(self.size):
            for column in range(self.size):
                if len(self.check_neighbors(row, column)) > 0:
                    return True
        return False