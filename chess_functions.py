### CREATE AND UPDATE BORAD FUNCTIONS

board = []

figures = [
    {"A8": "r", "B8": "k", "C8": "b", "D8": "Q", "E8": "K", "F8": "b", "G8": "k", "H8": "r"},
    {"A7": "p", "B7": "p", "C7": "p", "D7": "p", "E7": "p", "F7": "p", "G7": "p", "H7": "p"},
    {"A6": "_", "B6": "_", "C6": "_", "D6": "_", "E6": "_", "F6": "_", "G6": "_", "H6": "_"},
    {"A5": "_", "B5": "_", "C5": "_", "D5": "_", "E5": "_", "F5": "_", "G5": "_", "H5": "_"},
    {"A4": "_", "B4": "_", "C4": "_", "D4": "_", "E4": "_", "F4": "_", "G4": "_", "H4": "_"},
    {"A3": "_", "B3": "_", "C3": "_", "D3": "_", "E3": "_", "F3": "_", "G3": "_", "H3": "_"},
    {"A2": "p", "B2": "p", "C2": "p", "D2": "p", "E2": "p", "F2": "p", "G2": "p", "H2": "p"},
    {"A1": "r", "B1": "k", "C1": "b", "D1": "Q", "E1": "K", "F1": "b", "G1": "k", "H1": "r"},
    ]

def update_board():
    """ Updates figures and then adds updated figures to board """
    board.clear()
    counter = 8
    for i, row in enumerate(figures):
        lst = []
        for letter in "ABCDEFGH":
            lst.append(row[letter + str(counter - i)])
        board.append(lst)
    


def print_board(board):
    """ returns the printed board in the correct format """
    counter = 8
    res = ""
    res += "    _   _   _   _   _   _   _   _\n"
    for row in board:
        res += str(counter) + " | " + " | ".join(row) + " |\n"
        counter -= 1
    res += "    A   B   C   D   E   F   G   H"
    return res

update_board()

if __name__ == "__main__":
    print(print_board(board), "\n")



### THEM MOVES FOR CHESS GAME



def up(tile, n):
    """ Move figures on given tile n-steps ahead """
    for i, row in enumerate(figures):
        for key in row:
            if key == tile:
                selected_figure = row[tile]
                row[tile] = "_" #removes figure from selected tile
                number = int(tile[1])
                number += n
                tile = tile[0] + str(number) #changes tile to n-steps forward
                for figure in "prkbQK":
                    if figure == selected_figure:
                        figures[i - n][tile] = figure

                update_board()
                print_board(board)
                
                break


def down(tile, n):
    """ Move figures on given tile n-steps backwards """
    for i, row in enumerate(figures):
        figures_changed = False
        for key in row:
            if key == tile:
                figures_changed = True
                selected_figure = row[tile]
                row[tile] = "_" #removes figure from selected tile
                number = int(tile[1])
                number -= n
                tile = tile[0] + str(number) #changes tile to n-steps backwards
                for figure in "prkbQK":
                    if figure == selected_figure:
                        figures[i + n][tile] = figure

                update_board()
                print_board(board)
                
                break
        if figures_changed == True:
            break


def right(tile, n):
    """ Move figures on given tile n-steps to the right """
    for row in figures:
        letters = "ABCDEFGH"
        figures_changed = False
        for i, key in enumerate(row):
            if key == tile:
                figures_changed = True
                selected_figure = row[tile]
                row[tile] = "_" #removes figure from selected tile
                letter = letters[i + n]
                tile = letter + tile[1] #changes tile to n-steps to the right
                for figure in "prkbQK":
                    if figure == selected_figure:
                        
                        row[tile] = figure

                update_board()
                print_board(board)
                
                break
        if figures_changed == True:
            break


def left(tile, n):
    """ Move figures on given tile n-steps to the left """
    for row in figures:
        letters = "ABCDEFGH"
        figures_changed = False
        for i, key in enumerate(row):
            if key == tile:
                figures_changed = True
                selected_figure = row[tile]
                row[tile] = "_" #removes figure from selected tile
                letter = letters[i - n]
                tile = letter + tile[1] #changes tile to n-steps to the left
                for figure in "prkbQK":
                    if figure == selected_figure:
                        
                        row[tile] = figure

                update_board()
                print_board(board)
                
                break
        if figures_changed == True:
            break



def up_left(tile, n):
    """ Move figures on given tile n-steps to the left and forward """
    for figures_i, row in enumerate(figures):
        letters = "ABCDEFGH"
        figures_changed = False
        for row_i, key in enumerate(row):
            if key == tile:
                figures_changed = True
                selected_figure = row[tile]
                row[tile] = "_" #removes figure from selected tile
                letter = letters[row_i - n]
                number = int(tile[1])
                number += n
                tile = letter + str(number) #changes tile to n-steps to the left and forward
                for figure in "prkbQK":
                    if figure == selected_figure:
                        figures[figures_i - n][tile] = figure

                update_board()
                print_board(board)
                
                break
        if figures_changed == True:
            break


def up_right(tile, n):
    """ Move figures on given tile n-steps to the right and forward """
    for figures_i, row in enumerate(figures):
        letters = "ABCDEFGH"
        figures_changed = False
        for row_i, key in enumerate(row):
            if key == tile:
                figures_changed = True
                selected_figure = row[tile]
                row[tile] = "_" #removes figure from selected tile
                letter = letters[row_i + n]
                number = int(tile[1])
                number += n
                tile = letter + str(number) #changes tile to n-steps to the right and forward
                for figure in "prkbQK":
                    if figure == selected_figure:
                        figures[figures_i - n][tile] = figure

                update_board()
                print_board(board)
                
                break
        if figures_changed == True:
            break


def down_right(tile, n):
    """ Move figures on given tile n-steps to the right and down """
    for figures_i, row in enumerate(figures):
        letters = "ABCDEFGH"
        figures_changed = False
        for row_i, key in enumerate(row):
            if key == tile:
                figures_changed = True
                selected_figure = row[tile]
                row[tile] = "_" #removes figure from selected tile
                letter = letters[row_i + n]
                number = int(tile[1])
                number -= n
                tile = letter + str(number) #changes tile to n-steps to the right and down
                for figure in "prkbQK":
                    if figure == selected_figure:
                        figures[figures_i + n][tile] = figure

                update_board()
                print_board(board)
                
                break
        if figures_changed == True:
            break


def down_left(tile, n):
    """ Move figures on given tile n-steps to the left and down """
    for figures_i, row in enumerate(figures):
        letters = "ABCDEFGH"
        figures_changed = False
        for row_i, key in enumerate(row):
            if key == tile:
                figures_changed = True
                selected_figure = row[tile]
                row[tile] = "_" #removes figure from selected tile
                letter = letters[row_i - n]
                number = int(tile[1])
                number -= n
                tile = letter + str(number) #changes tile to n-steps to the left and down
                for figure in "prkbQK":
                    if figure == selected_figure:
                        figures[figures_i + n][tile] = figure

                update_board()
                print_board(board)
                
                break
        if figures_changed == True:
            break



#break problem down into easier smaller parts

class Figure:
    def __init__(self, figure_type, side, pos):
        self.figure_type = figure_type
        self.side = side
        self.pos = pos
    
    def __test__(self):
        pass
    
    
    
    
    
    
    
