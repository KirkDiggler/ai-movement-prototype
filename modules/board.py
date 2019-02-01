class AlreadyLinkedException(Exception):
    pass
class PieceAlreadyExistsException(Exception):
    pass
class InvalidCoordinate(Exception):
    pass
 
class Board:
    def __init__(self, width=None, height=None):
        self.height = height
        self.width = width
        self.pieces = {}

    def add_piece(self, hex, overwrite=False):
        if ('%d-%d' % (hex.col, hex.row)) in self.pieces and not overwrite:
            raise PieceAlreadyExistsException('row %d, col %d is already set.')

        self.pieces['%d-%d' % (hex.col, hex.row)] = hex

    def distance(self, start, end):
        sx, sy, sz = self._convert_to_cube(start)
        ex, ey, ez = self._convert_to_cube(end)

        return int((abs(sx - ex) + abs(sy - ey) + abs(sz - ez)) / 2)

    def _convert_to_cube(self, hex):
        x = hex.col
        z = int((hex.row - hex.col) / 2)
        y = -x-z

        return x, y, z

class HexNode:
    '''
    To allow a gap for the nodes in between 2 stacks
    (row + col) % 2 == 0
B
    '''
    def __init__(self, data, col, row):
        if (row + col) % 2 != 0:
            raise InvalidCoordinate('The coordinates must add up to an even number.')

        self.data = data
        self.row = row
        self.col = col

