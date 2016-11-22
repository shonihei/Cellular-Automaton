# Cellular Automaton

Cellular Automaton is a system similar to Conway's game of life. Unlike Conway's game of life however, each row represents "passing of time" or new generation. More information here: http://mathworld.wolfram.com/CellularAutomaton.html

In this implementation of cellular Automaton, rather than using simply two colors to represent on and off state, I used a series of closely related colors to represent the two states to create a more aesthetically pleasing.

# Sample Code
```python
cellDimension = 20 # in pixel
numColumn = 15     # in number of cells
numRow = 15        # in number of cells
rule = 73
activeColor = ["#000000"]
inactiveColor = ["#FFFFFF"]
automaton = CellularAutomaton(cellDimension, numColumn, numRow, rule, activeColor, inactiveColor)
automaton.make()
automaton.save("filenamehere")
```

# Sample Images
#### Example with two colors (What an elementary cellular automaton looks like)
![screenshot](https://github.com/shonihei/Cellular-Automaton/blob/master/sampleimages/bw.jpg)
#### Example with multiple colors
![screenshot](https://github.com/shonihei/Cellular-Automaton/blob/master/sampleimages/73Enlarged.jpg)

Both of these images are scalable by just changing the input
