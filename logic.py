# logic.py
from collections import Counter

def get_neighbors(x, y):
    return {(x+dx, y+dy) for dx in [-1, 0, 1]
                              for dy in [-1, 0, 1]
                              if not (dx == 0 and dy == 0)}

def next_gen(live_cells):
    neighbor_counts = Counter()
    for cell in live_cells:
        for neighbor in get_neighbors(*cell):
            neighbor_counts[neighbor] += 1

    return {
        cell for cell, count in neighbor_counts.items()
        if count == 3 or (count == 2 and cell in live_cells)
    }

