class adjGraph:
    def __init__(self):
        n=int(input("Enter Number of vertices:"))
        self.v=n

        self.adj_matrix=[[0]*n for _ in range(n)]
        self.create_graph_from_matrix()


    def create_graph_from_matrix(self):
        print("Enter adjacency matrix (row-wise): ")
        for i in range(self.v):
            row_values=list(map(int, input().split()))
            self.adj_matrix[i]=row_values


    def print_adj_matrix(self):
        # n=self.v
        # for i in range(n):
        #     for j in range(n):
        #         print(self.adj_matrix[i][j],end=" ")
        #     print()
        print(self.adj_matrix)


if __name__=="__main__":
    g1=adjGraph()
    print("Your given Graph Matrix is:")
    g1.print_adj_matrix()
    
