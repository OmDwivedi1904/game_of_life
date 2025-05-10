import os
from life import next_gen, save_pattern, load_pattern

def test_next_gen_still_life():
    block = {(1, 1), (1, 2), (2, 1), (2, 2)}
    result = next_gen(block, 5, 5)
    assert result == block  # Still life should remain the same

def test_save_and_load_pattern(tmp_path):
    test_cells = {(1, 1), (2, 2)}
    filename = tmp_path / "test_pattern.txt"
    save_pattern(test_cells, filename)
    loaded = load_pattern(filename)
    assert test_cells == loaded