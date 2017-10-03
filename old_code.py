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
        