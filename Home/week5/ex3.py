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
    array=['Maldon','Blaxhali','Dunwich','Harwich','Clacton','Tiptree','Feering']
    g=Graph(7,array)
    g.add_edge('Maldon','Tiptree',8)
    g.add_edge('Feering','Maldon',11)
    g.add_edge('Clacton','Maldon',40)
    g.add_edge('Harwich','Tiptree',31)
    g.add_edge('Feering','Blaxhali',46)
    g.add_edge('Dunwich','Blaxhali',17)
    g.add_edge('Harwich','Blaxhali',40)
    
    g.add_edge('Harwich','Dunwich',53)
    g.add_edge('Blaxhali','Dunwich',15)
    g.add_edge('Clacton','Harwich',17)
    g.add_edge('Tiptree','Clacton',29)
    g.add_edge('Tiptree','Feering',3)
    
    
   
   
   
    g.print_graph()

    start='Maldon'
    goal='Dunwich'

    result=g.UniformCostSearch(start,goal)

    if result is not None:
        path,cost=result
        print(f"Lowest Cost path form node {start} to node {goal}",path)
        print(f"Total Cost: {cost}")
    else:
        print(f"Lowest Cost path form node {start} to node {goal} NOT FOUND")
if __name__=="__main__":
    main()


    

