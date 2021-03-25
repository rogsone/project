import unittest


class klub():
    def __init__(self):
        self.klubztrenerem = False
    def klubztrenerem1(self):
        self.klubztrenerem = True

class testklub(unittest.TestCase):
    def setUp(self):
        self.klub = klub()
    def test_klub_pusty(self):
        self.assertFalse(self.klub.klubztrenerem)
    def test_klub_trener(self):
        self.klub.klubztrenerem1()
        self.assertTrue(self.klub.klubztrenerem)



print(testklub)

