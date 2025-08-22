#EXample 1 DFT (Depth First Traversal)
# Define a class named 'graph'
print("\n\n******************** DFS **************************")
class graph:
    # Define the initialization method for the class
    def __init__(self, gdict=None):
        # Check if a graph dictionary is provided, otherwise initialize an empty dictionary
        if gdict is None:
            gdict = {}
        # Assign the provided or initialized dictionary to the 'gdict' attribute of the class instance
        self.gdict = gdict
    
    # Define the Depth First Search (DFS) method
    def DFS(self, start, visited=None):
        # Initialize the set of visited nodes if not provided
        if visited is None:
            visited = set()

        # Mark the current node as visited
        visited.add(start)
        # Print the current node
        print(start)

        # Iterate through the adjacent nodes of the current node
        for next_node in self.gdict[start] - visited:
            # Recursively call DFS for unvisited adjacent nodes
            self.DFS(next_node, visited)

        # Return the set of visited nodes
        return visited

# Define the graph as a dictionary
gdict = { 
   "a": set(["b", "c"]),
   "b": set(["a", "d"]),
   "c": set(["a", "d"]),
   "d": set(["e"]),
   "e": set(["a"])
}

# Create an instance of the graph class
obj = graph(gdict)
# Perform DFS traversal starting from node 'a'
obj.DFS("a")


#Example 2 BFS (Breadth first Search)
# Print a header indicating BFS (Breadth First Search) is being performed
print("\n\n **************************** BFS ********************************")

# Import the 'collections' module for deque data structure
import collections

# Define a class named 'graph'
class graph:
    # Define the initialization method for the class
    def __init__(self, gdict=None):
        # Check if a graph dictionary is provided, otherwise initialize an empty dictionary
        if gdict is None:
            gdict = {}
        # Assign the provided or initialized dictionary to the 'gdict' attribute of the class instance
        self.gdict = gdict

    # Define the BFS (Breadth First Search) method
    def BFS(self, start_Node):
        # Track the visited and unvisited nodes using a set for 'seen' and a deque for 'dqueue'
        seen, dqueue = set([start_Node]), collections.deque([start_Node])

        # Iterate until the deque is empty
        while dqueue:
            # Remove the leftmost node from the deque and assign it to 'vertex'
            vertex = dqueue.popleft()
            # Call the 'marked' method to print the visited node
            self.marked(vertex)
            # Iterate through the adjacent nodes of 'vertex'
            for node in self.gdict[vertex]:
                # If the adjacent node is not visited yet
                if node not in seen:
                    # Mark it as visited and add it to the deque for further traversal
                    seen.add(node)
                    dqueue.append(node)

    # Define the 'marked' method to print the visited node
    def marked(self, n):
        # Print the visited node
        print(n)

# Define the graph as a dictionary
gdict = {
   "a": set(["b", "c"]),
   "b": set(["a", "d"]),
   "c": set(["a", "d"]),
   "d": set(["e"]),
   "e": set(["a"])
}

# Create an instance of the graph class with the provided graph dictionary
obj = graph(gdict)
# Perform BFS traversal starting from node 'a'
obj.BFS("a")
