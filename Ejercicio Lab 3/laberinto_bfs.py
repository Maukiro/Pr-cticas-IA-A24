from collections import deque

def solve_maze(maze, start, end):
    queue = deque([(start, [start])])
    while queue:
        (x, y), path = queue.popleft()

        if (x, y) == end:
            return True, path

        # Mark as visited
        maze[x][y] = '2'

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]):
                if maze[nx][ny] == '0' or maze[nx][ny] == 'E':
                    queue.append(((nx, ny), path + [(nx, ny)]))
                    if maze[nx][ny] != 'E':
                        maze[nx][ny] = '2'

    return False, []

if __name__ == "__main__":
    # 0 = open path, 1 = wall, S = start, E = end
    maze = [['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '1', '1', '1', '1', '1', '1', '1', '1', '0'],
            ['0', '1', '0', 'S', '0', '0', '0', '0', '1', '0'],
            ['0', '1', '0', '0', '0', '1', '1', '1', '1', '0'],
            ['0', '1', '1', '0', '0', '1', '0', '0', '1', '0'],
            ['0', '1', '0', '0', '0', '0', '0', '0', '1', '0'],
            ['0', '1', '1', '0', '0', '1', '1', '0', '0', '0'],
            ['0', '1', '0', '0', '0', '1', '0', '0', '1', '0'],
            ['0', '1', '0', '0', '1', '1', '0', '1', '1', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0', '0', 'E']
            ]
    start = (2, 3)
    end = (9, 9)
    
    solved, path = solve_maze(maze, start, end)

    if solved:
        print("Maze Solved!")
        for x, y in path:
            if maze[x][y] != 'S' and maze[x][y] != 'E':
                maze[x][y] = '*'
        for row in maze:
            print("".join(row))
    else:
        print("No solution found.")












