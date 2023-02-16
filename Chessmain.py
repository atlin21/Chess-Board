'''module is responsible for taking in user input and displaying the board
'''
import pygame as p
from Chess import Chessengine
Width = Height = 600
# ^larger number higher resolution
Dimension = 8
# ^ dimensions of the chess board(8x8)
SQ_Size = Height // Dimension
# ^square size
Max_Fps = 15
# ^ for the animation of moves
Images = {}

def load_images():
    pieces = ['wp', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bp', 'bR', 'bN', 'bB', 'bK', 'bQ']
    for piece in pieces:
        Images[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQ_Size, SQ_Size))

def main():
    p.init()
    screen = p.display.set_mode((Width, Height))
    clock = p.time.Clock()
    screen.fill(p.Color("black"))
    gs = Chessengine.Game_State()
    valid_moves = gs.get_valid_moves()
    move_made = False #when a user makes an invalid move, triggers and error
    load_images()
    running = True
    sq_Selected = ()
    # no square selected initially
    player_Clicks = []
    # documents users clicks(row, collum) EX. two Tuples: (4, 2), (4, 4)

    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                # e.type = event type
                location = p.mouse.get_pos()
                # ^x and y location of mouse
                coll = location[0] // SQ_Size
                row = location[1] // SQ_Size
                if sq_Selected == (row, coll):
                    # ^if the user clicks the same square twice
                    sq_Selected = ()
                    # un select initial square
                    player_Clicks = []
                    # reset clicks
                else:
                    sq_Selected = (row, coll)
                    player_Clicks.append(sq_Selected)
                    #append both first and second clicks
                if len(player_Clicks) == 2:
                    move = Chessengine.Move(player_Clicks[0], player_Clicks[1], gs.board)
                    print(move.get_chess_notation())
                    if move in valid_moves:
                        gs.make_move(move)
                        move_made = True
                    gs.make_move(move)
                    sq_Selected = ()
                    # resets clicks
                    player_Clicks = []
        if move_made:
            valid_moves = gs.get_valid_moves()
            move_made = True
        draw_game_state(screen, gs)
        clock.tick(Max_Fps)
        p.display.flip()
def draw_game_state(screen, gs):
    draw_board(screen)
    # ^draws the squares
    draw_pieces(screen, gs.board)
    # ^draws the pieces on the squares

def draw_board(screen):
    colors = [p.Color("white"), p.Color("yellow")]
    for r in range(Dimension): # for the 8 rows
        for c in range(Dimension): # for the 8 collumns
            color = colors[((r + c) % 2)]
            # determines the color based on the sum of the row and the collumns tiles, if the sum is even, its white
            p.draw.rect(screen, color, p.Rect(c * SQ_Size, r * SQ_Size, SQ_Size, SQ_Size ))
def draw_pieces(screen, board):
# draws pieces based off current instance of the board
    for r in range(Dimension):
        for c in range(Dimension):
            piece = board[r][c]
            if piece != "--":
                # ^if the location or tile is not empty("--")
                screen.blit(Images[piece], p.Rect(c * SQ_Size,r * SQ_Size, SQ_Size, SQ_Size ))
                # .blit is the term for Block transfer which is how you copy contents from one surface on to another
                # essentially overlapping photos in this case causing the image you paste to remain on the top layer

if __name__ == "__main__":
    main()