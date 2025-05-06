
from window import Window
from maze import Maze


def main():
    print("Initializing the Maze solver game....")
    num_rows = 16
    num_cols = 16
    margin = 50
    screen_x = 800
    screen_y = 800
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    print(f"""
Configuration : 
    - Screen resolution : {screen_x} x {screen_y}
    - Game matrix : {num_rows} x {num_cols}
    - Cell's width : {cell_size_x}
    - Cell's height : {cell_size_y}
""")
    win = Window(screen_x, screen_y)
    print("Game board created...")
    maze = Maze(margin, margin, num_rows, num_cols,
                cell_size_x, cell_size_y, win)
    print("Maze created...")
    print("resolving....")
    resolved = maze.solve()
    if resolved:
        print("The maze has been resolved!")
    else:
        print("The maze can't be resolve!")
    win.wait_for_close()


main()
