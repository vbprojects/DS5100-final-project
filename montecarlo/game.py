from .die import Die
from typing import List, Union
import pandas as pd
import numpy as np

class Game:
    """Game class, used to represent the results of rolling dice with the same faces, but not necessarily the same weights, some number of times"""
    def __init__(self, dice : List[Die]):
        """
        PURPOSE: Initializes a game with a list of dice

        INPUTS:
        dice  list of Die objects

        OUTPUT:
        None
        """
        for die in dice:
            if not isinstance(die, Die):
                raise TypeError("dice must be a list of Die objects")
        self.dice = dice
    def play(self, n : int) -> None:
        """
        PURPOSE: Rolls each individual die in the game n times and stores the results in an internal DataFrame

        INPUTS:
        n  int, greater than 0

        OUTPUT:
        None
        """
        if not isinstance(n, int):
            raise TypeError("n must be an int")
        if n <= 0:
            raise ValueError("n must be greater than 0")
        df = pd.DataFrame()
        for index, die in enumerate(self.dice):
            cur_dice_rolls = die.roll(n)
            df[index] = cur_dice_rolls
            df.index.name = "roll number"
        self._plays = df
    def show(self, wide : bool = True) -> pd.DataFrame:
        """
        PURPOSE: Returns the results of the game in a DataFrame, either in wide or narrow format.

        INPUTS:
        wide  bool, default True

        OUTPUTS:
        df  pd.DataFrame
        """
        if not isinstance(wide, bool):
            raise ValueError("wide must be a boolean")
        if wide:
            return self._plays.copy()
        else:
            df = self._plays.stack().to_frame('outcomes')
            df.index.names = ["roll number", "die"]
            return df
