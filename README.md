# METADATA

Author: Varun Bhatnagar
Project Name: Monte Carlo Simulator for DS5100

# Synopsis

This project is a monte carlo simulator. It implements a 3 classes, Die, Game, and Analyzer. The Die class simulates sampling from a discrete distribution given adjustble weights. The Game class simulates a sampling from multiple dice, and the Analyzer class implements getting empirical probailities from the simulation, including jackpots, combinations, and permutations.

We can create a die in the following way:

```python
from montecarlo.die import Die
import numpy as np

faces = np.asarray(['Heads', 'Tails'])
die = Die(faces)
die.change_weights('Heads', 10)
print(die.roll(10))
```

We can create a game in the following way:

```python
from montecarlo.game import Game
import numpy as np
from montecarlo.die import Die

faces = np.asarray(['Heads', 'Tails'])
die = Die(faces)
game = Game([die for i in range(10)])
game.play(1000)
game.show(wide = True)
game.show(wide = False)
```

We can create an analyzer in the following way:

```python
from montecarlo.analyzer import Analyzer
import numpy as np
from montecarlo.die import Die
from montecarlo.game import Game

faces = np.asarray(['Heads', 'Tails'])
die = Die(faces)
game = Game([die for i in range(10)])
game.play(1000)
analyzer = Analyzer(game)
analyzer.jackpot()
analyzer.face_count()
analyzer.combo_count()
analyzer.permutation_count()
```

# API Description

## Die Class

Die class, used to represent a series of states (faces) with weighted probablities, which can be sampled from through rolling

```python
def __init__(self, faces : np.ndarray) -> None:
        """
        PURPOSE: Initializes a die with given faces and equal weights
        
        INPUTS:
        faces  np.ndarray of either int or string dtype

        OUTPUT:
        None
        """
```

```python
def change_weight(self, face : Union[int, str], weight : Union[int, float]) -> None:
        """
        PURPOSE: Changes the weight of a given face of the die
        
        INPUTS:
        face    int or str
        weight  int or float

        OUTPUT
        None
        """
```

```python
def roll(self, n : int = 1) -> List[int]:
        """
        PURPOSE: Rolls the die n times and returns the results

        INPUTS:
        n  int, greater than 0

        OUTPUT:
        rolls  list of int
        """
```

```python
def show(self) -> pd.DataFrame:
        """
        PURPOSE: Returns a copy of the die's private data, including faces and weights

        INPUTS:
        None

        OUTPUT:
        data  pd.DataFrame
        """
```

## Game Class

Game class, used to represent the results of rolling dice with the same faces, but not necessarily the same weights, some number of times

```python
def __init__(self, dice : List[Die]):
        """
        PURPOSE: Initializes a game with a list of dice

        INPUTS:
        dice  list of Die objects

        OUTPUT:
        None
        """
```

```python
def play(self, n : int) -> None:
        """
        PURPOSE: Rolls each individual die in the game n times and stores the results in an internal DataFrame

        INPUTS:
        n  int, greater than 0

        OUTPUT:
        None
        """
```

```python
def show(self, wide : bool = True) -> pd.DataFrame:
        """
        PURPOSE: Returns the results of the game in a DataFrame, either in wide or narrow format.

        INPUTS:
        wide  bool, default True

        OUTPUTS:
        df  pd.DataFrame
        """
```

## Analyzer Class

Analyzer class, used to analyze the results of a game, including the number of jackpots, the counts of each face, the counts of each combination of faces, and the counts of each permutation of faces

```python
def __init__(self, game : Game) -> None:
        """
        PURPOSE: Initializes an Analyzer object with a Game object

        INPUTS:
        game  Game object

        OUTPUT:
        None
        """
```

```python
def jackpot(self) -> int:
        """
        PURPOSE: Returns the number of times all dice show the same face

        INPUTS:
        None

        OUTPUTS:
        int  number of jackpots
        """
```

```python
def face_count(self) -> pd.DataFrame:
        """
        PURPOSE: Returns a DataFrame with the counts of each face for each die

        INPUTS:
        None

        OUTPUTS:
        face_count_df  pd.DataFrame
        """
```

```python
def combo_count(self) -> pd.DataFrame:
        """
        PURPOSE: Returns a DataFrame with the counts of each combination of faces rolled

        INPUTS:
        None

        OUTPUTS:
        combo_count_df  pd.DataFrame
        """
```

```python
def permutation_count(self) -> pd.DataFrame:
        """
        PURPOSE: Returns a DataFrame with the counts of each permutation of faces rolled

        INPUTS:
        None

        OUTPUTS:
        permutation_count_df  pd.DataFrame
        """
```