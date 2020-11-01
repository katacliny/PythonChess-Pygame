from piece import Piece
from move import up, down, rigth, left

class Tower(Piece):
    
    def __init__(self, posx, posy, color, table_map):
        super(Tower, self).__init__(posx, posy, table_map, "T", move=[up, down, rigth, left], color=color, rangelen=8)
        self.posy = posx
        self.posx = posy