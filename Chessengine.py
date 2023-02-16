'''This module is responsible for storing information about the state of the chess game
also determines valid moves at each instance
creates a move log '''

class Game_State():
    def __init__(self):
        # board is an 8x8 2d list, each entry of the list has 2 attributes
        # the first letter being the color of the piece
        # the second being the type of piece
        # "--" represent empty spaces, squares with no pieces
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]

        ]
        self.White_To_Move = True
        self.Move_log = []
    def make_move(self, move):
        self.board[move.start_row][move.start_coll] = "--"
        self.board[move.end_row][move.end_coll] = move.piece_moved
        self.Move_log.append(move)
        self.White_To_Move = not self.White_To_Move

#def track_pieces(self):

    def get_pawn_moves(self, r, c, moves):
        pass
    def get_rook_moves(selfself, r, c, moves):
        pass
    def get_valid_moves(self):
        '''considers moves involving checks'''
        return self.get_possible_moves()

    def get_possible_moves(self):
        '''does not take in consideration of checks'''
        for r in range(len(self.board)):
            for c in range(len(self.board)):
                color = self.board[r][c][0]
                if (color == 'w' and self.White_To_Move) and (color == 'b' and not self.White_To_Move) :
                    piece = self.board[r][c][1]
                    if piece == 'p':
                        self.get_pawn_moves(r, c, moves)
                    elif piece == 'r':
                        self.get_rook_moves(r, c, moves)
        moves = [(6,4), (4,4), self.board]
        return moves


class Move():

    def __init__(self, initSq, endSq, board):
        self.start_row = initSq[0]
        self.start_coll = initSq[1]
        self.end_row = endSq[0]
        self.end_coll = endSq[1]
        self.piece_moved = board[self.start_row][self.start_coll]
        self. piece_captured = board[self.end_row][self.end_coll]
        self.move_ID = self.start_row * 100 + self.start_coll * 100 + self.end_row * 10 + self.end_coll
        print(self.move_ID)
    ranks_to_rows = {"1": 7, "2": 6, "3": 5, "4": 4,
                     "5": 3, "6": 2, "7": 1, "8": 0}
    rows_to_ranks = {v: k for k, v in ranks_to_rows.items()}
    files_to_colls = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4,
                     "f": 5, "g": 6, "h": 7}
    colls_to_files = {v: k for k, v in files_to_colls.items()}

    def __eq__(self, other):
        #comparing an object with an other object
        if isinstance(other, Move):
            return self.move_ID == other.move_ID
        return False

    def get_chess_notation(self):
        return self.get_rank_file(self.start_row, self.start_coll) + " " + "to" + " " + self.get_rank_file(self.end_row, self.end_coll)
    def get_rank_file(self, r, c):
        return self.colls_to_files[c] + self.rows_to_ranks[r]