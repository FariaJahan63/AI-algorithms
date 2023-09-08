import heapq

def astar(graph, start, goal, heuristic):
    open_set = [(0, 0, start)]  # Priority queue of nodes to be explored
    came_from = {}            # Dictionary to store parent pointers
    g_score = {node: float('inf') for node in graph}  # Cost to reach each node
    g_score[start] = 0
    visited = set()  # Set to store visited nodes

    while open_set:
        _, current_cost, current_node = heapq.heappop(open_set)

        if current_node in visited:
            continue

        visited.add(current_node)
        
        if current_node == goal:
            return reconstruct_path(came_from, current_node), g_score[goal]  # Return path and total cost
        
        for neighbor, cost in graph[current_node].items():
            if neighbor in visited:
                continue
                
            tentative_g_score = g_score[current_node] + cost
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current_node
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score, tentative_g_score, neighbor))

    return None, None  # No path found

# Rest of the code remains the same...


def reconstruct_path(came_from, current_node):
    path = [current_node]
    while current_node in came_from:
        current_node = came_from[current_node]
        path.insert(0, current_node)
    return path

# Example usage (same graph as before)
graph = {
    'S': {'A': 1,'B': 1,},
    'A': {'C': 1},
    'B': {'C': 2},
    'C': {'G':3 }, 
    'G': {}
}

def heuristic(node, goal):
    # Heuristic values based on actual distances (in this example, approximate values)
    heuristic_values = {
        'S': 2,  # Example heuristic values for the nodes
        'A': 2,
        'B': 1,
        'C': 1, 
        'G': 0
    }
    return heuristic_values[node]  # Return the heuristic value for the given node

start_node = 'S'
goal_node = 'G'

path, total_cost = astar(graph, start_node, goal_node, heuristic)
if path:
    print("Path:", path)
    print("Total cost:", total_cost)
else:
    print("No path found")
