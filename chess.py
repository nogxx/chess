""" CHESS - WORK IN PROGRESS

p = pawn, Q = queen, K = king, k = knight, b = bishop, r = rook

TO DO LIST:

- unittest
- GUI

- TURN STARTS HERE -

"""

from figure_class import Figure, move
from board_class import Board

# while True:
#     selected_tile = input("What tile do you want to select? ")
#     if selected_tile not in figures_list:
#         print("This is not an available tile.")
#         continue
#     else:
#         break
#
#
#
# selected_figure = None
#
# figure_names = {"p":"pawn", "Q":"queen", "K":"king",
#            "k":"knight", "b":"bishop", "r":"rook" }
#
# while selected_figure == None:
#     for row in chess_f.figures:
#         for key in row:
#             if key == selected_tile:
#                 selected_figure = row[key]
#                 if row[key] == "_":
#                     print("This tile is empty.")
#                     selected_figure = None
#                     selected_tile = input("What tile do you want to select? ")
#                 else:
#                     print("You have selected your {}.\n".
#                           format(figure_names[selected_figure]))
#
# #creating move
#
# possible_moves = {"pawn":{1:"up_1", 2:"up_2", 3:"up_left_1", 4:"up_right_1"},
#
#                   "queen":{1:"up_x", 2:"down_x", 3:"left_x", 4:"right_x",
#                        5:"up_right_x", 6:"up_left_x", 7:"down_right_x", 8:"down_left_x"},
#
#                   "king":{1:"up_1", 2:"down_1", 3:"left_1", 4:"right_1",
#                        5:"up_right_1", 6:"up_left_1", 7:"down_right_1", 8:"down_left_1"},
#
#                   "knight":{"?????"},
#
#                   "bishop":{1:"down_left_x", 2:"down_right_x", 3:"up_left_x", 4:"up_right_x"},
#
#                   "rook":{1:"up_x", 2:"down_x", 3:"left_x", 4:"right_x"},
#
#                   }
#
# print("The possible moves for {} are:\n".format(figure_names[selected_figure]))
#
# for move in possible_moves[figure_names[selected_figure]]:
#     print(move, ":", possible_moves[figure_names[selected_figure]][move])
#
# print("\n")
#
# while True:
#     try:
#         selected_move = int(input("Move number? "))
#         if selected_move not in possible_moves[figure_names[selected_figure]]:
#             print("This move is not available. ")
#         else:
#             break
#     except:
#         print("Please input a number!")

#if __name__ == "__main__":