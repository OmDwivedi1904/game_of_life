# Conway's Game of Life with FPS and Population Graph

This is an implementation of Conway's Game of Life, a cellular automaton devised by mathematician John Conway. The game simulates the evolution of cells on a grid based on simple rules that govern their birth, survival, and death. The project includes a graphical interface using Pygame and a real-time plot showing FPS and the current population using Matplotlib.

## Features

- **Interactive Grid**: The grid allows you to interact with it by adding and removing cells. Cells can be toggled between live and dead states.
- **FPS and Population Graph**: Real-time graphs that show the FPS (frames per second) and the population of live cells.
- **Basic Controls**:
  - **Space**: Start or pause the simulation.
  - **N**: Advance the simulation by one step.
  - **R**: Randomly populate the grid with live cells.
  - **S**: Save the current pattern of live cells to a file.
  - **L**: Load a saved pattern from a file.
- **File I/O**: Supports saving and loading patterns in a file for persistence.

## Requirements

- Python 3.x
- Pygame
- Matplotlib

You can install the required libraries using `pip`:

bash

pip install pygame matplotlib -- example






## How to Run the Game
Clone this repository to your local machine:


git clone https://github.com/yourusername/game-of-life.git
cd game-of-life
Run the script:


python life.py --width 40 --height 20 --fps 6
You can customize the game with these command-line arguments:

- width (default: 40): The number of columns in the grid.

- height (default: 20): The number of rows in the grid.

- fps (default: 6): The frames per second for the simulation.

## Rules of Life

Each cell in the grid has 8 neighbors and follows these rules every generation:

- Fewer than 2 live neighbors → Dies (under-population)
- 2 or 3 live neighbors → Lives on
- More than 3 live neighbors → Dies (over-population)
- Exactly 3 live neighbors (if currently dead) → Becomes alive (reproduction)

## Graphs

Two real-time graphs appear in the bottom-right corner of the screen:

- **FPS**: Frames per second – shows how fast the simulation is running.
- **Population**: The number of currently alive cells in the grid.

These graphs update as the game progresses.

## Save and Load Patterns

Use these keys to manage patterns:

- Press `S` to save the current pattern to `patterns.txt`.
- Press `L` to load the saved pattern from `patterns.txt`.
- Patterns are saved as coordinates of all currently live cells.


