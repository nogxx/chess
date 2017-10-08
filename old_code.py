# -*- coding: utf-8 -*-

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

# OLD KING MOVES

# METHOD 1: (work in progress)
            #  # must not move more than 1 spot up or down
            # if int(desired_pos[1]) > int(self.pos[1]) + 1 or int(desired_pos[1]) < int(self.pos[1]) - 1:
            #     return False
            # # must not move more than 1 spot right or left
            # if ord(desired_pos[0]) > ord(self.pos[0]) + 1 or ord(desired_pos[0]) < ord(self.pos[0]) - 1:
            #    return False

            # METHOD 2:
            #  return abs(ord(desired_pos[0]) - ord(self.pos[0])) == 1 and desired_pos[1] == self.pos[1] or \
            #        desired_pos[0] == self.pos[0] and abs(int(desired_pos[1]) - int(self.pos[1])) == 1 or \
            #        abs(ord(desired_pos[0]) - ord(self.pos[0])) == 1 and abs(
            #            int(desired_pos[1]) - int(self.pos[1])) == 1

            # METHOD 3:
            # moving_left_or_right_1 = abs(ord(desired_pos[0]) - ord(self.pos[0])) == 1 and desired_pos[1] == self.pos[1]
            # moving_up_or_down_1 = desired_pos[0] == self.pos[0] and abs(int(desired_pos[1]) - int(self.pos[1])) == 1
            # moving_diagonally_1 = abs(ord(desired_pos[0]) - ord(self.pos[0])) == 1 and abs(int(desired_pos[1]) - int(self.pos[1])) == 1
            #
            # return moving_left_or_right_1 or moving_up_or_down_1 or moving_diagonally_1

# selected_figure = None
#
# figure_names = {"p":"pawn", "Q":"queen", "K":"king",
#            "k":"knight", "b":"bishop", "r":"rook" }

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