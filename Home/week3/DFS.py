class Graph:
    def __init__(self,ver):
        self.nv=ver
        self.adj={}
        
        for i in range(self.nv):
            self.adj[i]=[]
        
    def add_edge(self,src,des):
        self.adj[src].append(des)
        self.adj[des].append(src)
    
    def print_graph(self):
        for item in range(self.nv):
            print(item,'->',self.adj[item])


    def DFSutil(self,u, visited):
        visited[u]=1
        print(u)

        # for i in range(len(self.adj[u])):
        #     if(visited[self.adj[u][i]]==0):
        #         self.DFSutil(self.adj[u][i], visited)

        for v in self.adj[u]:
            if(visited[v]==0):
                self.DFSutil(v,visited)


    def DFS(self,source):
        visited=[0 for i in range(self.nv)]

        visited[source]=1
        print(source)

        for i in self.adj:
            if(visited[i]==0):
                visited[i]=1
                self.DFSutil(i,visited)



def main():
    g=Graph(6)
    g.add_edge(2,1)
    g.add_edge(1,3)
    g.add_edge(2,5)
    g.add_edge(2,4)
    
    g.print_graph()
    
    g.DFS(0)

if __name__=="__main__":
    main()
    