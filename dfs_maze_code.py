import random

def make_maze(width, height):
    grid = [['#'] * width for _ in range(height)]

    def dfs(x, y):
        grid[y][x] = ' '
        directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 < nx < width - 1 and 0 < ny < height - 1 and grid[ny][nx] == '#':
                grid[y + dy // 2][x + dx // 2] = ' '
                dfs(nx, ny)

    start_x, start_y = 1, 1
    dfs(start_x, start_y)
    grid[start_y][start_x] = 'S'

    for i in range(height - 1, 0, -1):
        if grid[i][width - 2] == ' ':
            grid[i][width - 1] = 'E'
            break

    return grid

def print_maze(maze):
    for row in maze:
        print(''.join(row))

if __name__ == "__main__":
    width, height = 21, 15
    maze = make_maze(width, height)
    print_maze(maze)
