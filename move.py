def up(piece, rangelen, currentiteration=0):
    positions = []
    for y in range(piece.posy-rangelen, piece.posy):
        if y > 0:
            positions.append((piece.posx, y))
    return positions


def down(piece, rangelen, currentiteration=0):
    positions = []
    for y in range(piece.posy + 1, piece.posy + rangelen + 1):
        if y < 8:
            positions.append((piece.posx, y))
    return positions


def rigth(piece, rangelen, currentiteration=0):
    positions = []
    for x in range(piece.posx + 1, piece.posx + rangelen + 1):
        if x < 8:
            positions.append((x, piece.posy))
    return positions


def left(piece, rangelen, currentiteration=0):
    positions = []
    for x in range(piece.posx-rangelen, piece.posx):
        if x > 0:
            positions.append((x, piece.posy))
    return positions


def bishopDownRigth(piece, rangelen, currentiteration=0):
    positions = []
    for x in range(piece.posy, piece.posy + rangelen + 1):
        if piece.posx + x < 8 and piece.posy + x < 8:
            positions.append((piece.posx + x, piece.posy + x))
    return positions


def bishopDownLeft(piece, rangelen, currentiteration=0):
    positions = []
    for x in range(piece.posy, piece.posy + rangelen + 1):
        if piece.posx - x >= 0 and piece.posy + x < 8:
            positions.append((piece.posx - x, piece.posy + x))
    return positions


def bishopUpRigth(piece, rangelen, currentiteration=0):
    positions = []
    for x in range(piece.posy - rangelen, piece.posy):
        if piece.posx + (abs(x)) < 8 and piece.posy - abs(x) >= 0:
            positions.append((piece.posx + (abs(x)), piece.posy - abs(x)))
    return positions


def bishopUpLeft(piece, rangelen, currentiteration=0):
    positions = []
    for x in range(piece.posy - rangelen, piece.posy):
        if piece.posx - (abs(x)) >= 0 and piece.posy - abs(x) >= 0:
            positions.append((piece.posx - (abs(x)), piece.posy - abs(x)))
    return positions


def horseDownRigth(piece, rangelen, currentiteration=0):
    positions = []
    if piece.posx + 1 < 8 and piece.posy + rangelen < 8:
        positions.append((piece.posx + 1, piece.posy + rangelen))
        
    return positions


def horseDownLeft(piece, rangelen, currentiteration=0):
    positions = []
    if piece.posx - 1 >= 0 and piece.posy + rangelen < 8:
        positions.append((piece.posx - 1, piece.posy + rangelen))
        
    return positions

def horseUpnLeft(piece, rangelen, currentiteration=0):
    positions = []
    if piece.posx - 1 >= 0 and piece.posy - rangelen >= 0:
        positions.append((piece.posx - 1, piece.posy - rangelen))
        
    return positions


def horseUpnRigth(piece, rangelen, currentiteration=0):
    positions = []
    if piece.posx + 1 < 8 and piece.posy - rangelen >= 0:
        positions.append((piece.posx + 1, piece.posy - rangelen))
        
    return positions
    