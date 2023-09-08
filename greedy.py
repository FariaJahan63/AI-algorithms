# A Node class for GBFS Pathfinding
class Node:
    def _init_(self, v, weight):
        self.v=v
        self.weight=weight

# pathNode class will help to store
# the path from src to dest.
class pathNode:
    def _init_(self, node, parent):
        self.node=node
        self.parent=parent

# Function to add edge in the graph.
def addEdge(u, v, weight):
    # Add edge u -> v with weight weight.
    adj[u].append(Node(v, weight))


# Declaring the adjacency list
adj = []
# Greedy best first search algorithm function
def GBFS(h, V, src, dest):
    """ 
    This function returns a list of 
    integers that denote the shortest
    path found using the GBFS algorithm.
    If no path exists from src to dest, we will return an empty list.
    """
    # Initializing openList and closeList.
    openList = []
    closeList = []

    # Inserting src in openList.
    openList.append(pathNode(src, None))

    # Iterating while the openList 
    # is not empty.
    while (openList):

        currentNode = openList[0]
        currentIndex = 0
        # Finding the node with the least 'h' value
        for i in range(len(openList)):
            if(h[openList[i].node] < h[currentNode.node]):
                currentNode = openList[i]
                currentIndex = i

        # Removing the currentNode from 
        # the openList and adding it in 
        # the closeList.
        openList.pop(currentIndex)
        closeList.append(currentNode)
        
        # If we have reached the destination node.
        if(currentNode.node == dest):
            # Initializing the 'path' list. 
            path = []
            cur = currentNode

            # Adding all the nodes in the 
            # path list through which we have
            # reached to dest.
            while(cur != None):
                path.append(cur.node)
                cur = cur.parent
            

            # Reversing the path, because
            # currently it denotes path
            # from dest to src.
            path.reverse()
            return path
        

        # Iterating over adjacents of 'currentNode'
        # and adding them to openList if 
        # they are neither in openList or closeList.
        for node in adj[currentNode.node]:
            for x in openList:
                if(x.node == node.v):
                    continue
            
            for x in closeList:
                if(x.node == node.v):
                    continue
            
            openList.append(pathNode(node.v, currentNode))

    return []

# Driver Code
""" Making the following graph
             src = 0
            / | \
           /  |  \
          1   2   3
         /\   |   /\
        /  \  |  /  \
        4   5 6 7    8
               /
              /
            dest = 9
"""
# The total number of vertices.
V = 8
## Initializing the adjacency list
for i in range(V):
    adj.append([])

addEdge(0, 1, 140)
addEdge(0, 2, 118)
addEdge(0, 3, 75)
addEdge(1, 4, 99)
addEdge(1, 5, 151)
addEdge(1, 6, 80)
addEdge(4, 7, 211)

# Defining the heuristic values for each node.
h = [366, 253, 329, 374, 178, 380, 193, 0]
path = GBFS(h, V, 0, 7)
for i in range(len(path) - 1):
    print(path[i], end = " -> ")

print(path[(len(path)-1)])
