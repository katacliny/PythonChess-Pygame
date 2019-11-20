from pice import Piece
from move import up, down, rigth, left, horseDownRigth, horseDownLeft, horseUpnLeft, horseUpnRigth

class Horse(Piece):
        
    def __init__(self, posx, posy, color, table_map):
        super(Horse, self).__init__(posx, posy, table_map, "H", move=[horseDownRigth, horseDownLeft, horseUpnLeft, horseUpnRigth])
        self.posy = posx
        self.posx = posy
        self.color = color
        self.rangelen = 2