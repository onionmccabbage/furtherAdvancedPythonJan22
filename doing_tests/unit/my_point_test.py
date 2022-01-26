# testing the point class
from my_point import Point
import unittest

class testPoint(unittest.TestCase):
    def setUp(self):
        # this is called before each test
        self.point = Point(3,5) # every test will be offered a point at 3-5
    # here are the tests
    def testMoveBy(self):
        self.point.move_by(5,2)
        self.assertEqual(self.point.display(),(8,7))
    def testHypotenuse(self):
        self.point.move_by(2,2) # we are at (5,7)
        self.assertAlmostEqual(self.point.hypot(), 8.60, places=2) # 8.60232.....
    def testPointCounter(self):
        self.assertEqual(Point.points, 3) # there are three Point instances


if __name__ == '__main__':
    unittest.main() # this will look for tests and run them