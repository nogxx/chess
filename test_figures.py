# -*- coding: utf-8 -*-

import unittest

from figure_class import Figure, move
from board_class import Board

class FiguresMovesTest(unittest.TestCase):
    def setUp(self):
        print("setUp exec.")

    def testMoves(self):
        self.results = []

        # without pawns
        for move_ in ["C3", "E4", "G4", "C5", "D7", "F8", "D5", "H8", "G6"]:
            self.results.append(move(white_knight_left, move_, my_board, False))

        self.assertEqual(self.results, [True, True, False, True, True, True, False, False, True])

    def tearDown(self):
        self.results = None
        print("tearDown exec.")


if __name__ == "__main__":
    my_board = Board(Figure.figures_lst)

    # WHITE FIGURES
    # white_pawn1 = Figure("p", "white", "A2")
    # white_pawn2 = Figure("p", "white", "B2")
    # white_pawn3 = Figure("p", "white", "C2")
    # white_pawn4 = Figure("p", "white", "D2")
    # white_pawn5 = Figure("p", "white", "E2")
    # white_pawn6 = Figure("p", "white", "F2")
    # white_pawn7 = Figure("p", "white", "G2")
    # white_pawn8 = Figure("p", "white", "H2")

    white_rook_left = Figure("r", "white", "A1")
    white_rook_right = Figure("r", "white", "H1")
    white_knight_left = Figure("k", "white", "B1")
    white_knight_right = Figure("k", "white", "G1")
    white_bishop_left = Figure("b", "white", "C1")
    white_bishop_right = Figure("b", "white", "F1")
    white_queen = Figure("Q", "white", "D1")
    white_king = Figure("K", "white", "E1")

    # BLACK FIGURES
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

    my_board.update()
    print(my_board)

    unittest.main()


    for move_ in ["D4", "E5", "C3", "C2", "H2", "F4", "D3", "G5"]:
        move(white_queen, move_)

    for move_ in ["H4", "F2", "G2", "E2", "F3", "F5", "E2", "E3", "E5", "E4", "E3"]:
        move(white_king, move_)
