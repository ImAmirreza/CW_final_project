from solvers.base import Solver
from utils import timer_decorator
import math
import heapq


class AStar_Solver(Solver):
    def __init__(self, maze_game):
        self.maze_game = maze_game

    def heuristic(self, x, y):
        exit_x, exit_y = self.maze_game.get_exit_position()
        return math.sqrt((x - exit_x) ** 2 + (y - exit_y) ** 2)

    def astar(self):
        queue = []
        heapq.heappush(queue, (0, self.maze_game.get_player_position(), []))
        visited = set()

        while queue:
            cost, (x, y), path = heapq.heappop(queue)
            path = path + [(x, y)]

            if (x, y) == self.maze_game.get_exit_position():
                return path

            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if self.maze_game.is_valid_move(nx, ny) and (nx, ny) not in visited:
                    new_cost = cost + 1
                    priority = new_cost + self.heuristic(nx, ny)
                    heapq.heappush(queue, (priority, (nx, ny), path))
                    visited.add((nx, ny))
        return None

    @timer_decorator
    def solve(self):
        return self.astar()
