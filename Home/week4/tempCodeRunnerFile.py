
class Graph:
    def __init__(self,No):
        self.n=No
        self.adj_list={i:[] for i in range(self.n)}
       

    def add_edge(self,src,des):
        self.adj_list[src].append(des)
        self.adj_list[src].sort()

    def print_graph(self):
        for i in range(self.n):
            print(f"{i} is connected to ",end="")
            for des in self.adj_list[i]:
                print(f"->{des}",end=" ")
            print()
    
    def BFSutil(self,v,visited):
        queue=[]
        queue.append(v)
        
        while(len(queue)!=0):
            new=queue.pop(0)
            print(new)

            for item in self.adj_list[new]:
                if item not in visited:
                    queue.append(item)
                    visited.append(new)


    def BFS(self):
        visited=[]
        
        for i in range(self.n):
            if i not in visited:
                self.BFSutil(i,visited)
        
            

def main():
    
    g=Graph(4)
    g.add_edge(0,1)
    g.add_edge(2,0)
    g.add_edge(0,2)
    g.add_edge(2,3)
    # g.add_edge(3,3)
    g.BFS()
    


if __name__=="__main__":
    main()

