#test math functions
import unittest
import circles

class KnownValues(unittest.TestCase):
    #test add
    def test_add(self):
        self.assertEqual(circles.add(10,5),15)
        self.assertEqual(circles.add(-1,1),0)
        self.assertEqual(circles.add(1,-1),0)

    def test_subtract(self):
        self.assertEqual(circles.subtract(10,5),5)
        self.assertEqual(circles.subtract(-1,1),-2)
        self.assertEqual(circles.subtract(1,-1),2)

    def test_multiply(self):
        self.assertEqual(circles.multiply(10,5),50)
        self.assertEqual(circles.multiply(-1,1),-1)
        self.assertEqual(circles.multiply(1,-1),-1)
        self.assertEqual(circles.multiply(1,0),0)


    def test_divide(self):
        self.assertEqual(circles.divide(10,5),2)
        self.assertEqual(circles.divide(-1,1),-1)
        self.assertEqual(circles.divide(1,-1),-1)

        with self.assertRaises(ValueError):
            circles.divide(10,0)


if __name__ == '__main__':
    unittest.main()
