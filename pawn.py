from pice import Piece
from move import up, down, rigth, left

class Pawn(Piece):
    
    def __init__(self, posx, posy, color, table_map):
        super(Pawn, self).__init__(posx, posy, table_map, "P", move=[down])
        self.posy = posx
        self.posx = posy
        self.color = color
        self.rangelen = 1