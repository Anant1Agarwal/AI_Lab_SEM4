graph = {
    1: [2,6],
    2: [3,1],
    3: [2,8],
    4: [5],
    5: [4,10],
    6: [1,11],
    7: [8],
    8: [3,7],
    9: [10,14],
    10: [5,9,15],
    11: [6,12],
    12: [11,17],
    13: [14],
    14: [9,13,19],
    15: [10,20],
    16: [17],
    17: [16,18],
    18: [17,19],
    19: [14,18],
    20: [15]
}

visited = [False]*20
def dfs(visited,graph,node):
    if(node==20):
        print(20)
        exit(0)
    if(visited[node]==False):graph = {
    1: [2,6],
    2: [3,1],
    3: [2,8],
    4: [5],
    5: [4,10],
    6: [1,11],
    7: [8],
    8: [3,7],
    9: [10,14],
    10: [5,9,15],
    11: [6,12],
    12: [11,17],
    13: [14],
    14: [9,13,19],
    15: [10,20],
    16: [17],
    17: [16,18],
    18: [17,19],
    19: [14,18],
    20: [15]
}

visited = [False]*20
def dfs(visited,graph,node):
    if(node==20):
        print(20)
        exit(0)
    if(visited[node]==False):
        print(node,end = " ")
        visited[node]=True
        for i in graph[node]:
            dfs(visited,graph,i)
            
def main():
    dfs(visited,graph,2)

if __name__ == "__main__":
    main()