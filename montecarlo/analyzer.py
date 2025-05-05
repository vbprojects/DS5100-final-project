from .game import Game
import pandas as pd
import numpy as np
from typing import List, Union

class Analyzer:
    """Analyzer class, used to analyze the results of a game, including the number of jackpots, the counts of each face, the counts of each combination of faces, and the counts of each permutation of faces"""
    def __init__(self, game : Game) -> None:
        """
        PURPOSE: Initializes an Analyzer object with a Game object

        INPUTS:
        game  Game object

        OUTPUT:
        None
        """
        if not isinstance(game, Game):
            raise ValueError("Must pass a Game object")
        self.game = game
    def jackpot(self) -> int:
        """
        PURPOSE: Returns the number of times all dice show the same face

        INPUTS:
        None

        OUTPUTS:
        int  number of jackpots
        """
        return self.game.show().apply(lambda x: all(x == x[0]), axis = 1).sum().item()
    def face_count(self) -> pd.DataFrame:
        """
        PURPOSE: Returns a DataFrame with the counts of each face for each die

        INPUTS:
        None

        OUTPUTS:
        face_count_df  pd.DataFrame
        """
        records = [self.game.show(wide = False).outcomes[i].value_counts().to_dict() for i in range(self.game.show().shape[0])]
        return pd.DataFrame(records, columns=self.game.dice[0].show().index).fillna(0).astype(int)
    def combo_count(self) -> pd.DataFrame:
        """
        PURPOSE: Returns a DataFrame with the counts of each combination of faces rolled

        INPUTS:
        None

        OUTPUTS:
        combo_count_df  pd.DataFrame
        """
        value_counts = self.game.show().apply(lambda x: tuple(sorted(x.values)), axis = 1).value_counts()
        df = value_counts.to_frame()
        df.columns = ['n']
        df.index = pd.MultiIndex.from_tuples(df.index)
        return df
    def permutation_count(self) -> pd.DataFrame:
        """
        PURPOSE: Returns a DataFrame with the counts of each permutation of faces rolled

        INPUTS:
        None

        OUTPUTS:
        permutation_count_df  pd.DataFrame
        """
        value_counts = self.game.show().apply(lambda x: tuple(x.values), axis = 1).value_counts()
        df = value_counts.to_frame()
        df.columns = ['n']
        df.index = pd.MultiIndex.from_tuples(df.index)
        return df