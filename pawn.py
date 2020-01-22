from pice import Piece
from move import up, down, rigth, left

class Pawn(Piece):
    
    def __init__(self, posx, posy, color, table_map, isBlack = False):
        super(Pawn, self).__init__(posx, posy, table_map, "P", move=[down if not isBlack else up], color=color, rangelen=1)
        self.posy = posx
        self.posx = posy