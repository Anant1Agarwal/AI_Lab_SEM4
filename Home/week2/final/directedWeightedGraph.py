class Graph:
    def __init__(self,No):
        self.n=No
        self.adj_list={i:[] for i in range(self.n)}

    def add_edge(self,src,des,weight):
        self.adj_list[src].append([des,weight])
        self.adj_list[src].sort(key=lambda x:x[0])
    
    def print_graph(self):
        for i in range(self.n):
            for des,weight in self.adj_list[i]:
                print(f"vertex {i} is connected to {des} with a weight of {weight}")

    
def main():
    g=Graph(6)
    g.add_edge(0,1,6)
    g.add_edge(1,2,7)
    g.add_edge(2,1,4)
    g.add_edge(2,0,5)
    g.add_edge(3,2,10)
    g.add_edge(4,5,3)
    g.add_edge(5,4,1)
    g.print_graph()

if __name__=="__main__":
    main()
    




