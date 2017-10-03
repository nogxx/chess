# -*- coding: utf-8 -*-

# p = pawn, Q = queen, K = king, k = knight, b = bishop, r = rook


class Board:
    # takes pos from each figure and creates and prints a board
    # set_pos_to_figures() and update() merge??
    
    def __init__(self, positions, visible_board=[]):
        self.positions = positions  # not actually positions but instances of the Figures class
        self.visible_board = visible_board
    
    def __set_pos_to_figures(self):
            
        figures = [
            {"A8": "_", "B8": "_", "C8": "_", "D8": "_", "E8": "_", "F8": "_", "G8": "_", "H8": "_"},
            {"A7": "_", "B7": "_", "C7": "_", "D7": "_", "E7": "_", "F7": "_", "G7": "_", "H7": "_"},
            {"A6": "_", "B6": "_", "C6": "_", "D6": "_", "E6": "_", "F6": "_", "G6": "_", "H6": "_"},
            {"A5": "_", "B5": "_", "C5": "_", "D5": "_", "E5": "_", "F5": "_", "G5": "_", "H5": "_"},
            {"A4": "_", "B4": "_", "C4": "_", "D4": "_", "E4": "_", "F4": "_", "G4": "_", "H4": "_"},
            {"A3": "_", "B3": "_", "C3": "_", "D3": "_", "E3": "_", "F3": "_", "G3": "_", "H3": "_"},
            {"A2": "_", "B2": "_", "C2": "_", "D2": "_", "E2": "_", "F2": "_", "G2": "_", "H2": "_"},
            {"A1": "_", "B1": "_", "C1": "_", "D1": "_", "E1": "_", "F1": "_", "G1": "_", "H1": "_"},
            ]

        # can probably be improved - list comprehension???
        for line in figures:
            for tile in line:
                for position in self.positions:
                    if tile == position.pos:
                        line[tile] = position.name
        
        return figures

    
    def update(self):
        """ Updates self.visible_board with figures """
        self.visible_board.clear()
        figures = self.__set_pos_to_figures()
          
        for line in figures:
            lst = []
            for tile in line:
                lst.append(line[tile])
            self.visible_board.append(lst)
        
#        return self.visible_board - neccessary in any situation?

    def __str__(self):
        """ returns visible_board in the correct format """
        counter = 8
        res = ""
        res += "    _   _   _   _   _   _   _   _\n"
        
        for row in self.visible_board:
            res += str(counter) + " | " + " | ".join(row) + " |\n"
            counter -= 1
        res += "    A   B   C   D   E   F   G   H\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n"
        
        return res
