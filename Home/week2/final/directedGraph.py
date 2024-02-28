class Graph:
    def __init__(self,No):
        self.n=No
        self.adj_list={}
        
        for i in range(self.n):
            self.adj_list[i]=[]
        
    def add_edge(self,src,des):
        self.adj_list[src].append(des)
        self.adj_list[src].sort()
    
    def print_graph(self):
        for item in range(self.n):
            print(item,'->',self.adj_list[item])
    
def main():
    g=Graph(6)
    g.add_edge(0,1)
    g.add_edge(1,2)
    g.add_edge(2,1)
    g.add_edge(2,0)
    g.add_edge(3,2)
    g.add_edge(4,5)
    g.add_edge(5,4)
    g.print_graph()

if __name__=="__main__":
    main()
    