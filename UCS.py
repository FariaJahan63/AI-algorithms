import heapq

# Define the Romania map as a graph represented as an adjacency list
romania_map = {
    'Arad': [('Zerind', 75), ('Sibiu', 140), ('Timisoara', 118)],
    'Zerind': [('Arad', 75), ('Oradea', 71)],
    'Oradea': [('Zerind', 71), ('Sibiu', 151)],
    'Timisoara': [('Arad', 118), ('Lugoj', 111)],
    'Lugoj': [('Timisoara', 111), ('Mehadia', 70)],
    'Mehadia': [('Lugoj', 70), ('Drobeta', 75)],
    'Drobeta': [('Mehadia', 75), ('Craiova', 120)],
    'Craiova': [('Drobeta', 120), ('Rimnicu Vilcea', 146), ('Pitesti', 138)],
    'Sibiu': [('Arad', 140), ('Oradea', 151), ('Fagaras', 99), ('Rimnicu Vilcea', 80)],
    'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
    'Rimnicu Vilcea': [('Sibiu', 80), ('Craiova', 146), ('Pitesti', 97)],
    'Pitesti': [('Rimnicu Vilcea', 97), ('Craiova', 138), ('Bucharest', 101)],
    'Bucharest': [('Fagaras', 211), ('Pitesti', 101), ('Urziceni', 85), ('Giurgiu', 90)],
    'Urziceni': [('Bucharest', 85), ('Hirsova', 98), ('Vaslui', 142)],
    'Hirsova': [('Urziceni', 98), ('Eforie', 86)],
    'Eforie': [('Hirsova', 86)],
    'Vaslui': [('Urziceni', 142), ('Iasi', 92)],
    'Iasi': [('Vaslui', 92), ('Neamt', 87)],
    'Neamt': [('Iasi', 87)]
}

def ucs_search(graph, start, goal):
    priority_queue = [(0, start, [])]  # Priority queue to store (cost, node, path) tuples
    visited = set()  # Set to keep track of visited nodes

    while priority_queue:
        cost, current_node, path = heapq.heappop(priority_queue)

        if current_node in visited:
            continue

        visited.add(current_node)

        if current_node == goal:
            return cost, path + [current_node]

        for neighbor, edge_cost in graph[current_node]:
            if neighbor not in visited:
                new_cost = cost + edge_cost
                new_path = path + [current_node]
                heapq.heappush(priority_queue, (new_cost, neighbor, new_path))

    return None, []  # Goal not reached, return cost as None and an empty path

# Define the start and goal cities
start_city = 'Arad'
goal_city = 'Bucharest'

# Find the cost and path using UCS
cost, path = ucs_search(romania_map, start_city, goal_city)

if cost is not None:
    print(f"Path from {start_city} to {goal_city}:")
    print(" -> ".join(path))
    print(f"Total Cost: {cost}")
else:
    print(f"No path found from {start_city} to {goal_city}")
