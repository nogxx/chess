# -*- coding: utf-8 -*-

# p = pawn, Q = queen, K = king, k = knight, b = bishop, r = rook


class Board:
    # takes pos from each figure and creates and prints a board
    # set_pos_to_figures() and update() merge??
    
    def __init__(self, figures_lst=[], visible_board=[]):
        self.figures_lst = figures_lst  # not actually positions but instances of the Figures class
        self.visible_board = visible_board

    def is_free(self, pos, color=None):
        """ returns True if a pos is free, otherwise returns False

        if color then checks if pos is free FROM color

        """

        # staticmethod or classmethod???

        if color:
            for figure in self.figures_lst:
                if figure.pos == pos and figure.color == color:
                    return False
            return True

        for figure in self.figures_lst:
            if figure.pos == pos:
                return False

        return True

    def is_check(self):
        """ returns True if any figure could strike a Kind, else False"""
        for fig in self.figures_lst:
            if fig.name == "K" and fig.color == "white":
                print("found white king")
                white_king_pos = fig.pos
            elif fig.name == "K" and fig.color == "black":
                print("found black king", fig.name, fig.color, fig.pos)
                black_king_pos = fig.pos

        # loop through all white figures and look if anyone can kill the king

        print(black_king_pos, white_king_pos)
        for fig in self.figures_lst:
            if fig.color == "white" and fig.is_legal_move(black_king_pos):
                return True
            elif fig.color == "black" and fig.is_legal_move(white_king_pos):
                return True

        return False



    def del_and_move_and_update(self, desired_pos, a_figure, output=True):
        """ move figure??

        removes an instance of the Figure class from self.figures_lst

        """

        for figure_ in self.figures_lst:
            if figure_.pos == desired_pos:
                self.figures_lst.remove(figure_)


        for figure_ in self.figures_lst:
            figure_.pos = desired_pos

        self.update()

        if output:  # output should only ever be False if you want to unittest
            print(self)
    
    def __set_pos_to_figures(self):
            
        figures_table = [
            {"A8": "_", "B8": "_", "C8": "_", "D8": "_", "E8": "_", "F8": "_", "G8": "_", "H8": "_"},
            {"A7": "_", "B7": "_", "C7": "_", "D7": "_", "E7": "_", "F7": "_", "G7": "_", "H7": "_"},
            {"A6": "_", "B6": "_", "C6": "_", "D6": "_", "E6": "_", "F6": "_", "G6": "_", "H6": "_"},
            {"A5": "_", "B5": "_", "C5": "_", "D5": "_", "E5": "_", "F5": "_", "G5": "_", "H5": "_"},
            {"A4": "_", "B4": "_", "C4": "_", "D4": "_", "E4": "_", "F4": "_", "G4": "_", "H4": "_"},
            {"A3": "_", "B3": "_", "C3": "_", "D3": "_", "E3": "_", "F3": "_", "G3": "_", "H3": "_"},
            {"A2": "_", "B2": "_", "C2": "_", "D2": "_", "E2": "_", "F2": "_", "G2": "_", "H2": "_"},
            {"A1": "_", "B1": "_", "C1": "_", "D1": "_", "E1": "_", "F1": "_", "G1": "_", "H1": "_"},
            ]

        assert "figure" not in locals()

        # can probably be improved - list comprehension???
        for line in figures_table:
            for tile in line:
                for figure in self.figures_lst:
                    if tile == figure.pos:
                        line[tile] = figure.name
        
        return figures_table

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
