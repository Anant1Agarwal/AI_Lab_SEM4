class Graph:
    def __init__(self,n,vertices):
        self.nv=n
        self.adjList={}
        self.vertices=vertices
        
        for i in range(self.nv):
            self.adjList[i]=[]
        
        self.adjMat=[[0 for col in range(5)] for row in range(5)]

            
    def add_edge(self,src,des):
        src=self.vertices.index(src)
        des=self.vertices.index(des)
        self.adjList[src].append(des)
        self.adjList[des].append(src)

        self.adjMat[src][des]=1
        self.adjMat[des][src]=1

    
    def printGraph(self):
        print("Adjacency List is:")
        for i in range(self.nv):
            print(self.vertices[i],"->",end=" ")
            for j in range(len(self.adjList[i])):
                print(self.vertices[self.adjList[i][j]],end=" ")
            print()

        print("Adjacency Matrix is:")

        for i in range(len(self.adjMat)):
            for j in range(len(self.adjMat[0])):
                print(self.adjMat[i][j],end=" ")
            print()
            
    
def main():
    
    vertices=['A','B','C','D','E']
    g=Graph(5,vertices)
    g.add_edge('A','B')
    g.add_edge('A','E')
    g.add_edge('A','C')
    g.add_edge('C','B')
    g.add_edge('C','D')
    g.printGraph()


if __name__=="__main__":
    main()
    