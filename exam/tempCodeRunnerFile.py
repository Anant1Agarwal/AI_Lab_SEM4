size = 4
pits = [(1, 1), (2, 2), (3, 3)]
wumpus = (2, 1)
gold = (3, 0)

world = WumpusWorld(size, pits, wumpus, gold)
start_position = (0, 0)
path = world.bfs(start_position)

if path:
    print("Path found:")
    for i, position in enumerate(path):
        print(f"Step {i+1}: {position}")
else:
    print("No path found.")