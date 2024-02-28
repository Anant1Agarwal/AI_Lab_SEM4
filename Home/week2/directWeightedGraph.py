class Graph:
    def __init__(self,n):
        self.nv=n
        self.adj={}

        for i in range(n):
            self.adj[i]=[]
        
    def addEdge(self,src,des,weight):
        self.adj[src].append([des,weight])
    
    # def printGraph(self):
    #     for i in range(self.nv):
    #         print(i,"->",self.adj[i])
    def printGraph(self):
        for i in range(self.nv):
            for j in range(len(self.adj[i])):
                print(i,"connected to",self.adj[i][j][0],"with a weight of",self.adj[i][j][1])
    

def main():
    g=Graph(6)
    g.addEdge(2,0,5)
    g.addEdge(0,1,6)
    g.addEdge(2,1,4)
    g.addEdge(1,2,7)
    g.addEdge(3,2,10)
    g.addEdge(4,5,3)
    g.addEdge(5,4,1)
    g.printGraph()
    
if __name__=="__main__":
    main()
    