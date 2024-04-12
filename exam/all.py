def add_edge(src,des,weight):
    adj_list[src].append([des,weight])
    adj_list[src].sort(key=lambda x:x[0])

    adj_list[des].append([src,weight])
    adj_list[des].sort(key=lambda x:x[0])
    

def print_graph():
    for i in range(n):
        print(f"{arr[i]} is connected to ",end=" ")
        for des,weight in adj_list[arr[i]]:
            print(f"{des} with weight {weight} ",end=" ")
        print()

def BFS(start):
    queue=[]
    queue.append(start)
    visited[start]=True
    while queue:
        vertex=queue.pop(0)
        print(vertex,end =" ")

        for neighbour,_ in adj_list[vertex]:
            if not visited[neighbour]:
                queue.append(neighbour)
                visited[neighbour]=True

def DFS(vertex):
    newvisited.append(vertex)
    print(vertex, end=" ")

    for neighbour,_ in adj_list[vertex]:
        if neighbour not in  newvisited:
            DFS(neighbour)

def UCS(start,goal):
    prqueue=[]
    path=[]
    path.append(start)
    prqueue.append([0,start,path])
    prqueue.sort(key=lambda x:x[0])

    while prqueue:
        cur_cost,cur_node,cur_path=prqueue.pop(0)
        if cur_node not in newvisited1:
            newvisited1.append(cur_node)

            if cur_node==goal:
                return cur_path,cur_cost
            
            for des,weight in adj_list[cur_node]:
                if des not in newvisited1:
                    new_path=cur_path+[des]
                    prqueue.append([cur_cost+weight, des, new_path])
                    prqueue.sort(key=lambda x:x[0])



n=9
arr=['A','B','C','D','E','F','G','H','S']
adj_list={arr[i]:[] for i in range(n)}
add_edge('A','B',1)
add_edge('A','S',2)
add_edge('S','C',3)
add_edge('S','G',64)
add_edge('G','F',62)
add_edge('C','F',23)
add_edge('C','E',12)
add_edge('C','D',93)
add_edge('E','H',45)
add_edge('G','H',24)
print_graph()

visited={arr[i]: False for i in range(n)}
print("BFS of Graph is: ",end=" ")
BFS('A')
print()

newvisited=[]
print("DFS of Graph is: ",end=" ")
DFS('A')
print()

newvisited1=[]
result=UCS('A','F')
path,cost=result
print(f"shortest path cost is {cost} and path is {path}")
