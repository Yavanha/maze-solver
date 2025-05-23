import unittest

from maze import Maze
from window import Window


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, None)
        self.assertEqual(
            len(m1._cells),
            num_rows,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_cols,
        )

    def test_break_entrance_and_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(50, 50, num_rows, num_cols, 10, 10, None)
        self.assertFalse(
            m1._cells[0][0].has_top_wall
        )
        self.assertFalse(
            m1._cells[num_rows -
                      1][num_cols - 1].has_bottom_wall
        )


if __name__ == "__main__":
    unittest.main()
