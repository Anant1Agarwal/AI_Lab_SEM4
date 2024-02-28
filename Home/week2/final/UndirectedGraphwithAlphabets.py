class Graph:
    def __init__(self,No,arr):
        self.n=No
        self.adj_list={arr[i]:[] for i in range(self.n)}
        self.arr=arr

    def add_edge(self,src,des,weight):
        self.adj_list[src].append([des,weight])
        self.adj_list[src].sort(key=lambda x:x[0])

        self.adj_list[des].append([src,weight])
        self.adj_list[des].sort(key=lambda x:x[0])

    def print_graph(self):
        for i in range(self.n):
            print(f"{self.arr[i]} is connected to ",end=" ")
            for des,weight in self.adj_list[self.arr[i]]:
                print(f"{des}(weight:{weight})",end="  ")
            
            print()

def main():
    array=['A','B','C','D','E']
    g=Graph(5,array)
    g.add_edge('A','B',6)
    g.add_edge('A','E',7)
    g.add_edge('A','C',4)
    g.add_edge('B','C',5)
    g.add_edge('C','D',10)
    g.add_edge('C','E',3)
    g.print_graph()

if __name__=="__main__":
    main()


    

