from pice import Piece

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

    table_pices = []
    
    @staticmethod
    def getTableMap(cls):
        
        return cls.table_map
    
    @staticmethod
    def updateTableMap(cls, table_map):
        cls.table_map = table_map

    def deletePice(self, pice):
        self.table_pices.remove(pice)

    def addPice(self, posy, posx, pice):
        self.table_map[posx][posy] = pice

    def render(self, display, py, font):
        contx = 0
        conty = 0
        for row in self.table_map:
            for pice in row:
                if pice is 0:
                    pass
                else:
                    pice.render(display, py, self.table_map, font)
                conty+=1
            contx += 1
            conty = 0