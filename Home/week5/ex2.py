class Graph:
    def __init__(self,No,arr):
        self.n=No
        self.adj_list={arr[i]:[] for i in range(self.n)}
        self.arr=arr

    def add_edge(self,src,des,weight):
        self.adj_list[src].append([des,weight])
        self.adj_list[src].sort(key=lambda x:x[0])


    def print_graph(self):
        for i in range(self.n):
            print(f"{self.arr[i]} is connected to ",end=" ")
            for des,weight in self.adj_list[self.arr[i]]:
                print(f"{des}(weight:{weight})",end="  ")
            
            print()
    #very much similar to BFS but min costs involved
    def UniformCostSearch(self,start,Goal):
        visited=[]
        prqueue=[]
        ##stores cost upto that,vertex, and path
        path=[]
        prqueue.append([0,start,path])  
        prqueue.sort(key=lambda x:x[0])
        # visited.append(start)

        while(len(prqueue)!=0):
            current_cost,current_node,cur_path=prqueue.pop(0)

            if current_node not in visited:
                visited.append(current_node)
                
                cur_path.append(current_node)

                if current_node==Goal:
                    return cur_path,current_cost
            

                for des, weight in self.adj_list[current_node]:
                    if des not in visited:
                        prqueue.append([current_cost + weight, des, cur_path.copy()])
                        prqueue.sort(key=lambda x:x[0])

        return None
        

def main():
    array=['S','A','G1','B','C','G2','G3','D','E','F']
    g=Graph(10,array)
    g.add_edge('S','A',5)
    g.add_edge('S','B',9)
    g.add_edge('S','D',6)
    g.add_edge('C','S',6)
    g.add_edge('D','C',2)
    g.add_edge('D','E',2)
    g.add_edge('F','D',2)
    g.add_edge('F','G3',8)
    g.add_edge('C','F',7)
    g.add_edge('C','G2',5)
    g.add_edge('B','C',1)
    g.add_edge('A','B',3)
    g.add_edge('B','A',2)
    g.add_edge('A','G1',9)
    g.add_edge('E','G3',7)
   
   
   
    g.print_graph()

    start='S'
    goal='G3'

    result=g.UniformCostSearch(start,goal)

    if result is not None:
        path,cost=result
        print(f"Lowest Cost path form node {start} to node {goal}",path)
        print(f"Total Cost: {cost}")
    else:
        print(f"Lowest Cost path form node {start} to node {goal} NOT FOUND")
if __name__=="__main__":
    main()


    

