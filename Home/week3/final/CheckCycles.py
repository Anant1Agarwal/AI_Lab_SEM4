
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
    
    def Checkcycleutil(self, visited,v, path):
        visited.append(v)
        path.append(v)
        for i in self.adj_list[v]:
            if(i not in visited):
                if(self.Checkcycleutil(visited,i,path)):
                    return True
            elif( i in path):
                return True

        path.remove(v)
        return False
        
    

    def CheckCycle(self,node):
        visited=[]
        path=[]
        for i in range(self.n):
            if i not in visited:
                if(self.Checkcycleutil(visited,i,path)):
                    return True
                
        return False

def main():
    
    g=Graph(4)
    g.add_edge(0,1)
    g.add_edge(2,0)
    g.add_edge(0,2)
    g.add_edge(2,3)
    # g.add_edge(3,3)

    
    g.print_graph()
    if (g.CheckCycle(0)):
        print("Graph has Cycles.")
    else:
        print("No cycle detected")


if __name__=="__main__":
    main()

