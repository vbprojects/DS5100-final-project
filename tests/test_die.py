import unittest
import numpy as np
from montecarlo.die import Die


class TestDie(unittest.TestCase):
    def test_init(self):
        self.assertRaises(TypeError, Die, np.asarray([1.4, 2, 3]))
        self.assertRaises(ValueError, Die, np.asarray([1, 2, 2]))

    def test_change_weight(self):
        die = Die(np.asarray([1, 2, 3]))
        die.change_weight(2, 2)
        self.assertEqual(die.show().weights[2], 2)
        self.assertRaises(TypeError, die.change_weight, 2, "2")
        self.assertRaises(IndexError, die.change_weight, 4, 2)
        self.assertRaises(ValueError, die.change_weight, 2, -1)
    
    def test_roll(self):
        die = Die(np.asarray([1, 2, 3]))
        die.change_weight(2, 2)
        rolls = die.roll(10)
        self.assertEqual(len(rolls), 10)
        self.assertRaises(TypeError, die.roll, "10")
        self.assertRaises(ValueError, die.roll, -1)
    
    def test_show(self):
        die = Die(np.asarray([1]))
        self.assertEqual(die.show().index[0], 1)
        self.assertEqual(die.show().weights[1], 1)
