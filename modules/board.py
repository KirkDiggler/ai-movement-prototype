class AlreadyLinkedException(Exception):
    pass
 
class Board:
    def __init__(self, width, height):
        self.height = height
        self.width = width

    def build(self):
        pass

        
class HexNode:
    def __init__(self, item):
        self.sides = 6
        self.item = item
        self._nodes = [None] * self.sides

    '''
    Link 2 nodes for the given side. 
    The index of the node sides goes around counter clockwise with 0 at the bottom.

    Th linkable nodes would be 3 apart. 
    Side 0 can link to side 3, 1 can link to 4 and 2 to 5
    '''
    def link_nodes(self, side, node):
        if side > self.sides:
            raise IndexError("%d is out of range for %d sides" % (side, self.sides))

        self.set_side(side, node)

        # TODO: calculate the adjustment on sides 
        if side < 3:
            paired_side = side + 3
        else:
            paired_side = side - 3

        node.set_side(paired_side, self)

    def get_side(self, side):
        return self._nodes[side]

    def set_side(self, side, node):
        if self.get_side(side) is not None:
            raise AlreadyLinkedException("side %d is already linked" & side)

        # Both sides are available, time to link
        self._nodes[side] = node

