
class HandlerTableMove:

    currentSelection = []
    table_map = []
    
    def interchange(self):

        print("intercambio")

    @staticmethod
    def getCurrentSelection(cls):

        return cls.currentSelection

    @staticmethod
    def setSelection(cls, selection):
        print("entraaaa")
        if selection not in cls.currentSelection:
            cls.currentSelection.append(selection)

    @staticmethod
    def select(cls):
        if len(cls.currentSelection) == 2:
            first = cls.currentSelection[1][2]
            second = cls.currentSelection[0][2]
            cls.table_map[cls.currentSelection[0][0]][cls.currentSelection[0][1]] = first
            cls.table_map[cls.currentSelection[1][0]][cls.currentSelection[1][1]] = second
            print(cls.currentSelection)
            print("hace la seleccion")
            print(cls.table_map)
            cls.currentSelection = []

