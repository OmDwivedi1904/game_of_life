#Conway's Game of Life with FPS and Population Graph
This is an implementation of Conway's Game of Life, a cellular automaton devised by mathematician John Conway. The game simulates the evolution of cells on a grid based on simple rules that govern their birth, survival, and death. The project includes a graphical interface using Pygame and a real-time plot showing FPS and the current population using Matplotlib.

##Features
Interactive Grid: The grid allows you to interact with it by adding and removing cells. Cells can be toggled between live and dead states.

FPS and Population Graph: Real-time graphs that show the FPS (frames per second) and the population of live cells.

Basic Controls:

Space: Start or pause the simulation.

N: Advance the simulation by one step.

R: Randomly populate the grid with live cells.

S: Save the current pattern of live cells to a file.

L: Load a saved pattern from a file.

File I/O: Supports saving and loading patterns in a file for persistence.

Requirements
Python 3.x

Pygame

Matplotlib

You can install the required libraries using pip:

pip install pygame matplotlib
How to Run the Game
Clone this repository to your local machine:


git clone https://github.com/yourusername/game-of-life.git
cd game-of-life
Run the life.py script:


python life.py --width 40 --height 20 --fps 6
You can adjust the width, height, and fps using the command-line arguments.

--width (default 40): The width of the grid.

--height (default 20): The height of the grid.

--fps (default 6): The frames per second of the simulation.

How the Game Works
Each cell in the grid can be in one of two states:

Alive (green cell)

Dead (black cell)

Rules for the Next Generation:
A cell with fewer than 2 live neighbors dies (under-population).

A cell with 2 or 3 live neighbors stays alive.

A cell with more than 3 live neighbors dies (over-population).

A dead cell with exactly 3 live neighbors becomes alive.

The simulation is updated in real-time, with a graphical display of the grid and two graphs: FPS and Population.

Graphs
The simulation also includes two graphs displayed in the bottom-right corner:

FPS (Frames per second): The number of frames the game can process per second.

Population: The number of live cells in the grid at any given time.

These graphs are updated in real-time as the simulation runs.

Example Screenshots
Game in Action

FPS and Population Graph

Save and Load Patterns
You can save and load patterns using the following keys:

S: Save the current pattern to a file named patterns.txt.

L: Load a previously saved pattern from patterns.txt.

Patterns are saved as a list of coordinates where live cells are located.



