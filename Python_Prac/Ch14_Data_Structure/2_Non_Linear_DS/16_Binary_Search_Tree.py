class Node:
    def __init__(self, data):
        # Initialize a node with data and set left and right child nodes to None
        self.data = data
        self.left = None
        self.right = None
    
    def inser(self, newdata):
        # Insert new data into the binary search tree
        if self.data:
            # If the current node has data
            if newdata < self.data:
                # If the new data is less than the current node's data
                if self.left is None:
                    # If there's no left child node, create a new one with the new data
                    self.left = Node(newdata)
                else:
                    # Otherwise, recursively call insert on the left child node
                    self.left.inser(newdata)
            elif newdata > self.data:
                # If the new data is greater than the current node's data
                if self.right is None:
                    # If there's no right child node, create a new one with the new data
                    self.right = Node(newdata)
                else:
                    # Otherwise, recursively call insert on the right child node
                    self.right.inser(newdata)
        else:
            # If the current node has no data, set the data to the new data
            self.data = newdata
    
    def Find_Value(self, key, index=0):
        # Search for a value (key) in the binary search tree
        if key < self.data:
            # If the key is less than the current node's data
            if self.left is None:
                # If there's no left child node, the key is not found
                return str(key) + " Is Not Found", None
            else:
                # Recursively search for the key in the left subtree
                return self.left.Find_Value(key, index)
        elif key > self.data:
            # If the key is greater than the current node's data
            if self.right is None:
                # If there's no right child node, the key is not found
                return str(key) + " Is Not Found", None
            else:
                # Recursively search for the key in the right subtree
                return self.right.Find_Value(key, index)
        else:
            # If the key matches the current node's data, return the data and index
            return self.data, index
        

    def printTree(self):
        # Print the binary search tree in sorted order
        if self.left:
            # If there's a left child node, recursively print its subtree
            self.left.printTree()
        print(self.data)  # Print the current node's data
        if self.right:
            # If there's a right child node, recursively print its subtree
            self.right.printTree()
        
obj = Node(12)
obj.inser(6)
obj.inser(14)
obj.inser(5)
obj.inser(3)
obj.inser(13)
# Print the binary search tree
obj.printTree()

# Search for a value in the binary search tree
n = int(input("Enter number: "))

# Call the Find_Value method to search for the value
find, index = obj.Find_Value(n)

# Check if the result is a string (indicating the value was not found)
if isinstance(find, str):
    print(find)  # Print a message indicating the value was not found
else:
    # Print a message indicating the value was found along with its index
    print(f"The value {find} is found at index {index}")
