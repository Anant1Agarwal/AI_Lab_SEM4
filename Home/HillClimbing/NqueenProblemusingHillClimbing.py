import random
def generate_random_state():
    return [random.randint(0,7) for _ in range(8)]

def calculate_conflicts(state):
    conflicts=0
    for i in range(len(state)):
        for j in range(i+1,len(state)):
            if state[i]==state[j] or abs(i-j)==abs(state[i]-state[j]):
                conflicts+=1
    
    return conflicts


def find_best_neighbor(current_state):
    best_state=current_state[:]
    best_conflicts=calculate_conflicts(current_state)

    for i in range(len(current_state)):
        for j in range(8):
            if j!=current_state[i]:
                current_state=current_state[:i]+[j]+current_state[i+1:]
                current_conflicts=calculate_conflicts(current_state)
                if current_conflicts<best_conflicts:
                    best_state=current_state
                    best_conflicts=current_conflicts
                
    return best_state


def hill_climbing_search():
    current_state=generate_random_state()
    current_conflicts=calculate_conflicts(current_state)
    while current_conflicts>0:
        next_state=find_best_neighbor(current_state)
        next_conflicts=calculate_conflicts(next_state)

        if next_conflicts>=current_conflicts:
            break

        current_state=next_state
        current_conflicts=next_conflicts
    return current_state

def is_solution(state):
    return calculate_conflicts(state) == 0

print("hel")
solution = hill_climbing_search()
while not is_solution(solution):
    print("current solution:",solution)
    solution = hill_climbing_search()
print("Solution found:",solution)

