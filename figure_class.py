### THEM MOVES FOR CHESS GAME



#def up(tile, n):
#    """ Move figures on given tile n-steps ahead """
#    for i, row in enumerate(figures):
#        for key in row:
#            if key == tile:
#                selected_figure = row[tile]
#                row[tile] = "_" #removes figure from selected tile
#                number = int(tile[1])
#                number += n
#                tile = tile[0] + str(number) #changes tile to n-steps forward
#                for figure in "prkbQK":
#                    if figure == selected_figure:
#                        figures[i - n][tile] = figure
#
#                update_board()
#                print_board(board)
#                
#                break
#
#
#def down(tile, n):
#    """ Move figures on given tile n-steps backwards """
#    for i, row in enumerate(figures):
#        figures_changed = False
#        for key in row:
#            if key == tile:
#                figures_changed = True
#                selected_figure = row[tile]
#                row[tile] = "_" #removes figure from selected tile
#                number = int(tile[1])
#                number -= n
#                tile = tile[0] + str(number) #changes tile to n-steps backwards
#                for figure in "prkbQK":
#                    if figure == selected_figure:
#                        figures[i + n][tile] = figure
#
#                update_board()
#                print_board(board)
#                
#                break
#        if figures_changed == True:
#            break
#
#
#def right(tile, n):
#    """ Move figures on given tile n-steps to the right """
#    for row in figures:
#        letters = "ABCDEFGH"
#        figures_changed = False
#        for i, key in enumerate(row):
#            if key == tile:
#                figures_changed = True
#                selected_figure = row[tile]
#                row[tile] = "_" #removes figure from selected tile
#                letter = letters[i + n]
#                tile = letter + tile[1] #changes tile to n-steps to the right
#                for figure in "prkbQK":
#                    if figure == selected_figure:
#                        
#                        row[tile] = figure
#
#                update_board()
#                print_board(board)
#                
#                break
#        if figures_changed == True:
#            break
#
#
#def left(tile, n):
#    """ Move figures on given tile n-steps to the left """
#    for row in figures:
#        letters = "ABCDEFGH"
#        figures_changed = False
#        for i, key in enumerate(row):
#            if key == tile:
#                figures_changed = True
#                selected_figure = row[tile]
#                row[tile] = "_" #removes figure from selected tile
#                letter = letters[i - n]
#                tile = letter + tile[1] #changes tile to n-steps to the left
#                for figure in "prkbQK":
#                    if figure == selected_figure:
#                        
#                        row[tile] = figure
#
#                update_board()
#                print_board(board)
#                
#                break
#        if figures_changed == True:
#            break
#
#
#
#def up_left(tile, n):
#    """ Move figures on given tile n-steps to the left and forward """
#    for figures_i, row in enumerate(figures):
#        letters = "ABCDEFGH"
#        figures_changed = False
#        for row_i, key in enumerate(row):
#            if key == tile:
#                figures_changed = True
#                selected_figure = row[tile]
#                row[tile] = "_" #removes figure from selected tile
#                letter = letters[row_i - n]
#                number = int(tile[1])
#                number += n
#                tile = letter + str(number) #changes tile to n-steps to the left and forward
#                for figure in "prkbQK":
#                    if figure == selected_figure:
#                        figures[figures_i - n][tile] = figure
#
#                update_board()
#                print_board(board)
#                
#                break
#        if figures_changed == True:
#            break
#
#
#def up_right(tile, n):
#    """ Move figures on given tile n-steps to the right and forward """
#    for figures_i, row in enumerate(figures):
#        letters = "ABCDEFGH"
#        figures_changed = False
#        for row_i, key in enumerate(row):
#            if key == tile:
#                figures_changed = True
#                selected_figure = row[tile]
#                row[tile] = "_" #removes figure from selected tile
#                letter = letters[row_i + n]
#                number = int(tile[1])
#                number += n
#                tile = letter + str(number) #changes tile to n-steps to the right and forward
#                for figure in "prkbQK":
#                    if figure == selected_figure:
#                        figures[figures_i - n][tile] = figure
#
#                update_board()
#                print_board(board)
#                
#                break
#        if figures_changed == True:
#            break
#
#
#def down_right(tile, n):
#    """ Move figures on given tile n-steps to the right and down """
#    for figures_i, row in enumerate(figures):
#        letters = "ABCDEFGH"
#        figures_changed = False
#        for row_i, key in enumerate(row):
#            if key == tile:
#                figures_changed = True
#                selected_figure = row[tile]
#                row[tile] = "_" #removes figure from selected tile
#                letter = letters[row_i + n]
#                number = int(tile[1])
#                number -= n
#                tile = letter + str(number) #changes tile to n-steps to the right and down
#                for figure in "prkbQK":
#                    if figure == selected_figure:
#                        figures[figures_i + n][tile] = figure
#
#                update_board()
#                print_board(board)
#                
#                break
#        if figures_changed == True:
#            break
#
#
#def down_left(tile, n):
#    """ Move figures on given tile n-steps to the left and down """
#    for figures_i, row in enumerate(figures):
#        letters = "ABCDEFGH"
#        figures_changed = False
#        for row_i, key in enumerate(row):
#            if key == tile:
#                figures_changed = True
#                selected_figure = row[tile]
#                row[tile] = "_" #removes figure from selected tile
#                letter = letters[row_i - n]
#                number = int(tile[1])
#                number -= n
#                tile = letter + str(number) #changes tile to n-steps to the left and down
#                for figure in "prkbQK":
#                    if figure == selected_figure:
#                        figures[figures_i + n][tile] = figure
#
#                update_board()
#                print_board(board)
#                
#                break
#        if figures_changed == True:
#            break
        
        
### NEW CLASSES ###
# p = pawn, Q = queen, K = king, k = knight, b = bishop, r = rook

