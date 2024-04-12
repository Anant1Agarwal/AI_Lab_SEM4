from collections import deque
import heapq

# Function to find the index of the blank tile (0)
def find_blank(puzzle):
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] == 0:
                return i, j

# Function to generate possible moves for a given puzzle state
def generate_moves(puzzle):
    blank_row, blank_col = find_blank(puzzle)
    moves = []
    
    # Move up
    if blank_row > 0:
        new_puzzle = [row[:] for row in puzzle]
        new_puzzle[blank_row][blank_col], new_puzzle[blank_row - 1][blank_col] = \
            new_puzzle[blank_row - 1][blank_col], new_puzzle[blank_row][blank_col]
        moves.append(new_puzzle)
    
    # Move down
    if blank_row < 2:
        new_puzzle = [row[:] for row in puzzle]
        new_puzzle[blank_row][blank_col], new_puzzle[blank_row + 1][blank_col] = \
            new_puzzle[blank_row + 1][blank_col], new_puzzle[blank_row][blank_col]
        moves.append(new_puzzle)
    
    # Move left
    if blank_col > 0:
        new_puzzle = [row[:] for row in puzzle]
        new_puzzle[blank_row][blank_col], new_puzzle[blank_row][blank_col - 1] = \
            new_puzzle[blank_row][blank_col - 1], new_puzzle[blank_row][blank_col]
        moves.append(new_puzzle)
    
    # Move right
    if blank_col < 2:
        new_puzzle = [row[:] for row in puzzle]
        new_puzzle[blank_row][blank_col], new_puzzle[blank_row][blank_col + 1] = \
            new_puzzle[blank_row][blank_col + 1], new_puzzle[blank_row][blank_col]
        moves.append(new_puzzle)
    
    return moves

# Function to check if the puzzle is solved
def is_goal(puzzle):
    return puzzle == [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

# # Breadth-First Search
# def bfs(initial_state):
#     queue = deque([(initial_state, [])])
#     visited = set()
    
#     while queue:
#         state, path = queue.popleft()
#         visited.add(tuple(map(tuple, state)))
        
#         if is_goal(state):
#             return path
        
#         for move in generate_moves(state):
#             if tuple(map(tuple, move)) not in visited:
#                 queue.append((move, path + [move]))

#     return None
def bfs(initial_state):
    que=[]
    que.append((initial_state,[]))
    visited = []
    
    while que:
        state, path = que.pop(0)
        visited.append(state)
        
        if is_goal(state):
            return path
        
        for move in generate_moves(state):
            if move not in visited:
                que.append((move, path + [move]))

    return None


# Depth-First Search
def dfs(initial_state):
    stack = [(initial_state, [])]
    visited = set()
    
    while stack:
        state, path = stack.pop()
        visited.add(tuple(map(tuple, state)))
        
        if is_goal(state):
            return path
        
        for move in reversed(generate_moves(state)):
            if tuple(map(tuple, move)) not in visited:
                stack.append((move, path + [move]))

    return None

# A* Search (Manhattan Distance Heuristic)
def heuristic(state):
    h = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                goal_row = state[i][j] // 3
                goal_col = state[i][j] % 3
                h += abs(i - goal_row) + abs(j - goal_col)
    return h

def astar(initial_state):
    heap = [(heuristic(initial_state), 0, initial_state, [])]
    visited = set()
    
    while heap:
        _, cost, state, path = heapq.heappop(heap)
        visited.add(tuple(map(tuple, state)))
        
        if is_goal(state):
            return path
        
        for move in generate_moves(state):
            if tuple(map(tuple, move)) not in visited:
                new_cost = cost + 1
                heapq.heappush(heap, (new_cost + heuristic(move), new_cost, move, path + [move]))

    return None

# Test the program
initial_state = [[1, 2, 0], [3, 4, 5], [6, 7, 8]]

print("BFS:", bfs(initial_state))
print("A*:", astar(initial_state))

print("DFS:", dfs(initial_state))
