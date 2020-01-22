from pice import Piece
from move import up, down, rigth, left, bishopDownRigth, bishopDownLeft, bishopUpRigth, bishopUpLeft

class Queen(Piece):
    
    def __init__(self, posx, posy, color, table_map):
        super(Queen, self).__init__(posx, posy, table_map, "Q", move=[up, down, rigth, left, bishopDownRigth, bishopDownLeft, bishopUpRigth, bishopUpLeft], color=color, rangelen=8)
        self.posy = posx
        self.posx = posy