class DirectedUnweightedGraphwithAlphabets:
    def __init__(self, no_of_vertices):
        self.v=no_of_vertices
        # self.adj_list=[]

        # for i in range(self.v):
        #     self.adj_list[i]=[]
        self.adj_list = [[] for _ in range(no_of_vertices)]
        self.data_list=[]

        print("Enter characters in graph:")
        for i in range(self.v):
            c=input()
            self.data_list.append(c)

    def addEdge(self,source_data, destination_data):
        # if(source_data not in self.data_list):
        #     self.data_list.append(source_data)
        
        source=self.data_list.index(source_data)
        destination=self.data_list.index(destination_data)

        self.adj_list[source].append(destination)
        self.adj_list[destination].append(source)
        
    
    def printGraph(self):
        for i in range(self.v):
            print(self.data_list[i],":[",end=" ")
            for j in range(len(self.adj_list[i])):
                if(self.adj_list[i][j]==1):
                    print(self.data_list[j], end="")
            print(":]")   
            print()

if __name__=="__main__":
    g1=DirectedUnweightedGraphwithAlphabets(5)
    g1.addEdge('A','B') 
    g1.addEdge('A','C') 
    g1.addEdge('A','E') 
    g1.addEdge('B','C')
    g1.addEdge('C','D')
    g1.addEdge('C','E')

    g1.printGraph()
    
    