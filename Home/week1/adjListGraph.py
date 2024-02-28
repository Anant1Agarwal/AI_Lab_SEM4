class adjGraph:
    def __init__(self):
        n=int(input("Enter Number of vertices:"))
        self.v=n

        #basically a dictionary, with key as i/vertex and value as list
        self.adj_list={i:[] for i in range(n)} 
       
        self.create_graph_from_list()


    def create_graph_from_list(self):
        print(" Enter the adjacency list(comma-seperated,-1 to end to a list")
        for i in range(self.v):
            neighbours=list(map(int, input().split(',')))
            if neighbours==[-1]:
                continue
            self.adj_list[i]=neighbours


    def print_adj_list(self):
        for i in range(self.v):
            print(i,"is connected to",end=" ")
            for j in range(len(self.adj_list[i])):
                print("->",self.adj_list[i][j] ,end=" ")
            print()


if __name__=="__main__":
    g1=adjGraph()
    print("Your given Graph adjacency List is:")
    g1.print_adj_list()
    