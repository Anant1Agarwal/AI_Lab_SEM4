def main():
    g=Graph(6)
    g.add_edge(0,1,6)
    g.add_edge(1,2,7)
    g.add_edge(2,1,4)
    g.add_edge(2,0,5)
    g.add_edge(3,2,10)
    g.add_edge(4,5,3)
    g.add_edge(5,4,1)
    g.print_graph()

if __name__=="__main__":
    main()