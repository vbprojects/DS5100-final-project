import unittest
import numpy as np
from montecarlo.die import Die
from montecarlo.game import Game

class TestGame(unittest.TestCase):
    def test_init(self):
        self.assertRaises(TypeError, Game, [1, 2, 3])
        game = Game([Die(np.asarray([1, 2, 3])), Die(np.asarray([1, 2, 3]))])
        self.assertEqual(len(game.dice), 2)
        self.assertEqual(game.dice[0].show().index[0], 1)
    def test_play(self):
        game = Game([Die(np.asarray([1, 2, 3])), Die(np.asarray([1, 2, 3]))])
        self.assertRaises(TypeError, game.play, "10")
        self.assertRaises(ValueError, game.play, -1)
        game.play(10)
        self.assertEqual(game._plays.shape[0], 10)
    def test_show(self):
        game = Game([Die(np.asarray([1, 2, 3])), Die(np.asarray([1, 2, 3]))])
        game.play(10)
        wide_df = game.show()
        self.assertEqual(wide_df.shape[0], 10)
        self.assertEqual(wide_df.shape[1], 2)
        narrow_df = game.show(False)
        self.assertEqual(narrow_df.shape[0], 20)
        self.assertEqual(narrow_df.shape[1], 1)
        self.assertRaises(ValueError, game.show, "True")