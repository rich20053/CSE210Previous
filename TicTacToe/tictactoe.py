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
        #self.board_space = [self.size]
        self.board_space = []
        for i in range (self.size):
            self.board_space.append(i+1)
        #for i in range(self.size):
         #   print(i)
          #  self.board_space[i] = i

        
        

    def draw_board(self):
        # Draw current board object
        
        print("")
        print("{}|{}|{}".format(self.board_space[0],self.board_space[1],self.board_space[2]))
        print("-+-+-")
        print("{}|{}|{}".format(self.board_space[3],self.board_space[4],self.board_space[5]))
        print("-+-+-")
        print("{}|{}|{}".format(self.board_space[6],self.board_space[7],self.board_space[8]))
        print("")
        """
        for i in range(self.size):
            for j in range(self.size):
                print(self.board_space[i][j])
                print
                print("{} + {}i".format(self.real, self.imaginary))

"""
    def mark_board(self, current_player_marker, selected_position):
        # mark the board with the player's choice
        if self.board_space[selected_position-1] == "x" or self.board_space[selected_position-1] == "o":
            print("This space is already chosen.  Please select another.")
            return (False)
        self.board_space[selected_position-1]=current_player_marker
        return (True)

    def check_rows(self):
        if self.board_space[0] == self.board_space[1] and self.board_space[2] == self.board_space[1]:
            return(True)
        if self.board_space[3] == self.board_space[4] and self.board_space[3] == self.board_space[5]:
            return(True)
        if self.board_space[7] == self.board_space[8] and self.board_space[8] == self.board_space[6]:
            return(True)
        return(False)
            
    def check_columns(self):
        if self.board_space[0] == self.board_space[self.edge_size] and self.board_space[0] == self.board_space[2*(self.edge_size)]:
           return(True)
        if self.board_space[1] == self.board_space[4] and self.board_space[1] == self.board_space[7]:
            return(True)
        if self.board_space[2] == self.board_space[5] and self.board_space[5] == self.board_space[8]:
            return(True)
        return(False)
            
    def check_diagonals(self):
        if self.board_space[0] == self.board_space[self.edge_size+1] and self.board_space[0] == self.board_space[2*(self.edge_size+1)]:
            return(True)
        if self.board_space[self.edge_size-1] == self.board_space[self.edge_size+1] and self.board_space[self.edge_size+1] == self.board_space[2*(self.edge_size)]:
            return(True)
        return(False)

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
    game_board = Board(3)

    while (not(game_board.is_game_over())):
        valid_response = False
        while (not(valid_response)):
            choice = int(input("x\'s turn to choose a square (1-9): "))
            valid_response = game_board.mark_board(player_x.get_marker(),choice)
        game_board.draw_board()
        if game_board.is_game_over():
            break
        valid_response = False
        while (not(valid_response)):
            choice = int(input("o\'s turn to choose a square (1-9): "))
            valid_response = game_board.mark_board(player_o.get_marker(),choice)
        game_board.draw_board()
      

if __name__ == "__main__":
    main()