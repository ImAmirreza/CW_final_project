from solvers.base import Solver
from utils import timer_decorator


class BFS_Solver(Solver):
    def __init__(self, maze_game):
        self.maze_game = maze_game

    def bfs(self):
        queue = [(self.maze_game.get_player_position(), [])]
        visited = set()

        while queue:
            (x, y), path = queue.pop(0)
            path = path + [(x, y)]

            if (x, y) == self.maze_game.get_exit_position():
                return path

            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if self.maze_game.is_valid_move(nx, ny) and (nx, ny) not in visited:
                    queue.append(((nx, ny), path))
                    visited.add((nx, ny))

        return None

    @timer_decorator
    def solve(self):
        return self.bfs()