from board_class import Board

class Figure:
    #think about how I want to use this class top-down
    #imagine scenario
    #what methods will I need and which of those do I have to accsess (private)
    #example: Figure("p", "white", "A2")
    
    figures_lst = []
    
    def __init__(self, name, color, pos):
        self.name = name
        self.color = color
        self.pos = pos
                   
        Figure.figures_lst.append(self)
        

    def isFree(pos, color=None):
        #returns True if a pos is free, otherwise returns False
        #if color then checks if pos is free FROM color
        #staticmethod or classmethod???
        
        if color:
            for figure in Figure.figures_lst:
                if figure.pos == pos and figure.color == color:
                    return False
            return True
        
        
        for figure in Figure.figures_lst:
            if figure.pos == pos:
                return False
            
        return True
    
    def Move(self, desired_pos):
        self.pos = desired_pos
        myBoard.update()
        print(myBoard)




# p = pawn, Q = queen, K = king, k = knight, b = bishop, r = rook

    def isLegalMove(self, desired_pos):
        #RULE 1: must not move to a tile where there is a friendly figure
        if Figure.isFree(desired_pos, self.color) == False:
            print("RULE1")
            return False
        
        #RULE 2: must move at all
        if self.pos == desired_pos:
            return False
        
        # - 1 - WHITE PAWN MOVES - 1 - 
        if self.name == "p" and self.color == "white":
            #can I move 2 or 1 spots?
            if self.pos[1] == str(2):
                move_ahead = 2
            else:
                move_ahead = 1
            
            #must not move ahead when there is a enemy figure in front
            if desired_pos == self.pos[0] + str(int(self.pos[1]) + 1) and not Figure.isFree(desired_pos):
                return False
            
                
            #no left or right movement except when striking
            if self.pos[0] != desired_pos[0]:
                #must not move left or right if there is no enemy there
                if Figure.isFree(desired_pos, "black"):
                    return False
                #must not move more than 1 tile either left or right
                possible_pos_when_striking = [chr(ord(self.pos[0]) - 1), self.pos[0], chr(ord(self.pos[0]) + 1)]
                if desired_pos[0] not in possible_pos_when_striking:
                    return False
                
                
            #must not move backwards
            if int(self.pos[1]) > int(desired_pos[1]):
                return False
            
            #move ahead either 1 or 2
            if int(desired_pos[1]) > int(self.pos[1]) + move_ahead:
                return False
            
            return True
            
            
            
        
        # - 2 - BLACK PAWN MOVES - 2 -
        elif self.name == "p" and self.color == "black":
            #can I move 2 or 1 spots?
            if self.pos[1] == str(7):
                move_backwards = 2
            else:
                move_backwards = 1
            
            #must not move backwards when there is a enemy figure in behind
            if desired_pos == self.pos[0] + str(int(self.pos[1]) - 1) and not Figure.isFree(desired_pos):
                return False
            
            #no left or right movement except when striking
            if self.pos[0] != desired_pos[0]:
                #must not move left or right if there is no enemy there
                if Figure.isFree(desired_pos, "white"):
                    return False
                #must not move more than 1 tile either left or right
                possible_pos_when_striking = [chr(ord(self.pos[0]) - 1), self.pos[0], chr(ord(self.pos[0]) + 1)]
                if desired_pos[0] not in possible_pos_when_striking:
                    return False
                
            #must not move forwards
            if int(self.pos[1]) < int(desired_pos[1]):
                return False
            
            #move backwards either 1 or 2
            if int(desired_pos[1]) - move_backwards > int(self.pos[1]):
                return False
        
            return True
        
            
        
        
    
    def __test__(self):
        pass
    
    
