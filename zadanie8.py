import unittest

from bowling_game import Game

class BowlingGameTest(unittest.TestCase):

  def setUp(self):
    self.g = Game()

  def roll_many(self, rolls, pins):
    for roll in range(0, rolls):
      self.g.roll(pins)


  def roll_spare(self):
    self.g.roll(5)
    self.g.roll(5)

  def roll_strike(self):
    self.g.roll(10)

  def test_one_strike(self):
    self.roll_strike()
    self.g.roll(3)
    self.g.roll(6)
    self.assertEqual(self.g.score(), 28)


  def three(self):
    rolls = 1
    pins = 3
    self.roll_many(rolls, pins)
    self.assertEqual(self.g.score(), 3)

  def test_one_spare(self):
    self.roll_spare()
    self.g.roll(3)
    self.roll_many(16, 0)
    self.assertEqual(self.g.score(), 16)


if __name__ == '__main__':
    unittest.main()
