import unittest
import os






class klub():
    def __init__(self):
        file = open("Kluby.txt", "w")
        file.write("Manchester City, Bayern Monachium")
        file.close()
    def usuniecie(self):
        self.usuniecie = os.remove("Kluby.txt")


class testklub(unittest.TestCase):
    def setUp(self):
        self.klub = klub()
    def tearDown(self):
        self.klub.usuniecie()
    def test_czytaj(self):
        with open("Kluby.txt", "r") as klubby:
            zawartosc = klubby.read()
        self.assertEqual(zawartosc,"Manchester City, Bayern Monachium")




if __name__ == '__main__':
    unittest.main()




