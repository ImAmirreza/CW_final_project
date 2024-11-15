from solvers.base import Solver
from utils import timer_decorator


class DFS_Solver(Solver):
    def __init__(self, maze_game):
        self.maze_game = maze_game
        self.visited = set()

    def dfs(self, x, y, path):
        self.visited.add((x, y))
        path.append((x, y))

        if (x, y) == self.maze_game.get_exit_position():
            return path

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if self.maze_game.is_valid_move(nx, ny) and (nx, ny) not in self.visited:
                result = self.dfs(nx, ny, path)
                if result:
                    return result

        path.pop()
        return None

    @timer_decorator
    def solve(self):
        return self.dfs(
            self.maze_game.get_player_position()[0],
            self.maze_game.get_player_position()[1],
            [],
        )
