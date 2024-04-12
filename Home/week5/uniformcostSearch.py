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
                
                

                if current_node==Goal:
                    return cur_path,current_cost
            

                for des, weight in self.adj_list[current_node]:
                    if des not in visited:
                        new_path=cur_path+[des]
                        prqueue.append([current_cost + weight, des, new_path])
                        prqueue.sort(key=lambda x:x[0])


        return None
        

def main():
    array=['S','1','2','3','4','5','G']
    g=Graph(7,array)
    g.add_edge('S','1',2)
    g.add_edge('S','3',5)
    g.add_edge('1','G',1)
    g.add_edge('3','G',6)
    g.add_edge('5','G',3)
    g.add_edge('2','1',4)
    g.add_edge('4','2',4)
    g.add_edge('5','2',6)
    g.add_edge('3','4',2)
    g.add_edge('G','4',7)
    g.add_edge('4','5',3)
   
   
    g.print_graph()

    start='S'
    goal='G'

    result=g.UniformCostSearch(start,goal)

    if result is not None:
        path,cost=result
        print(f"Lowest Cost path form node {start} to node {goal}",path)
        print(f"Total Cost: {cost}")
    else:
        print(f"Lowest Cost path form node {start} to node {goal} NOT FOUND")
if __name__=="__main__":
    main()


    

