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
    
def main():
    g=Graph(6)
    g.add_edge(0,1)
    g.add_edge(1,2)
    
    g.add_edge(2,0)
    g.add_edge(3,2)
    g.add_edge(4,5)
    
    g.print_graph()

if __name__=="__main__":
    main()
    