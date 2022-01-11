""" 
File: tictactoe.py
Author: Mark Richmodn
This program implements a Tic Tac Toe game.
"""

from types import ClassMethodDescriptorType


class Board():
    """
    Board class - All information and activities of the playing board
    """
    def __init__(self, selected_size):
        # Set initial Variables
        self.edge_size = selected_size
        self.size = selected_size * selected_size
        self.board = ""
        self.board_space = []
        for i in range (self.size):
            self.board_space.append(i+1)
        #for i in range(self.size):
         #   print(i)
          #  self.board_space[i] = i

        
        

    def draw_board(self):
        # Draw current board object

        print("")
        self.board = ""

        for i in range(self.size):
            if self.edge_size > 3 and (i < 9 or self.board_space[i] != i+1):
                self.board += " "
            self.board += "{}".format(self.board_space[i])
            if (i % self.edge_size != self.edge_size -1):
                self.board += "|"
            else:
                self.board += "\n"
                if i != self.size - 1:
                    if self.edge_size > 3 and (i < 9 or self.board_space[i] != i+1 or (i > 8)):
                        self.board += "-"
                    self.board += "-" 
                    for i in range(self.edge_size-1):
                        self.board += "+-" 
                        if self.edge_size > 3 and (i < 9 or self.board_space[i] != i+1):
                            self.board += "-"
                    self.board += "\n" 
        print(self.board)
        
    def mark_board(self, current_player_marker, selected_position):
        # mark the board with the player's choice
        if self.board_space[selected_position-1] == "x" or self.board_space[selected_position-1] == "o":
            print("This space is already chosen.  Please select another.")
            return (False)
        self.board_space[selected_position-1]=current_player_marker
        return (True)

    def check_rows(self):
        row_filled = True
        cell_value = "x"
        for i in range (self.edge_size):
            for j in range (self.edge_size):
                if j == 0:
                    cell_value = self.board_space[(i*self.edge_size)+j]
                row_filled = row_filled and (self.board_space[(i*self.edge_size)+j] == cell_value)
            if row_filled:
                return(row_filled)
            if i != self.edge_size - 1:
                row_filled = True
        return(row_filled)
            
    def check_columns(self):
        column_filled = True
        cell_value = "x"
        for i in range (self.edge_size):
            for j in range (self.edge_size):
                if j == 0:
                    cell_value = self.board_space[(j*self.edge_size)+i]
                column_filled = column_filled and (self.board_space[(j*self.edge_size)+i] == cell_value)
            if column_filled:
                return(column_filled)
            if i != self.edge_size - 1:
                column_filled = True
        return(column_filled)
            
    def check_diagonals(self):

        diagonal_filled = True
        for j in range (0, self.size, self.edge_size + 1):
            if j == 0:
                cell_value = self.board_space[j]
            diagonal_filled = diagonal_filled and (self.board_space[j] == cell_value)
        if diagonal_filled:
            return(diagonal_filled)

        diagonal_filled = True
        for j in range (self.size-self.edge_size, self.edge_size-2, -1*(self.edge_size-1)):
            if j == self.size-self.edge_size:
                cell_value = self.board_space[j]
            diagonal_filled = diagonal_filled and (self.board_space[j] == cell_value)

        return(diagonal_filled)

    def check_draw(self):
        for i in range(self.size):
           if self.board_space[i] == i+1:
                return(False)
        return(True)       

    def is_game_over(self):
        if self.check_rows() or self.check_columns() or self.check_diagonals():
            print("Good game. Thanks for playing!\n")
            return(True)
        if (self.check_draw()):
            print("Draw. Thanks for playing!\n")
            return(True)
        return (False)


class Player():
    """
    Player class - All information and activities about a player
    """
    def __init__(self, play_marker):
        # Set initial Variables
        self.marker = play_marker

    def get_marker(self):
        # Draw current board object
        return(self.marker)
               
def main():
#   main function calls other functions
    player_x = Player("x")
    player_o = Player("o")

    
    board_size = int(input("Input how many spaces per side (3-9, but typically this is 3): "))

    input_string_x = "x\'s turn to choose a square (1-{}): ".format(board_size**2)
    input_string_o = "o\'s turn to choose a square (1-{}): ".format(board_size**2)
 
    game_board = Board(board_size)
    
    game_board.draw_board()

    while (not(game_board.is_game_over())):
        valid_response = False
        while (not(valid_response)):
            choice = int(input(input_string_x))
            valid_response = game_board.mark_board(player_x.get_marker(),choice)
        game_board.draw_board()
        if game_board.is_game_over():
            break
        valid_response = False
        while (not(valid_response)):
            choice = int(input(input_string_o))
            valid_response = game_board.mark_board(player_o.get_marker(),choice)
        game_board.draw_board()
      

if __name__ == "__main__":
    main()