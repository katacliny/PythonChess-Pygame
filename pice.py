from handletablemove import HandlerTableMove

class Piece:
    
    def __init__(self, posx, posy, table_map, p_type="N", text_color=(0,0,0), move = [], rangelen = 1, color = ()):
        self.posx = posx
        self.posy = posy
        self.table_map = table_map
        self.higthLight = (250, 0, 0)
        self.p_type = p_type
        self.text_color = text_color
        self.is_selected = False
        self.move = move
        self.color = color
        self.rangelen = rangelen

    def eat(self):
        pass

    def render(self, display, py, table_map, font):
        if self.is_selected:
            for pos in self.getPositions():
                    py.draw.rect(display, (255, 0, 0), (50 * pos[0], 50 * pos[1], 50, 50), True)
        py.draw.rect(display, self.higthLight if self.isOverSelected(py, self)[0] or self.is_selected else self.color, (50 * self.posx, 50 * self.posy, 50, 50), False)
        textsurface = font.render(self.p_type, False, self.text_color)
        display.blit(textsurface,(53 * self.posx, 50 * self.posy))
    
    def rangeAtackShow(self):
        pass
    
    def rangeAtackValidate(self):
        pass
    
    def isOverSelected(self, py, pice):
        mouseposs = py.mouse.get_pos()
        is_over_selected = [False, False]
        if mouseposs[0] > (pice.posx * 50) and mouseposs[0] < (pice.posx * 50) + 50 and mouseposs[1] > (pice.posy * 50) and mouseposs[1] < (pice.posy * 50) + 50:
            if py.mouse.get_pressed()[0] is 1 and not self.is_selected:
                HandlerTableMove.setSelection(HandlerTableMove, (pice.posx, pice.posy, pice))
                HandlerTableMove.table_map = self.table_map
                HandlerTableMove.select(HandlerTableMove)
                self.is_selected = True
            is_over_selected[0] = True
        else:
            if py.mouse.get_pressed()[0] is 1:
                self.is_selected = False
            is_over_selected[0] = False
            
        return is_over_selected
        
    def getPositions(self):

        positions = []
        for x in self.move:
            m = x(self, self.rangelen)
            if m is not None:
               for n in m:
                   if self.table_map[n[0]][n[1]] == 0:
                        positions.append(n)
                   
        return positions
