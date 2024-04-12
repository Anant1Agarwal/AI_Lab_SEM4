# Water Jug Problem using BFS
from collections import deque

# Function to find all possible states from the current state
def get_moves(state, capacities):
    moves = []
    a_max, b_max = capacities
    a, b = state
    # Fill jug A
    if a < a_max:
        moves.append((a_max, b))
    # Fill jug B
    if b < b_max:
        moves.append((a, b_max))
    # Empty jug A
    if a > 0:
        moves.append((0, b))
    # Empty jug B
    if b > 0:
        moves.append((a, 0))
    # Pour from A to B
    if a > 0 and b < b_max:
        amount = min(a, b_max - b)
        moves.append((a - amount, b + amount))
    # Pour from B to A
    if b > 0 and a < a_max:
        amount = min(b, a_max - a)
        moves.append((a + amount, b - amount))

    return moves

# Function to solve the water jug problem using BFS
def bfs(start, target, capacities, visited):
    queue = deque([(start, None)])  # (current_state, parent_state)

    while queue:
        current_state, parent_state = queue.popleft()

        if current_state == target:
            path = [current_state]
            while parent_state is not None:
                path.append(parent_state[0])
                parent_state = parent_state[1]
            path.reverse()
            return path

        next_moves = get_moves(current_state, capacities)
        for next_move in next_moves:
            if next_move not in visited:
                visited.append(next_move)
                queue.append((next_move, (current_state, parent_state)))

    return None  # Goal state is not reachable


start=(0,0)
target = (2,0)
capacities=(4,3)
visited=[]
path=bfs(start,target, capacities, visited)

if path:
    print("Steps to reach the goal:")
    for p in path:
        print(p)
else:
    print("No solution")

    
