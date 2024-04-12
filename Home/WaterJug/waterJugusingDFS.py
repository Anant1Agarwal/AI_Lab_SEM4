def dfs(start,target,capacities,visited):
    if start==target:
        return [target]
    visited.append(start)
    for move in get_moves(start,capacities):
        if move not in visited:
            path=dfs(move,target,capacities,visited)
            if path:
                return [start]+path


def get_moves(state,capcities):
    moves=[]
    a_max,b_max=capacities
    a,b=state
    if a<a_max:
        moves.append((a_max,b))
    if b<b_max:
        moves.append((a,b_max))
    if a>0:
        moves.append((0,b))
    if b>0:
        moves.append((a,0))
    if a>0 and b<b_max:
        amount=min(a,b_max-b)
        moves.append((a-amount,b+amount))
    if b>0 and a<a_max:
        amount=min(b,a_max-a)
        moves.append((a+amount,b-amount))
    return moves

start=(0,0)
target = (2,0)
capacities=(4,3)
visited=[]

path=dfs(start,target,capacities,visited)

if path:
    print("Steps to reach the goal:")
    for p in path:
        print(p)
else:
    print("No solution")
