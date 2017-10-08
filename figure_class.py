# -*- coding: utf-8 -*-

class Figure:
    """Class to create all possible figures.

    is_legal_move(self, desired_pos) checks if a move is allowed.

    """

    def __init__(self, name, color, pos, board):
        self.name = name
        self.color = color
        self.pos = pos
        self.board = board

        board.figures_lst.append(self)

    # p = pawn, Q = queen, K = king, k = knight, b = bishop, r = rook

    def is_legal_move(self, desired_pos):
        """ returns True if the proposed move is egal, else False"""

        # import to pawns, rook, bishop, queen?

        # make one big if for path

        def shifted_pos(pos, x=0, y=0):
            """ returns a shifted version of self.pos (x, y). Does NOT change self.pos"""
            return chr(ord(pos[0]) + x) + str(int(pos[1]) + y)

        # calculate all possible moves instead???, "K", "k" example

        path = []

        # RULE 1: must not move to a tile where there is a friendly figure
        if not self.board.is_free(desired_pos, self.color):
            #print("RULE1")
            return False

        # RULE 2: must move at all
        if self.pos == desired_pos:
            #print("RULE2")
            return False

        # RULE 3: must not move beyond the board
        if desired_pos not in [x + str(y) for x in "ABCDEFGH" for y in range(1, 9)]:
            #print("RULE3")
            return False

        # - 1 - WHITE PAWN MOVES - 1 - 
        if self.name == "p" and self.color == "white":
            # can I move 2 or 1 spots?
            if self.pos[1] == str(2):
                move_ahead = 2
            else:
                move_ahead = 1

            # must not move ahead when there is a figure in front
            if desired_pos == self.pos[0] + str(int(self.pos[1]) + 1) and not self.board.is_free(desired_pos):
                return False

            # no left or right movement except when striking
            if self.pos[0] != desired_pos[0]:
                # must not move left or right if there is no enemy there
                if self.board.is_free(desired_pos, "black"):
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
            if desired_pos == self.pos[0] + str(int(self.pos[1]) - 1) and not self.board.is_free(desired_pos):
                return False

            # no left or right movement except when striking
            if self.pos[0] != desired_pos[0]:
                # must not move left or right if there is no enemy there
                if self.board.is_free(desired_pos, "white"):
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
                if not self.board.is_free(pos):
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
                if not self.board.is_free(pos):
                    return False

            return True

        # - 5 - QUEEN MOVES - 5 - 

        elif self.name == "Q":
            # must not have a figure in its path moving left/right
            if self.pos[0] != desired_pos[0] and self.pos[1] == desired_pos[1]:
                distance = ord(desired_pos[0]) - ord(self.pos[0])  # positive = right, negative = left

                if distance > 0:
                    for i in range(1, distance):
                        path.append(chr(ord(self.pos[0]) + i) + self.pos[1])
                else:
                    for i in range(1, -distance):
                        path.append(chr(ord(self.pos[0]) - i) + self.pos[1])

            # must not have a figure in its path moving forward/backward
            elif self.pos[1] != desired_pos[1] and self.pos[0] == desired_pos[0]:
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

                # left/up
                if int(desired_pos[1]) > int(self.pos[1]):
                    for i in range(1, distance):
                        path.append(chr(ord(self.pos[0]) + i) + str(int(self.pos[1]) + i))

                # left/down
                else:
                    for i in range(1, distance):
                        path.append(chr(ord(self.pos[0]) - i) + str(int(self.pos[1]) - i))

            for pos in path:
                if not self.board.is_free(pos):
                    return False

            return True

        # - 6 - KING MOVES - 6 -

        elif self.name == "K":

            for x, y in (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1):
                if shifted_pos(self.pos, x, y) == desired_pos:
                    return True

            return False  # not necessary but I don't know why

        # - 7 - KNIGHT MOVES - 7 -

        elif self.name == "k":

            for x, y in (-2, -1), (-1, -2), (1, -2), (2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1):
                if shifted_pos(self.pos, x, y) == desired_pos:
                    return True

            return False  # not necessary but I don't know why - None and False are both not True


# - 8 - ROCHADE - 8 -
# - 9 - EN PASSANT - 9 -
# - 10 - CHECK - 10 -
# - 11 - CHECKMATE - 11 -
# - 12 - PROMOTION - 12 -


def move(fig, pos, a_board, output=True):
    if fig.is_legal_move(pos):
        if output:
            print("Moving from {} to {}!".format(fig.pos, pos))

        a_board.del_and_move_and_update(pos, a_board, output)
        return True
    else:
        if output:
            print("Move {} to {} not allowed!\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n".format(fig.pos, pos))
        return False