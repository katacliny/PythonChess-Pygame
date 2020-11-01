from piece import Piece

class WhiteSpace(Piece):
    
    def __init__(self, posx, posy, color, table_map):
        super(WhiteSpace, self).__init__(posx, posy, table_map, "W", move=[], color=color, rangelen=0)
        self.posy = posx
        self.posx = posy

class Table:
    
    table_map = [   [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],]

    table_pieces = []
    
    @staticmethod
    def getTableMap(cls):
        
        return cls.table_map
    
    @staticmethod
    def updateTableMap(cls, table_map):
        cls.table_map = table_map

    def deletepiece(self, piece):
        self.table_pieces.remove(piece)

    def addpiece(self, posy, posx, piece):
        self.table_map[posx][posy] = piece

    def render(self, display, py, font):
        contx = 0
        conty = 0
        for row in self.table_map:
            for piece in row:
                if piece == 0:
                    self.table_map[contx][conty] = WhiteSpace(conty, contx, (255,255,255), self.table_map)
                else:
                    piece.render(display, py, self.table_map, font)
                conty+=1
            contx += 1
            conty = 0