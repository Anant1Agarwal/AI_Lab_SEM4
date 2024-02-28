
class Graph:
    def __init__(self,No,arr):
        self.n=No
        self.adj_list={arr[i]:[] for i in range(self.n)}
        self.arr=arr

    def add_edge(self,src,des):
        self.adj_list[src].append(des)
        self.adj_list[src].sort()

        self.adj_list[des].append(src)
        self.adj_list[des].sort()

    def print_graph(self):
        for i in range(self.n):
            print(f"{self.arr[i]} is connected to ",end="")
            for des in self.adj_list[self.arr[i]]:
                print(f"->{des}",end=" ")
            print()
    
    def dfs(self,node,visited):
        if node not in visited:
            visited.append(node)
            print(node,end=" ")
            
            for k in self.adj_list[node]:
                if k not in visited:
                    self.dfs(k,visited)

def main():
    array=['A','B','C','D','E','F','G','H','S']
    g=Graph(9,array)
    g.add_edge('A','B')
    g.add_edge('A','S')
    g.add_edge('S','C')
    g.add_edge('C','D')
    g.add_edge('C','E')
    g.add_edge('H','E')
    g.add_edge('C','F')
    g.add_edge('G','F')
    g.add_edge('S','G')
    g.add_edge('G','H')

    
    g.print_graph()
    g.dfs('A',[])


if __name__=="__main__":
    main()


    
