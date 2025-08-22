#EXample 1 Create Root
"""
We just create a Node class and add assign a value to the node. This becomes tree with only a root node"""

from typing import Any


class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def printTree(self):
        return self.data
#Create obj
obj=Node(10)
print("Root Node: ",obj.printTree())

#EXample 2 Inserting into a Tree
"""
To insert into a tree we use the same node class created above and add a insert class to it. The insert class compares the value of the node to the parent node and decides to add it as a left node or a right node. Finally the PrintTree class is used to print the tree."""
print("\n\n******************************** Insert Into Tree ***************************")
# Define a class Node
class Node:
    def __init__(self, data):
        self.data = data  # Initialize the data attribute of the node with the value of data
        self.left = None  # Initialize the left child of the node as None
        self.right = None  # Initialize the right child of the node as None

    # Insert into Tree
    def insert(self, newdata):
        if self.data:
            if newdata < self.data:
                if self.left is None:
                    self.left = Node(newdata)  # Create a new node with newdata and set it as the left child of the current node
                else:
                    self.left.insert(newdata)  # Recursively call insert method on the left child of the current node
            elif newdata > self.data:
                if self.right is None:
                    self.right = Node(newdata)  # Create a new node with newdata and set it as the right child of the current node
                else:
                    self.right.insert(newdata)  # Recursively call insert method on the right child of the current node
        else:
            self.data = newdata  # If the current node is empty, set its data to newdata

    # Print the tree
    def printTree(self):
        if self.left:
            self.left.printTree()  # Recursively call printTree method on the left child of the current node

        print(self.data)  # Print the data of the current node

        if self.right:
            self.right.printTree()  # Recursively call printTree method on the right child of the current node

# Use the insert method to add nodes
obj = Node(12)
obj.insert(6)
obj.insert(14)
obj.insert(3)
obj.insert(11)
obj.insert(13)
obj.printTree()  # Print the tree


print("\n\n************************************************ In-Order Traversing**********************************************************")

# Define a class Node
class Node:
    def __init__(self, data):
        self.data = data  # Initialize the data attribute of the node with the value of data
        self.left = None  # Initialize the left child of the node as None
        self.right = None  # Initialize the right child of the node as None

    # Insert into Tree
    def insert(self, newdata):
        if self.data:
            if newdata < self.data:
                if self.left is None:
                    self.left = Node(newdata)  # Create a new node with newdata and set it as the left child of the current node
                else:
                    self.left.insert(newdata)  # Recursively call insert method on the left child of the current node
            elif newdata > self.data:
                if self.right is None:
                    self.right = Node(newdata)  # Create a new node with newdata and set it as the right child of the current node
                else:
                    self.right.insert(newdata)  # Recursively call insert method on the right child of the current node
        else:
            self.data = newdata  # If the current node is empty, set its data to newdata

    # Print the tree
    def printTree(self):
        if self.left:
            self.left.printTree()  # Recursively call printTree method on the left child of the current node

        print(self.data)  # Print the data of the current node

        if self.right:
            self.right.printTree()  # Recursively call printTree method on the right child of the current node

    # In order traversal
    # Left -> Parent -> Right
    def In_Order(self, root):
        #L-P_R
        res = []
        if root:
            res = self.In_Order(root.left)  # Recursively call In_Order method on the left child of the current node
            res.append(root.data)  # Append the data of the current node to the result list
            res = res + self.In_Order(root.right)  # Recursively call In_Order method on the right child of the current node

        return res

# Use the insert method to add nodes
obj = Node(27)
obj.insert(14)
obj.insert(35)
obj.insert(10)
obj.insert(19)
obj.insert(31)
obj.insert(42)

obj.printTree()  # Print the tree
print(obj.In_Order(obj))  # Print the tree in order

"""
************************************************ In-Order Traversing**********************************************************
10
14
19
27
31
35
42
[10, 14, 19, 27, 31, 35, 42]
"""

print("\n\n******************************* Pre-Order Traversing***************************************")
# Define a class Node
class Node:
    def __init__(self, data):
        self.data = data  # Initialize the data attribute of the node with the value of data
        self.left = None  # Initialize the left child of the node as None
        self.right = None  # Initialize the right child of the node as None

    # Insert into Tree
    def insert(self, newdata):
        if self.data:
            if newdata < self.data:
                if self.left is None:
                    self.left = Node(newdata)  # Create a new node with newdata and set it as the left child of the current node
                else:
                    self.left.insert(newdata)  # Recursively call insert method on the left child of the current node
            elif newdata > self.data:
                if self.right is None:
                    self.right = Node(newdata)  # Create a new node with newdata and set it as the right child of the current node
                else:
                    self.right.insert(newdata)  # Recursively call insert method on the right child of the current node
        else:
            self.data = newdata  # If the current node is empty, set its data to newdata

    # Print the tree
    def printTree(self):
        if self.left:
            self.left.printTree()  # Recursively call printTree method on the left child of the current node

        print(self.data)  # Print the data of the current node

        if self.right:
            self.right.printTree()  # Recursively call printTree method on the right child of the current node

    def Pre_Order(self,root):
        #P-L-R
        result=[]
        if root:
            #first parent
            result.append(root.data)
            #then left
            result=result+self.Pre_Order(root.left)
            result=result+self.Pre_Order(root.right)
        return result
    
obj=Node(27)
obj.insert(14)
obj.insert(35)
obj.insert(10)
obj.insert(19)
obj.insert(31)
obj.insert(42)

#called printTree()
obj.printTree()

#called pre_Order()
print(obj.Pre_Order(obj))

print('\n\n****************************** Post-Order Traversing*****************************')
# Define a class Node
class Node:
    def __init__(self, data):
        self.data = data  # Initialize the data attribute of the node with the value of data
        self.left = None  # Initialize the left child of the node as None
        self.right = None  # Initialize the right child of the node as None

    # Insert into Tree
    def insert(self, newdata):
        if self.data:
            if newdata < self.data:
                if self.left is None:
                    self.left = Node(newdata)  # Create a new node with newdata and set it as the left child of the current node
                else:
                    self.left.insert(newdata)  # Recursively call insert method on the left child of the current node
            elif newdata > self.data:
                if self.right is None:
                    self.right = Node(newdata)  # Create a new node with newdata and set it as the right child of the current node
                else:
                    self.right.insert(newdata)  # Recursively call insert method on the right child of the current node
        else:
            self.data = newdata  # If the current node is empty, set its data to newdata

    # Print the tree
    def printTree(self):
        if self.left:
            self.left.printTree()  # Recursively call printTree method on the left child of the current node

        print(self.data)  # Print the data of the current node

        if self.right:
            self.right.printTree()  # Recursively call printTree method on the right child of the current node

    def Post_Order(self,root):
        #L--R-P
        result=[]
        if root:
            result=self.Post_Order(root.left)
            result=result + self.Post_Order(root.right)
            result.append(root.data)
        return result
obj=Node(27)
obj.insert(14)
obj.insert(35)
obj.insert(10)
obj.insert(19)
obj.insert(31)
obj.insert(42)

#called printTree()
obj.printTree()

#called pre_Order()
print(obj.Post_Order(obj))
"""
****************************** Post-Order Traversing*****************************    
10
14
19
27
31
35
42
[10, 19, 14, 31, 42, 35, 27]"""