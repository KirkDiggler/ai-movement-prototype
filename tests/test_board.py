import unittest
from context import board

class TestBoard(unittest.TestCase):
    def test_distance(self):
        b = board.Board()
        distance = b.distance(board.HexNode(data={}, row=2, col=2), board.HexNode(data={}, row=7, col=5))

        self.assertEqual(4, distance)
