from queue import PriorityQueue

class Graph:
    def __init__(self, No, arr):
        self.n = No
        self.adj_list = {arr[i]: [] for i in range(self.n)}
        self.arr = arr

    def add_edge(self, src, des, weight):
        self.adj_list[src].append([des, weight])
        self.adj_list[src].sort(key=lambda x: x[0])
        self.adj_list[des].append([src, weight])
        self.adj_list[des].sort(key=lambda x: x[0])

    def print_graph(self):
        for i in range(self.n):
            print(f"{self.arr[i]} is connected to ", end=" ")
            for des, weight in self.adj_list[self.arr[i]]:
                print(f"{des}(weight:{weight})", end=" ")
            print()

def heuristic(a, b):
    # You can define your own heuristic function here
    # For example, you can use the Euclidean distance
    # between the two nodes if they have coordinates
    return abs(ord(a) - ord(b))

def a_star_search(graph, start, goal):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            # Reconstruct the path
            path = [goal]
            while current != start:
                current = came_from[current]
                path.append(current)
            path.reverse()
            return path, cost_so_far[goal]

        for next_node, weight in graph.adj_list[current]:
            new_cost = cost_so_far[current] + weight
            if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                cost_so_far[next_node] = new_cost
                priority = new_cost + heuristic(next_node, goal)
                frontier.put(next_node, priority)
                came_from[next_node] = current

    return [], 0  # No path found

array = ['A', 'B', 'C', 'D', 'E']
g = Graph(5, array)
g.add_edge('A', 'B', 6)
g.add_edge('A', 'E', 7)
g.add_edge('A', 'C', 4)
g.add_edge('B', 'C', 5)
g.add_edge('C', 'D', 10)
g.add_edge('C', 'E', 3)

start = 'A'
goal = 'D'
path, total_cost = a_star_search(g, start, goal)
if path:
    print(f"The shortest path from {start} to {goal} is: {' -> '.join(path)}")
    print(f"The total cost of the path is: {total_cost}")
else:
    print(f"No path found from {start} to {goal}")
