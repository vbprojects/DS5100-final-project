import unittest
import numpy as np
from montecarlo.die import Die
from montecarlo.game import Game
from montecarlo.analyzer import Analyzer

class TestAnalyzer(unittest.TestCase):
    def test_init(self):
        self.assertRaises(ValueError, Analyzer, [1, 2, 3])
        die = Die(np.asarray([1, 2, 3]))
        game = Game([die, die])
        analyzer = Analyzer(game)
    def test_jackpot(self):
        die = Die(np.asarray([1, 2]))
        game = Game([die, die])
        analyzer = Analyzer(game)
        game.play(10)
        self.assertEqual(type(analyzer.jackpot()), int)
    def test_face_count(self):
        die = Die(np.asarray([1, 2, 3]))
        game = Game([die, die])
        analyzer = Analyzer(game)
        game.play(10)
        face_count_df = analyzer.face_count()
        self.assertEqual(face_count_df.shape[0], 10)
        self.assertEqual(face_count_df.shape[1], 3)
    def test_combo_count(self):
        die = Die(np.asarray([1, 2]))
        game = Game([die, die])
        analyzer = Analyzer(game)
        game.play(10)
        combo_count_df = analyzer.combo_count()
        combos = combo_count_df['n'].index.to_list()
        self.assertTrue((1, 1) in combos and (1, 2) in combos and (2, 2) in combos)
    def test_permutation_count(self):
        die = Die(np.asarray([1, 2]))
        game = Game([die, die])
        analyzer = Analyzer(game)
        game.play(10)
        perm_count_df = analyzer.permutation_count()
        perms = perm_count_df['n'].index.to_list()
        self.assertTrue((1, 1) in perms and (1, 2) in perms and (2, 1) in perms and (2, 2) in perms)

if __name__ == '__main__':
    unittest.main()