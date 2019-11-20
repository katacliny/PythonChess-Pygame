def up(pice, rangelen, currentiteration=0):
    positions = []
    for y in range(pice.posy-rangelen, pice.posy):
        if y > 0:
            positions.append((pice.posx, y))
    return positions


def down(pice, rangelen, currentiteration=0):
    positions = []
    for y in range(pice.posy + 1, pice.posy + rangelen + 1):
        if y < 8:
            positions.append((pice.posx, y))
    return positions


def rigth(pice, rangelen, currentiteration=0):
    positions = []
    for x in range(pice.posx + 1, pice.posx + rangelen + 1):
        if x < 8:
            positions.append((x, pice.posy))
    return positions


def left(pice, rangelen, currentiteration=0):
    positions = []
    for x in range(pice.posx-rangelen, pice.posx):
        if x > 0:
            positions.append((x, pice.posy))
    return positions


def bishopDownRigth(pice, rangelen, currentiteration=0):
    positions = []
    for x in range(pice.posy, pice.posy + rangelen + 1):
        if pice.posx + x < 8 and pice.posy + x < 8:
            positions.append((pice.posx + x, pice.posy + x))
    return positions


def bishopDownLeft(pice, rangelen, currentiteration=0):
    positions = []
    for x in range(pice.posy, pice.posy + rangelen + 1):
        if pice.posx - x >= 0 and pice.posy + x < 8:
            positions.append((pice.posx - x, pice.posy + x))
    return positions


def bishopUpRigth(pice, rangelen, currentiteration=0):
    positions = []
    for x in range(pice.posy - rangelen, pice.posy):
        if pice.posx + (abs(x)) < 8 and pice.posy - abs(x) >= 0:
            positions.append((pice.posx + (abs(x)), pice.posy - abs(x)))
    return positions


def bishopUpLeft(pice, rangelen, currentiteration=0):
    positions = []
    for x in range(pice.posy - rangelen, pice.posy):
        if pice.posx - (abs(x)) >= 0 and pice.posy - abs(x) >= 0:
            positions.append((pice.posx - (abs(x)), pice.posy - abs(x)))
    return positions


def horseDownRigth(pice, rangelen, currentiteration=0):
    positions = []
    if pice.posx + 1 < 8 and pice.posy + rangelen < 8:
        positions.append((pice.posx + 1, pice.posy + rangelen))
        
    return positions


def horseDownLeft(pice, rangelen, currentiteration=0):
    positions = []
    if pice.posx - 1 >= 0 and pice.posy + rangelen < 8:
        positions.append((pice.posx - 1, pice.posy + rangelen))
        
    return positions

def horseUpnLeft(pice, rangelen, currentiteration=0):
    positions = []
    if pice.posx - 1 >= 0 and pice.posy - rangelen >= 0:
        positions.append((pice.posx - 1, pice.posy - rangelen))
        
    return positions


def horseUpnRigth(pice, rangelen, currentiteration=0):
    positions = []
    if pice.posx + 1 < 8 and pice.posy - rangelen >= 0:
        positions.append((pice.posx + 1, pice.posy - rangelen))
        
    return positions
    