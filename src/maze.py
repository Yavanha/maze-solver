from cell import Cell
from time import sleep
import random


class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win, seed=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = []
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells__visited()
        if seed is not None:
            random.seed(seed)

    def _create_cells(self):
        for i in range(self.num_rows):
            col_cells = []
            for j in range(self.num_cols):
                col_cells.append(Cell(self.win))
            self._cells.append(col_cells)
        if self.win is None:
            return
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        cell_x1 = self.x1 + self.cell_size_x * j
        cell_y1 = self.y1 + self.cell_size_y * i
        cell_x2 = cell_x1 + self.cell_size_x
        cell_y2 = cell_y1 + self.cell_size_y
        self._cells[i][j].draw(cell_x1, cell_y1, cell_x2, cell_y2)
        self._animate()

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self.num_rows - 1][self.num_cols -
                                       1].has_bottom_wall = False
        self._draw_cell(self.num_rows - 1, self.num_cols - 1)

    def _break_walls_r(self, i, j):
        current_cell = self._cells[i][j]
        current_cell.visited = True
        while True:
            to_visit = []

            # left i - 1 / j
            if j > 0 and not self._cells[i][j - 1].visited:
                to_visit.append((i, j - 1))
            # right i + 1 / j
            if j < self.num_cols - 1 and not self._cells[i][j + 1].visited:
                to_visit.append((i, j + 1))
            # top i / j - 1
            if i > 0 and not self._cells[i - 1][j].visited:
                to_visit.append((i - 1, j))
            # bot i / j + 1
            if i < self.num_rows - 1 and not self._cells[i + 1][j].visited:
                to_visit.append((i + 1, j))

            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return
            row, col = to_visit[random.randrange(len(to_visit))]

            # left
            if col == j - 1:
                current_cell.has_left_wall = False
                self._cells[row][col].has_right_wall = False
            # right
            if col == j + 1:
                current_cell.has_right_wall = False
                self._cells[row][col].has_left_wall = False

            # top
            if row == i - 1:
                current_cell.has_top_wall = False
                self._cells[row][col].has_bottom_wall = False

            # bottom
            if row == i + 1:
                current_cell.has_bottom_wall = False
                self._cells[row][col].has_top_wall = False

            self._break_walls_r(row, col)

    def _reset_cells__visited(self):
        for row in self._cells:
            for cell in row:
                cell.visited = False

    def solve(self):
        self._solve_r(0, 0)

    def _solve_r(self, i, j):
        self._animate()
        print(i, j)
        current_cell = self._cells[i][j]
        current_cell.visited = True

        if i == self.num_rows - 1 and j == self.num_cols - 1:
            return True

        directions = []
        if j > 0:
            directions.append((i, j - 1))
        if j < self.num_cols - 1:
            directions.append((i, j + 1))

        if i > 0:
            directions.append((i - 1, j))
        if i < self.num_rows - 1:
            directions.append((i + 1, j))
        for row, col in directions:
            if not self._cells[row][col].visited and (col == j - 1 and not current_cell.has_left_wall and not self._cells[row][col].has_right_wall
                                                      or col == j + 1 and not current_cell.has_right_wall and not self._cells[row][col].has_left_wall
                                                      or row == i - 1 and not current_cell.has_top_wall and not self._cells[row][col].has_bottom_wall
                                                      or row == i + 1 and not current_cell.has_bottom_wall and not self._cells[row][col].has_top_wall):
                current_cell.draw_move(self._cells[row][col])
                if self._solve_r(row, col):
                    return True
                else:
                    current_cell.draw_move(self._cells[row][col], True)

        return False

    def _animate(self):
        if self.win is None:
            return
        self.win.redraw()
        sleep(0.05)
