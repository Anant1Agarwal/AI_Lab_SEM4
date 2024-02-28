# direct acyclic graph
#additonal to check cycles

class Graph:
    def __init__(self,ver):
        self.nv=ver
        self.adj={}
        
        for i in range(self.nv):
            self.adj[i]=[]
        
    def add_edge(self,src,des):
        self.adj[src].append(des)
        
    
    def print_graph(self):
        for item in range(self.nv):
            print(item,'->',self.adj[item])


    def TopSortUtil(self,u,visited):
        print()

    def TopSort(self,source):
        visited=[0 for i in range(self.nv)]

        stack=[]
        visited[source]=1
        stack.append(source);

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

if __name__=="__main__":
    main()
    