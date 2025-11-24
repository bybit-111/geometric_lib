import unittest
import math

from circle import area as circle_area, perimeter as circle_perimeter
from rectangle import area as rectangle_area, perimeter as rectangle_perimeter
from square import area as square_area, perimeter as square_perimeter
from triangle import area as triangle_area, perimeter as triangle_perimeter

class CircleTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = circle_area(0)
        self.assertEqual(res, 0)

    def test_area_one(self):
        res = circle_area(1)
        self.assertAlmostEqual(res, math.pi)

    def test_area_positive(self):
        res = circle_area(3)
        self.assertAlmostEqual(res, math.pi * 9)

    def test_perimeter_zero(self):
        res = circle_perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_one(self):
        res = circle_perimeter(1)
        self.assertAlmostEqual(res, 2 * math.pi)

    def test_perimeter_positive(self):
        res = circle_perimeter(5)
        self.assertAlmostEqual(res, 10 * math.pi)


class RectangleTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = rectangle_area(10, 0)
        self.assertEqual(res, 0)

    def test_area_positive(self):
        res = rectangle_area(4, 5)
        self.assertEqual(res, 20)

    def test_perimeter_zero(self):
        res = rectangle_perimeter(0, 0)
        self.assertEqual(res, 0)

    def test_perimeter_positive(self):
        res = rectangle_perimeter(3, 4)
        self.assertEqual(res, 14)


class SquareTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = square_area(0)
        self.assertEqual(res, 0)

    def test_area_positive(self):
        res = square_area(5)
        self.assertEqual(res, 25)

    def test_perimeter_zero(self):
        res = square_perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_positive(self):
        res = square_perimeter(3)
        self.assertEqual(res, 12)


class TriangleTestCase(unittest.TestCase):

    def test_area_zero(self):
        res = triangle_area(0, 0)
        self.assertEqual(res, 0)

    def test_area_positive(self):
        res = triangle_area(6, 4)
        self.assertEqual(res, 12)

    def test_perimeter_zero(self):
        res = triangle_perimeter(0, 0, 0)
        self.assertEqual(res, 0)

    def test_perimeter_positive(self):
        res = triangle_perimeter(3, 4, 5)
        self.assertEqual(res, 12)