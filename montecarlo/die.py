import numpy as np
import pandas as pd
from typing import Union, List
class Die:
    """Die class, used to represent a series of states (faces) with weighted probablities, which can be sampled from through rolling"""
    def __init__(self, faces : np.ndarray) -> None:
        """
        PURPOSE: Initializes a die with given faces and equal weights
        
        INPUTS:
        faces  np.ndarray of either int or string dtype

        OUTPUT:
        None
        """
        if not (isinstance(faces, np.ndarray) and (faces.dtype == np.int64 or faces.dtype == np.int32 or np.issubdtype(faces.dtype, np.str_))):
            raise TypeError("faces must be of type np.ndarray, either int or string")
        if len(set(faces)) != len(faces):
            raise ValueError("faces must be unique")
        self._data = pd.DataFrame({"weights": np.ones(len(faces), dtype=float)}, index=faces)
    def change_weight(self, face : Union[int, str], weight : Union[int, float]) -> None:
        """
        PURPOSE: Changes the weight of a given face of the die
        
        INPUTS:
        face    int or str
        weight  int or float

        OUTPUT
        None
        """
        if not (isinstance(weight, int) or isinstance(weight, float)):
            raise TypeError("invalid weight type, must be int or float")
        if face not in self._data.index:
            raise IndexError("face not found in die")
        if weight < 0:
            raise ValueError("weight must not be negative")
        self._data.loc[self._data.index == face,"weights"] = weight
    def roll(self, n : int = 1) -> List[int]:
        """
        PURPOSE: Rolls the die n times and returns the results

        INPUTS:
        n  int, greater than 0

        OUTPUT:
        rolls  list of int
        """
        if not isinstance(n, int):
            raise TypeError("n must be an int")
        if n <= 0:
            raise ValueError("n must be greater than 0")
        dtype = self._data.index.dtype
        transform = (lambda x: x.item()) if dtype == np.int64 or dtype == np.int32 else (lambda x: x)
        return list(map(transform, np.random.choice(self._data.index, n, p=self._data.weights / self._data.weights.sum())))
    def show(self) -> pd.DataFrame:
        """
        PURPOSE: Returns a copy of the die's private data, including faces and weights

        INPUTS:
        None

        OUTPUT:
        data  pd.DataFrame
        """
        return self._data.copy()