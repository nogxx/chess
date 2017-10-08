""" CHESS - WORK IN PROGRESS

p = pawn, Q = queen, K = king, k = knight, b = bishop, r = rook

TO DO LIST:

- GUI
- rochade, en passant, promotion, check, checkmate

- TURN STARTS HERE -

"""

from figure_class import Figure, move
from board_class import Board

my_board = Board()

# WHITE FIGURES

white_pawn1 = Figure("p", "white", "A2", my_board)
white_pawn2 = Figure("p", "white", "B2", my_board)
white_pawn3 = Figure("p", "white", "C2", my_board)
white_pawn4 = Figure("p", "white", "D2", my_board)
white_pawn5 = Figure("p", "white", "E2", my_board)
white_pawn6 = Figure("p", "white", "F2", my_board)
white_pawn7 = Figure("p", "white", "G2", my_board)
white_pawn8 = Figure("p", "white", "H2", my_board)

white_rook_left = Figure("r", "white", "A1", my_board)
white_rook_right = Figure("r", "white", "H1", my_board)
white_knight_left = Figure("k", "white", "B1", my_board)
white_knight_right = Figure("k", "white", "G1", my_board)
white_bishop_left = Figure("b", "white", "C1", my_board)
white_bishop_right = Figure("b", "white", "F1", my_board)
white_queen = Figure("Q", "white", "D1", my_board)
white_king = Figure("K", "white", "E1", my_board)

# BLACK FIGURES

black_pawn1 = Figure("p", "black", "A7", my_board)
black_pawn2 = Figure("p", "black", "B7", my_board)
black_pawn3 = Figure("p", "black", "C7", my_board)
black_pawn4 = Figure("p", "black", "D7", my_board)
black_pawn5 = Figure("p", "black", "E7", my_board)
black_pawn6 = Figure("p", "black", "F7", my_board)
black_pawn7 = Figure("p", "black", "G7", my_board)
black_pawn8 = Figure("p", "black", "H7", my_board)

black_rook_left = Figure("r", "black", "A8", my_board)
black_rook_right = Figure("r", "black", "H8", my_board)
black_knight_left = Figure("k", "black", "B8", my_board)
black_knight_right = Figure("k", "black", "G8", my_board)
black_bishop_left = Figure("b", "black", "C8", my_board)
black_bishop_right = Figure("b", "black", "F8", my_board)
black_queen = Figure("Q", "black", "D8", my_board)
black_king = Figure("K", "black", "E8", my_board)

my_board.update()
print(my_board)

possible_input = [x + str(y) for x in "ABCDEFGH" for y in range(1, 9)]

while True:
    while True:
        pos1 = input("What tile do you want to select? ")

        if pos1 not in [fig_.pos for fig_ in my_board.figures_lst]:
            print("This tile is empty!")
            continue

        for fig_ in my_board.figures_lst:
            if fig_.pos == pos1:
                fig = fig_

        if pos1 not in possible_input:
            print("This tile is not valid!")
            continue

        else:
            break

    while True:
        desired_pos = input("Where do you want to move? ")

        if desired_pos not in possible_input:
            print("This tile is not valid!")
            continue

        else:
            break

    successful_move = move(fig, desired_pos, my_board)

    if successful_move:
        break



