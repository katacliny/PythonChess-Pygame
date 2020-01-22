import pygame as py
from table import Table
from pice import Piece
from pawn import Pawn
from queen import Queen
from bishop import Bishop
from tower import Tower
from horse import Horse
from king import King

display = py.display.set_mode([400, 400])
time = py.time.Clock()
running = 1
py.font.init() 
font = py.font.SysFont('Comic Sans MS', 30)
bishop_color = (200,200,200)
tower_color = (200,200,200)
horse_color = (200,200,200)
king_color = (200,200,200)
quin_color = (200,200,200)
pawn_color = (200, 200, 200)

def mainThread():
    
    table = Table()
    table.addPice(1, 0, Pawn(1, 0, pawn_color, table.table_map))
    table.addPice(1, 1, Pawn(1, 1, pawn_color, table.table_map))
    table.addPice(1, 2, Pawn(1, 2, pawn_color, table.table_map))
    table.addPice(1, 3, Pawn(1, 3, pawn_color, table.table_map))
    table.addPice(1, 4, Pawn(1, 4, pawn_color, table.table_map))
    table.addPice(1, 5, Pawn(1, 5, pawn_color, table.table_map))
    table.addPice(1, 6, Pawn(1, 6, pawn_color, table.table_map))
    table.addPice(1, 7, Pawn(1, 7, pawn_color, table.table_map))
    
    table.addPice(0, 0, Tower(0, 0, tower_color, table.table_map))
    table.addPice(0, 1, Horse(0, 1, horse_color, table.table_map))
    table.addPice(0, 2, Bishop(0, 2, bishop_color, table.table_map))
    table.addPice(0, 3, King(0, 3, king_color, table.table_map))
    table.addPice(0, 4, Queen(0, 4, quin_color, table.table_map))
    table.addPice(0, 5, Bishop(0, 5, bishop_color, table.table_map))
    table.addPice(0, 6, Horse(0, 6, horse_color, table.table_map))
    table.addPice(0, 7, Tower(0, 7, tower_color, table.table_map))
    
    
    table.addPice(6, 0, Pawn(6, 0, pawn_color, table.table_map, True))
    table.addPice(6, 1, Pawn(6, 1, pawn_color, table.table_map, True))
    table.addPice(6, 2, Pawn(6, 2, pawn_color, table.table_map, True))
    table.addPice(6, 3, Pawn(6, 3, pawn_color, table.table_map, True))
    table.addPice(6, 4, Pawn(6, 4, pawn_color, table.table_map, True))
    table.addPice(6, 5, Pawn(6, 5, pawn_color, table.table_map, True))
    table.addPice(6, 6, Pawn(6, 6, pawn_color, table.table_map, True))
    table.addPice(6, 7, Pawn(6, 7, pawn_color, table.table_map, True))
    
    table.addPice(7, 0, Tower(7, 0, tower_color, table.table_map))
    table.addPice(7, 1, Horse(7, 1, horse_color, table.table_map))
    table.addPice(7, 2, Bishop(7, 2, bishop_color, table.table_map))
    table.addPice(7, 3, King(7, 3, king_color, table.table_map))
    table.addPice(7, 4, Queen(7, 4, quin_color, table.table_map))
    table.addPice(7, 5, Bishop(7, 5, bishop_color, table.table_map))
    table.addPice(7, 6, Horse(7, 6, horse_color, table.table_map))
    table.addPice(7, 7, Tower(7, 7, tower_color, table.table_map))
    
    while True: 
        for evento in py.event.get():
            if evento.type == py.QUIT:
                py.quit()
                
        display.fill((255,255,255))
        table.render(display, py, font)
        py.display.flip()
        time.tick(64)
                
                
mainThread()
quit()