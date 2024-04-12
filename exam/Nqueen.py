import random
def generate_random_state():
    return [random.randint(0,4) for _ in range(5)]

def calculate_conflicts(state):
    conflicts=0
    for i in range(5):
        for j in range(i+1,5):
            if state[i]==state[j] or abs(i-j)==abs(state[i]-state[j]):
                conflicts+=1

    return conflicts

def is_solution(state):
    return calculate_conflicts(state)==0

def find_neighbours(state):
    neighbours=[]
    for i in range(5):
        for j in range(5):
            if j!=state[i]:
                neighbor=state[:i]+[j]+state[i+1:]
                neighbours.append(neighbor)
    return neighbours

def BFS_queens():
    start=generate_random_state()
    que=[start]
    visited=[]
    visited.append(que)
    while que:
        cur_state=que.pop()
        if is_solution(cur_state):
                return cur_state
            
        neighbours=find_neighbours(cur_state)

        for neighbour in neighbours:
            if neighbour not in visited:
                que.append(neighbour)
                visited.append(neighbour)

def DFS_queens(state,visited):
    if is_solution(state):
        return state
    
    visited.append(state)
    neighbours =find_neighbours(state)
    for neighbor in neighbours:
        if neighbor not in visited:
            sol=DFS_queens(neighbor, visited)
            if sol:
                return sol
    
    
   
    



result=BFS_queens()
print(f"SOlution found: {result}")

start2=generate_random_state()
visited=[]
result2=DFS_queens(start2,visited)
print(f"Solution from DFS is {result2}")