if __name__ == "__main__":
    myBoard = Board(Figure.figures_lst)
    
    #WHITE FIGURES
    white_pawn1 = Figure("p", "white", "A2")
    white_pawn2 = Figure("p", "white", "B2")
    white_pawn3 = Figure("p", "white", "C2")
    white_pawn4 = Figure("p", "white", "D2")
    white_pawn5 = Figure("p", "white", "E2")
    white_pawn6 = Figure("p", "white", "F2")
    white_pawn7 = Figure("p", "white", "G2")
    white_pawn8 = Figure("p", "white", "H2")
    
    white_rook_left = Figure("r", "white", "A1")
    white_rook_right = Figure("r", "white", "H1")
    white_knight_left = Figure("k", "white", "B1")
    white_knight_right = Figure("k", "white", "G1")
    white_bishop_left = Figure("b", "white", "C1")
    white_bishop_right = Figure("b", "white", "F1")
    white_queen = Figure("Q", "white", "D1")
    white_king = Figure("K", "white", "E1")
    
    #BLACK FIGURES
    black_pawn1 = Figure("p", "black", "A7")
    black_pawn2 = Figure("p", "black", "B7")
    black_pawn3 = Figure("p", "black", "C7")
    black_pawn4 = Figure("p", "black", "D7")
    black_pawn5 = Figure("p", "black", "E7")
    black_pawn6 = Figure("p", "black", "F7")
    black_pawn7 = Figure("p", "black", "G7")
    black_pawn8 = Figure("p", "black", "H7")
    
    black_rook_left = Figure("r", "black", "A8")
    black_rook_right = Figure("r", "black", "H8")
    black_knight_left = Figure("k", "black", "B8")
    black_knight_right = Figure("k", "black", "G8")
    black_bishop_left = Figure("b", "black", "C8")
    black_bishop_right = Figure("b", "black", "F8")
    black_queen = Figure("Q", "black", "D8")
    black_king = Figure("K", "black", "E8")
    
    myBoard.update()
    print(myBoard)
    
    def move(fig, pos):
        if fig.isLegalMove(pos):
            fig.Move(pos)
        else:
            print("Move {} to {} not allowed!".format(fig.pos, pos))
    
#    move(white_pawn1, "A4")
#    move(white_pawn1, "A5")
#    move(white_pawn1, "A6")
#    move(white_pawn1, "A7")
#    move(white_pawn1, "B7")
#    
#    move(black_pawn8, "H5")
#    move(black_pawn8, "H4")
#    move(black_pawn8, "H3")
#    move(black_pawn8, "H2")
#    move(black_pawn8, "G2")
    


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
