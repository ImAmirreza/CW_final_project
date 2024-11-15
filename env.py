import random
class MazeGame:
    PLAYER = 'P'
    EXIT = 'E'
    EMPTY = '.'
    WALL = "X"
    def __init__(self, maze=None, width=10, height=5):
        if maze is None:
            print("Generating maze...")
            self.maze = self.generate_maze(width, height)
        else:
            self.maze = maze
        self.player_position = self.find_player_position()
        self.exit_position = self.find_exit_position()
    def generate_maze(self, width, height):
        maze = [[self.EMPTY for _ in range(width)] for _ in range(height)]
        for i in range(height):
            for j in range(width):
                if random.random() < 0.2:
                    maze[i][j] = self.WALL
        # Place 'P' at a random position
        while True:
            x = random.randint(0, height - 1)
            y = random.randint(0, width - 1)
            if maze[x][y] == self.EMPTY:
                maze[x][y] = self.PLAYER
                player_position = (x, y)
                break
        # Place 'E' at a random position that is not too close to 'P'
        while True:
            x = random.randint(0, height - 1)
            y = random.randint(0, width - 1)
            if maze[x][y] == self.EMPTY and abs(x - player_position[0]) + abs(y - player_position[1]) > 5:
                maze[x][y] = self.EXIT
                break
        return maze


    def find_player_position(self):
        for i in range(len(self.maze)):
            for j in range(len(self.maze[i])):
                if self.maze[i][j] == self.PLAYER:
                    return (i, j)

    def find_exit_position(self):
        for i in range(len(self.maze)):
            for j in range(len(self.maze[i])):
                if self.maze[i][j] == self.EXIT:
                    return (i, j)

    def is_valid_move(self, x, y):
        if x < 0 or y < 0 or x >= len(self.maze) or y >= len(self.maze[0]):
            return False
        if self.maze[x][y] == self.WALL:
            return False
        return True

    def get_maze(self):
        return self.maze

    def get_player_position(self):
        return self.player_position

    def get_exit_position(self):
        return self.find_exit_position()








