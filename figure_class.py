# -*- coding: utf-8 -*-

class Figure:
    """Class to create all possible figures.

    also checks if a given move is legal

    """
    # TO DO: ship is_free to Board class??

    figures_lst = []

    def __init__(self, name, color, pos):
        self.name = name
        self.color = color
        self.pos = pos

        Figure.figures_lst.append(self)

    def is_free(pos, color=None):
        # returns True if a pos is free, otherwise returns False
        # if color then checks if pos is free FROM color
        # staticmethod or classmethod???

        if color:
            for figure in Figure.figures_lst:
                if figure.pos == pos and figure.color == color:
                    return False
            return True

        for figure in Figure.figures_lst:
            if figure.pos == pos:
                return False

        return True

    #bad func name?
    def del_and_move_and_update(self, desired_pos, a_board, output=True):
        # I don't have to actually deleted the instance of Figure class. I can just remove it from
        # Figure.figures_list since the board updates its figures from this list. (probably :) )

        for figure_ in Figure.figures_lst:
            if figure_.pos == desired_pos:
                Figure.figures_lst.remove(figure_)

        self.pos = desired_pos
        a_board.update()
        if output:
            print(a_board)

    # p = pawn, Q = queen, K = king, k = knight, b = bishop, r = rook


    def is_legal_move(self, desired_pos):

        # MOST USEFUL FUNCTION!!! NEXT TIME MAKE IT EARLIER x)
        # import to pawns, rook, bishop, queen, king?
        def change_pos(pos, x=0, y=0):
            return chr(ord(pos[0]) + x) + str(int(pos[1]) + y)

        # calculate all possible moves instead???, "K", "k" example

        path = []
        possible_moves = []

        # RULE 1: must not move to a tile where there is a friendly figure
        if not Figure.is_free(desired_pos, self.color):
            print("RULE1")
            return False

        # RULE 2: must move at all
        if self.pos == desired_pos:
            return False

        # RULE 3: must not move beyond the board
        if desired_pos not in [x + str(y) for x in "ABCDEFGH" for y in range(1, 9)]:
            return False

        # - 1 - WHITE PAWN MOVES - 1 - 
        if self.name == "p" and self.color == "white":
            # can I move 2 or 1 spots?
            if self.pos[1] == str(2):
                move_ahead = 2
            else:
                move_ahead = 1

            # must not move ahead when there is a figure in front
            if desired_pos == self.pos[0] + str(int(self.pos[1]) + 1) and not Figure.is_free(desired_pos):
                return False

            # no left or right movement except when striking
            if self.pos[0] != desired_pos[0]:
                # must not move left or right if there is no enemy there
                if Figure.is_free(desired_pos, "black"):
                    return False
                # must not move more than 1 tile either left or right
                possible_pos_when_striking = [chr(ord(self.pos[0]) - 1), self.pos[0], chr(ord(self.pos[0]) + 1)]
                if desired_pos[0] not in possible_pos_when_striking:
                    return False

            # must not move down
            if int(self.pos[1]) > int(desired_pos[1]):
                return False

            # move ahead either 1 or 2
            if int(desired_pos[1]) > int(self.pos[1]) + move_ahead:
                return False

            return True

        # - 2 - BLACK PAWN MOVES - 2 -
        elif self.name == "p" and self.color == "black":
            # can I move 2 or 1 spots?
            if self.pos[1] == str(7):
                move_down = 2
            else:
                move_down = 1

            # must not move down when there is a figure behind
            if desired_pos == self.pos[0] + str(int(self.pos[1]) - 1) and not Figure.is_free(desired_pos):
                return False

            # no left or right movement except when striking
            if self.pos[0] != desired_pos[0]:
                # must not move left or right if there is no enemy there
                if Figure.is_free(desired_pos, "white"):
                    return False
                # must not move more than 1 tile either left or right
                possible_pos_when_striking = [chr(ord(self.pos[0]) - 1), self.pos[0], chr(ord(self.pos[0]) + 1)]
                if desired_pos[0] not in possible_pos_when_striking:
                    return False

            # must not move up
            if int(self.pos[1]) < int(desired_pos[1]):
                return False

            # move down either 1 or 2
            if int(desired_pos[1]) - move_down > int(self.pos[1]):
                return False

            return True

        # - 3 - ROOK MOVES - 3 - 
        elif self.name == "r":
            # must not move diagonally
            if self.pos[0] != desired_pos[0] and self.pos[1] != desired_pos[1]:
                return False

            # must not have a figure in its path moving left/right
            if self.pos[0] != desired_pos[0]:
                distance = ord(desired_pos[0]) - ord(self.pos[0])  # positive = right, negative = left

                if distance > 0:
                    for i in range(1, distance):
                        path.append(chr(ord(self.pos[0]) + i) + self.pos[1])
                else:
                    for i in range(1, -distance):
                        path.append(chr(ord(self.pos[0]) - i) + self.pos[1])

            # must not have a figure in its path moving forward/backward
            if self.pos[1] != desired_pos[1]:
                distance = int(desired_pos[1]) - int(self.pos[1])  # positive = up, negative = down

                # positive = up
                if distance > 0:
                    for i in range(1, distance):
                        path.append(self.pos[0] + str(int(self.pos[1]) + i))
                # negative = down
                else:
                    for i in range(1, -distance):
                        path.append(self.pos[0] + str(int(self.pos[1]) - i))

            for pos in path:
                if not Figure.is_free(pos):
                    return False

            return True

        # - 4 - BISHOP MOVES - 4 - 

        elif self.name == "b":
            # must not move up/down or left/right
            if self.pos[0] == desired_pos[0] or self.pos[1] == desired_pos[1]:
                return False

            distance = abs(ord(desired_pos[0]) - ord(self.pos[0]))

            print(distance)

            # must not have a figure in its path moving right (up or odwn)
            if ord(desired_pos[0]) > ord(self.pos[0]):

                # right/up
                if int(desired_pos[1]) > int(self.pos[1]):
                    for i in range(1, distance):
                        path.append(chr(ord(self.pos[0]) + i) + str(int(self.pos[1]) + i))

                # right/down
                else:
                    for i in range(1, distance):
                        path.append(chr(ord(self.pos[0]) - i) + str(int(self.pos[1]) - i))

            # must not have a figure in its path moving left (up or down)
            elif ord(desired_pos[0]) < ord(self.pos[0]):

                # left/up
                if int(desired_pos[1]) > int(self.pos[1]):
                    for i in range(1, distance):
                        path.append(chr(ord(self.pos[0]) + i) + str(int(self.pos[1]) + i))

                # left/down
                else:
                    for i in range(1, distance):
                        path.append(chr(ord(self.pos[0]) - i) + str(int(self.pos[1]) - i))

            for pos in path:
                if not Figure.is_free(pos):
                    return False

            return True

        # - 5 - QUEEN MOVES - 5 - 

        elif self.name == "Q":

            # must not have a figure in its path moving left/right
            if self.pos[0] != desired_pos[0] and self.pos[1] == desired_pos[1]:
                print(1)
                distance = ord(desired_pos[0]) - ord(self.pos[0])  # positive = right, negative = left

                if distance > 0:
                    for i in range(1, distance):
                        path.append(chr(ord(self.pos[0]) + i) + self.pos[1])
                else:
                    for i in range(1, -distance):
                        path.append(chr(ord(self.pos[0]) - i) + self.pos[1])

            # must not have a figure in its path moving forward/backward
            elif self.pos[1] != desired_pos[1] and self.pos[0] == desired_pos[0]:
                print(2)
                distance = int(desired_pos[1]) - int(self.pos[1])  # positive = up, negative = down

                # positive = up
                if distance > 0:
                    for i in range(1, distance):
                        path.append(self.pos[0] + str(int(self.pos[1]) + i))
                # negative = down
                else:
                    for i in range(1, -distance):
                        path.append(self.pos[0] + str(int(self.pos[1]) - i))

            # must not move in a diagonally line which is not straight (D1 to E5)
            horizontal_distance = abs(ord(desired_pos[0]) - ord(self.pos[0]))
            vertical_distance = abs(int(desired_pos[1]) - int(self.pos[1]))

            # must not have a figure in its path moving right (up or down)
            if ord(desired_pos[0]) > ord(self.pos[0]) and desired_pos[1] != self.pos[1]:

                if horizontal_distance != vertical_distance:
                    return False

                distance = abs(ord(desired_pos[0]) - ord(self.pos[0]))

                print(3)
                # right/up
                if int(desired_pos[1]) > int(self.pos[1]):
                    for i in range(1, distance):
                        path.append(chr(ord(self.pos[0]) + i) + str(int(self.pos[1]) + i))

                # right/down
                else:
                    for i in range(1, distance):
                        path.append(chr(ord(self.pos[0]) - i) + str(int(self.pos[1]) - i))

            # must not have a figure in its path moving left (up or down)
            elif ord(desired_pos[0]) < ord(self.pos[0]) and desired_pos[1] != self.pos[1]:

                if horizontal_distance != vertical_distance:
                    return False

                distance = abs(ord(desired_pos[0]) - ord(self.pos[0]))

                print(4)
                # left/up
                if int(desired_pos[1]) > int(self.pos[1]):
                    for i in range(1, distance):
                        path.append(chr(ord(self.pos[0]) + i) + str(int(self.pos[1]) + i))

                # left/down
                else:
                    for i in range(1, distance):
                        path.append(chr(ord(self.pos[0]) - i) + str(int(self.pos[1]) - i))

            for pos in path:
                if not Figure.is_free(pos):
                    return False

            return True

        # - 6 - KING MOVES - 6 -

        elif self.name == "K":
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

            moving_left_or_right_1 = abs(ord(desired_pos[0]) - ord(self.pos[0])) == 1 and desired_pos[1] == self.pos[1]
            moving_up_or_down_1 = desired_pos[0] == self.pos[0] and abs(int(desired_pos[1]) - int(self.pos[1])) == 1
            moving_diagonally_1 = abs(ord(desired_pos[0]) - ord(self.pos[0])) == 1 and abs(int(desired_pos[1]) - int(self.pos[1])) == 1

            return moving_left_or_right_1 or moving_up_or_down_1 or moving_diagonally_1

        # - 7 - KNIGHT MOVES - 7 -

        elif self.name == "k":
            # left_bot = chr(ord(self.pos[0]) - 2) + str(int(self.pos[1]) - 2)
            # left_top = chr(ord(self.pos[0]) - 2) + str(int(self.pos[1]) + 2)
            # right_bot = chr(ord(self.pos[0]) + 2) + str(int(self.pos[1]) + 2)
            # right_top = chr(ord(self.pos[0]) + 2) + str(int(self.pos[1]) - 2)

            for x, y in (-2, -1), (-1, -2), (1, -2), (2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1):
                possible_moves.append(change_pos(self.pos, x, y))

            return desired_pos in possible_moves



# - 8 - ROCHADE - 8 -
# - 9 - EN PASSANT - 9 -
# - 10 - CHECK - 10 -
# - 11 - CHECKMATE - 11 -
# - 12 - VERWANDLUNG - 12 -

def move(fig, pos, a_board, output=True):
    if fig.is_legal_move(pos):
        if output:
            print("Moving from {} to {}".format(fig.pos, pos))

        fig.del_and_move_and_update(pos, a_board, output)
        return True
    else:
        if output:
            print("Move {} to {} not allowed!\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n".format(fig.pos, pos))
        return False