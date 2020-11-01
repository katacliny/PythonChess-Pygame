
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
        
        if len(cls.currentSelection) >= 1 and cls.currentSelection[0][2].p_type == "W":
            cls.currentSelection = []
        if selection not in cls.currentSelection and len(cls.currentSelection) < 2:
            if len(cls.currentSelection) >= 1 and (selection[0], selection[1]) in cls.currentSelection[0][2].getPositions():
                cls.currentSelection.append(selection)
            elif len(cls.currentSelection) >= 1 and not (selection[0], selection[1]) in cls.currentSelection[0][2].getPositions():
                cls.currentSelection = []
            elif len(cls.currentSelection) == 0:
                cls.currentSelection.append(selection)
           

    @staticmethod
    def select(cls):
        if len(cls.currentSelection) > 1:
            second = cls.currentSelection[1][2]
            first = cls.currentSelection[0][2]
            save = (first.posx, first.posy)
            first.posx = second.posx
            first.posy = second.posy
            second.posx = save[0]
            second.posy = save[1]
            
            cls.table_map[cls.currentSelection[0][0]][cls.currentSelection[0][1]] = second
            cls.table_map[cls.currentSelection[1][0]][cls.currentSelection[1][1]] = first
            cls.currentSelection = []

