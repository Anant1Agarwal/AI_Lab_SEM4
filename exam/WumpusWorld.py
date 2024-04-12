
from collections import deque


def is_valid_position(position):
    x, y = position
    return 0 <= x < size and 0 <= y < size

def is_safe_position( position):
    x, y = position
    return position not in pits and position != wumpus

def get_adjacent_positions( position):
    x, y = position
    adjacent_positions = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
    return [pos for pos in adjacent_positions if is_valid_position(pos)]

def bfs(start):
    visited = []
    queue = [(start, [])]

    while queue:
        position, path = queue.pop(0)
        if position == gold:
            return path + [position]
        
        if position not in visited:
            visited.append(position)
            for adj_position in get_adjacent_positions(position):
                if is_safe_position(adj_position):
                    queue.append((adj_position, path + [position]))
    return None


size = 4
pits = [(1, 1), (2, 2), (3, 3)]
wumpus = (2, 1)
gold = (3, 0)

start_position = (0, 0)
path =bfs(start_position)

if path:
    print("Path found:")
    for i, position in enumerate(path):
        print(f"Step {i+1}: {position}")
else:
    print("No path found.")


