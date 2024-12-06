import unittest
from mod3 import squareroot as md3


class TestSquareRoot(unittest.TestCase):

    def test_squareroot(self):
        self.assertEqual(md3(0),0)
        self.assertEqual(md3(4),2)
     
unittest.main()