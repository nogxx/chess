# -*- coding: utf-8 -*-

import unittest

from figure_class import Figure, move
from board_class import Board


class FiguresMovesTest(unittest.TestCase):
    # TO DO: write tests for all figures
    def setUp(self):
        self.testboard = Board()

        # WHITE FIGURES

        # self.test_white_pawn1 = Figure("p", "white", "A2", self.testboard)
        # self.test_white_pawn2 = Figure("p", "white", "B2", self.testboard)
        # self.test_white_pawn3 = Figure("p", "white", "C2", self.testboard)
        # self.test_white_pawn4 = Figure("p", "white", "D2", self.testboard)
        # self.test_white_pawn5 = Figure("p", "white", "E2", self.testboard)
        # self.test_white_pawn6 = Figure("p", "white", "F2", self.testboard)
        # self.test_white_pawn7 = Figure("p", "white", "G2", self.testboard)
        # self.test_white_pawn8 = Figure("p", "white", "H2", self.testboard)

        self.test_white_rook_left = Figure("r", "white", "A1", self.testboard)
        self.test_white_rook_right = Figure("r", "white", "H1", self.testboard)
        self.test_white_knight_left = Figure("k", "white", "B1", self.testboard)
        self.test_white_knight_right = Figure("k", "white", "G1", self.testboard)
        self.test_white_bishop_left = Figure("b", "white", "C1", self.testboard)
        self.test_white_bishop_right = Figure("b", "white", "F1", self.testboard)
        self.test_white_queen = Figure("Q", "white", "D1", self.testboard)
        self.test_white_king = Figure("K", "white", "E1", self.testboard)

        # BLACK FIGURES

        self.test_black_pawn1 = Figure("p", "black", "A7", self.testboard)
        self.test_black_pawn2 = Figure("p", "black", "B7", self.testboard)
        self.test_black_pawn3 = Figure("p", "black", "C7", self.testboard)
        self.test_black_pawn4 = Figure("p", "black", "D7", self.testboard)
        self.test_black_pawn5 = Figure("p", "black", "E7", self.testboard)
        self.test_black_pawn6 = Figure("p", "black", "F7", self.testboard)
        self.test_black_pawn7 = Figure("p", "black", "G7", self.testboard)
        self.test_black_pawn8 = Figure("p", "black", "H7", self.testboard)

        self.test_black_rook_left = Figure("r", "black", "A8", self.testboard)
        self.test_black_rook_right = Figure("r", "black", "H8", self.testboard)
        self.test_black_knight_left = Figure("k", "black", "B8", self.testboard)
        self.test_black_knight_right = Figure("k", "black", "G8", self.testboard)
        self.test_black_bishop_left = Figure("b", "black", "C8", self.testboard)
        self.test_black_bishop_right = Figure("b", "black", "F8", self.testboard)
        self.test_black_queen = Figure("Q", "black", "D8", self.testboard)
        self.test_black_king = Figure("K", "black", "E8", self.testboard)

        self.testboard.update()
        # print(self.testboard)

        self.results = []

    def testKnightMoves(self):
        for move_ in ["C3", "E4", "G4", "C5", "D7", "F8", "D5", "H8", "G6"]:
            self.results.append(move(self.test_white_knight_left, move_, self.testboard, False))

        self.assertEqual(self.results, [True, True, False, True, True, True, False, False, True])

    def testQueenMoves(self):
        for move_ in ["D2", "D4", "H7", "G7", "H8", "E5", "G6", "F6", "I6", "B6", "A5"]:
            self.results.append(move(self.test_white_queen, move_, self.testboard, False))

        self.assertEqual(self.results, [True, True, False, True, True, True, False, True, False, True, True])

    def testKingMoves(self):
        for move_ in ["D1", "D2", "E3", "E2", "E4", "C2", "G4", "E3"]:
            self.results.append(move(self.test_white_king, move_, self.testboard, False))

        self.assertEqual(self.results, [False, True, True, True, False, False, False, True])

    # def testCheck(self):
    #     for move_ in ["E2", "E3", "E4", "E5", "E6"]:
    #         move(self.test_white_king, move_, self.testboard, True)
    #
    #     self.assertTrue(self.testboard.is_check())

    def tearDown(self):
        self.results = None
        del self.testboard


if __name__ == "__main__":
    unittest.main()
