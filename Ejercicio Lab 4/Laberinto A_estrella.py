import heapq

class Node:
    def __init__(self, row, col, parent=None):
        self.row = row
        self.col = col
        self.parent = parent
        self.g = 0  # Costo real desde el nodo inicial hasta este nodo
        self.h = 0  # Heurística: Estimación del costo desde este nodo hasta el nodo objetivo
        self.f = 0  # f = g + h
    
    def __lt__(self, other):
        return self.f < other.f
    
    def __eq__(self, other):
        return self.row == other.row and self.col == other.col

def heuristic(node, goal):
    return abs(node.row - goal[0]) + abs(node.col - goal[1])

def A_star(maze, start, end):
    open_list = []
    closed_list = set()
    
    start_node = Node(start[0], start[1])
    goal_node = Node(end[0], end[1])
    
    heapq.heappush(open_list, start_node)
    
    while open_list:
        current_node = heapq.heappop(open_list)
        
        if (current_node.row, current_node.col) == end:
            path = []
            while current_node:
                path.append((current_node.row, current_node.col))
                current_node = current_node.parent
            return True, path[::-1]
        
        closed_list.add((current_node.row, current_node.col))
        
        for d_row, d_col in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_row, new_col = current_node.row + d_row, current_node.col + d_col
            
            if 0 <= new_row < len(maze) and 0 <= new_col < len(maze[0]) and maze[new_row][new_col] != '1' and (new_row, new_col) not in closed_list:
                neighbor = Node(new_row, new_col, current_node)
                neighbor.g = current_node.g + 1
                neighbor.h = heuristic(neighbor, end)
                neighbor.f = neighbor.g + neighbor.h
                
                heapq.heappush(open_list, neighbor)
    
    return False, []

if __name__ == "__main__":
    # 0 = open path, 1 = wall, S = start, E = end
    maze = [
    ['S', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
    ['0', '0', '1', '0', '0', '0', '1', '0', '0', '0', '0', '0', '1', '0', '1', '0', '1', '0', '0', '1'],
    ['1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '1', '0', '1'],
    ['1', '0', '0', '0', '1', '0', '0', '0', '1', '0', '1', '0', '0', '0', '1', '0', '0', '0', '0', '1'],
    ['1', '1', '1', '0', '1', '0', '1', '0', '1', '0', '1', '1', '1', '1', '1', '1', '1', '1', '0', '1'],
    ['1', '0', '0', '0', '1', '0', '1', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '1'],
    ['1', '1', '1', '0', '1', '0', '1', '1', '1', '1', '1', '1', '1', '0', '1', '1', '1', '1', '1', '1'],
    ['1', '0', '0', '0', '1', '0', '1', '0', '1', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '1'],
    ['1', '0', '1', '1', '1', '0', '1', '0', '1', '0', '1', '1', '1', '0', '1', '0', '1', '1', '0', '1'],
    ['1', '0', '0', '1', '0', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '0', '0', '0', '1'],
    ['1', '0', '1', '1', '1', '0', '1', '0', '1', '1', '1', '0', '1', '0', '1', '1', '1', '1', '1', '1'],
    ['1', '0', '0', '0', '0', '0', '1', '0', '1', '0', '0', '0', '1', '0', '1', '0', '0', '0', '0', '1'],
    ['1', '1', '1', '0', '1', '1', '1', '0', '1', '1', '1', '0', '1', '0', '1', '1', '1', '1', '1', '1'],
    ['1', '0', '0', '0', '0', '0', '1', '0', '0', '0', '1', '0', '0', '0', '0', '0', '1', '0', '0', '1'],
    ['1', '0', '1', '0', '1', '0', '1', '0', '1', '1', '1', '1', '1', '1', '1', '0', '1', '1', '0', '1'],
    ['1', '0', '1', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'],
    ['1', '0', '1', '0', '1', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '1'],
    ['1', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', 'E']
]

    start = (0, 0)
    end = (19, 19)

    solved, path = A_star(maze, start, end)

    if solved:
        print("Maze Solved!")
        for x, y in path:
            if maze[x][y] != 'S' and maze[x][y] != 'E':
                maze[x][y] = '*'
        for row in maze:
            print("".join(row))
    else:
        print("No solution found.")
