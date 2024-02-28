class DirectedUndirectedGraph:


    def __init__(self, no_of_vertices):
        self.v=no_of_vertices
        # self.adj_list=[]

        # for i in range(self.v):
        #     self.adj_list[i]=[]
        self.adj_list = [[] for _ in range(no_of_vertices)]


    def addEdge(self,source, destination):
        self.adj_list[source].append(destination)
    
    def printGraph(self):
        for k in range(self.v):
            for j in range(len(self.adj_list[k])):
                print("(",k,"->",self.adj_list[k][j],")", end="")
                
            print()

if __name__=="__main__":
    g1=DirectedUndirectedGraph(6)
    g1.addEdge(0,1)
    g1.addEdge(1,2)
    g1.addEdge(2,0)
    g1.addEdge(2,1)
    g1.addEdge(3,2)
    g1.addEdge(4,5)
    g1.addEdge(5,4)
    g1.printGraph()
    
    