from pice import Piece
from move import up, down, rigth, left

class King(Piece):
        
    def __init__(self, posx, posy, color, table_map):
        super(King, self).__init__(posx, posy, table_map, "K", move=[up, down, rigth, left])
        self.posy = posx
        self.posx = posy
        self.color = color
        self.rangelen = 1