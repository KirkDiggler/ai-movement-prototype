class InvalidCoordinate(Exception):
    pass

class HexNode:
    '''
    To allow a gap for the nodes in between 2 stacks
    (row + col) % 2 == 0

    '''
    def __init__(self, data, col, row):
        if (row + col) % 2 != 0:
            raise InvalidCoordinate('The coordinates must add up to an even number.')

        self.data = data
        self.row = row
        self.col = col


class PieceAttributes:
    def __init__(self, health, damage, movement, attack=None):
        self.health = health
        self.damage = damage
        self.movement = movement
        self.attack = attack
 
class NPC(PieceAttributes):
    def __init__(self):
        pass