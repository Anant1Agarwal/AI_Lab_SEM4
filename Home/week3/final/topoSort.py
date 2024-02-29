
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
    
    def topoutil(self, visited, v, stack):
        visited.append(v)
        for i in self.adj_list[v]:
            if(i not in visited):
                self.topoutil(visited,i,stack)
        
        stack.append(v)



    def topo_sort(self,node,visited):
        # if node not in visited:
        #     visited.append(node)
            
        #     for k in self.adj_list[node]:
        #         if k not in visited:
        #             self.dfs(k,visited)
            
        #     stack=[]
        #     stack.append(node)
        #     print(stack[-1:])

        stack=[]
        for i in range(self.n):
            if i not in visited:
                self.topoutil(visited,i,stack)
        
        print(stack[::-1])

            

def main():
    
    g=Graph(6)
    g.add_edge(5,2)
    g.add_edge(5,0)
    g.add_edge(4,0)
    g.add_edge(4,1)
    g.add_edge(2,3)
    g.add_edge(3,1)
  

    
    g.print_graph()
    g.topo_sort(0,[])


if __name__=="__main__":
    main()

