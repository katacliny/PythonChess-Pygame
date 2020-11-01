from piece import Piece

class WhiteSpace(Piece):
    
    @staticmethod
    def render(posx, posy, display, py, table_map):
        
        py.draw.rect(display, (200, 200, 200), (50 * posx, 50 * posy, 50, 50), True)

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
                    pass
                else:
                    piece.render(display, py, self.table_map, font)
                conty+=1
            contx += 1
            conty = 0