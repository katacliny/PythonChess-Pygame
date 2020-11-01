
class HandlerTableMove:

    currentSelection = []
    table_map = []
    block = False
    
    def interchange(self):
        print("intercambio")

    @staticmethod
    def getCurrentSelection(cls):

        return cls.currentSelection

    @staticmethod
    def setSelection(cls, selection):
        if selection not in cls.currentSelection and len(cls.currentSelection) < 2:
            cls.currentSelection.append(selection)

    @staticmethod
    def select(cls):
        if len(cls.currentSelection) > 1:
            first = cls.currentSelection[1][2]
            second = cls.currentSelection[0][2]
            save = (second.posx, second.posy)
            second.posx = first.posx
            second.posy = first.posy
            first.posx = save[0]
            first.posy = save[1]
            cls.table_map[cls.currentSelection[0][0]][cls.currentSelection[0][1]] = first
            cls.table_map[cls.currentSelection[1][0]][cls.currentSelection[1][1]] = second
          
            cls.currentSelection = []

