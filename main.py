from utils import print_maze
from env import MazeGame
from solvers import __all__


maze_game = MazeGame()

print("Original Maze:")
for row in maze_game.get_maze():
    print(" ".join(row))


for solver in __all__:
    solver_instance = solver(maze_game)
    path = solver_instance.solve()
    name = str(solver.__name__).split("_")[0]
    if path:
        print(f"\n{name} Solution:")
        print_maze(maze_game.get_maze(), path)
    else:
        print(f"\nNo {name} solution found")

    # Additional functionalities
    print(f"\n{name} Statistics:")
    print(f"Path length: {len(path)}")
    print(f"Time taken: {solver_instance.time_taken * 1000:.5f} ms")
    print("-" * 50)
