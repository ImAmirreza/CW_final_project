import time
from functools import wraps


def print_maze(maze, path):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if (
                (i, j) in path
                and path.index((i, j)) != 0
                and path.index((i, j)) != len(path) - 1
            ):
                print(path.index((i, j)) + 1, end=" ")
            else:
                print(maze[i][j], end=" ")
        print()


def timer_decorator(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        start_time = time.time()
        result = func(self, *args, **kwargs)
        end_time = time.time()
        self.time_taken = end_time - start_time
        return result

    return wrapper
