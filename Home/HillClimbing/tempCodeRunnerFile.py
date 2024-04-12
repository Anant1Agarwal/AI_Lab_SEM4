
import random

# Function to generate a random state for the 8-Queen problem
def generate_random_state():
    return [random.randint(0, 7) for _ in range(8)]

# Function to calculate the number of conflicts in a state
def calculate_conflicts(state):
    conflicts = 0
    for i in range(len(state)):
        for j in range(i + 1, len(state)):
            if state[i] == state[j] or abs(i - j) == abs(state[i] - state[j]):
                conflicts += 1
    return conflicts

# Function to find the best neighbor state
def find_best_neighbor(current_state):
    best_state = current_state[:]
    best_conflicts = calculate_conflicts(current_state)
    for i in range(len(current_state)):
        for j in range(8):
            if j != current_state[i]:
                new_state = current_state[:i] + [j] + current_state[i+1:]
                conflicts = calculate_conflicts(new_state)
                if conflicts < best_conflicts:
                    best_state = new_state
                    best_conflicts = conflicts
    return best_state

# Function to solve the 8-Queen problem using hill climbing
def hill_climbing_search():
    current_state = generate_random_state()
    current_conflicts = calculate_conflicts(current_state)
    while current_conflicts > 0:
        next_state = find_best_neighbor(current_state)
        next_conflicts = calculate_conflicts(next_state)
        if next_conflicts >= current_conflicts:
            break
        current_state = next_state
        current_conflicts = next_conflicts
    return current_state

# Function to check if a state is a solution (no conflicts)
def is_solution(state):
    return calculate_conflicts(state) == 0

# Main function to execute the program
if __name__ == "__main__":
    solution = hill_climbing_search()
    while not is_solution(solution):
        solution = hill_climbing_search()
    print("Solution found:",solution)
   
