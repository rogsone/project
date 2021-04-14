import unittest
from portfel import zamalo, Portfel

class portfelTest(unittest.TestCase):
    def podstawow_pieniadz(self):
        portfel = Portfel()
        self.assertEqual(portfel.get_money(),0)
    def test_start(self):
        portfel = Portfel(50)
        self.assertEqual(portfel.get_money(), 50)
    def test_dodaj(self):
        portfel = Portfel(50)
        portfel.add_money(50)
        self.assertEqual(portfel.get_money(), 100)
    def test_odejmij(self):
        portfel = Portfel(50)
        portfel.use_money(20)
        self.assertEqual(portfel.get_money(), 30)
    def test_raise(self):
        portfel = Portfel(199)
        with self.assertRaises(zamalo):
            portfel.use_money(200)



    if __name__ == '__main__':
        unittest.main()