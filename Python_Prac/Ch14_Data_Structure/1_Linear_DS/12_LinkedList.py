#Example1 Single linked list  Creation

class Node:
    def __init__(self,dataval=None):
        self.dataval=dataval
        self.nextval=None
class Single_linked_list:
    def __init__(self):
        self.headval=None

list1=Single_linked_list()
list1.headval=Node("Mon")
e2=Node("Tuesday")
e3=Node("Wed")

#Link first node to second node
list1.headval.nextval=e2

#link second node to third node
e2.nextval=e3


#Example 2 Traversing a Linked List
"""
Singly linked lists can be traversed in only forward direction starting form the first data element. We simply print the value of the next data element by assigning the pointer of the next node to the current data element."""

# Define a class Node with two attributes: dataval and nextval
class Node:
   def __init__(self, dataval=None):
      self.dataval = dataval
      self.nextval = None

# Define a class SLinkedList with one attribute: headval
class SLinkedList:
   def __init__(self):
      self.headval = None

   # Define a method listprint to print the linked list
   def listprint(self):
           printvalue=self.headval
           while printvalue is not None:
               print(printvalue.dataval)
               printvalue=printvalue.nextval

# Create an instance of the SLinkedList class
list2=SLinkedList()

# Create three instances of the Node class with data values "Monday", "Tuesday", and "Wed"
list2.headval=Node("Monday")
e2=Node("Tuesday")
e3=Node("Wed")

# Link the first node to the second node
list2.headval.nextval=e2

# Link the second node to the third node
e2.nextval=e3

# Print the linked list
list2.listprint()

#Example 3 Insertion in a Linked List
"""
Inserting element in the linked list involves reassigning the pointers from the existing nodes to the newly inserted node. Depending on whether the new data element is getting inserted at the beginning or at the middle or at the end of the linked list, we have the below scenarios.
"""
# Inserting at the Beginning
"""
This involves pointing the next pointer of the new data node to the current head of the linked list. So the current head of the linked list becomes the second data element and the new node becomes the head of the linked list."""

# Define a class Node with two attributes: dataval and nextval
class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

# Define a class SLinkedList with one attribute: headval
class SLinkedList:
    def __init__(self):
        self.headval = None

    # Define a method listprint to print the linked list
    def listprint(self):
        # Set printvalue to the head node
        printvalue = self.headval

        # Traverse the linked list and print the data value of each node
        while printvalue is not None:
            print(printvalue.dataval)
            printvalue = printvalue.nextval

    # Define a method atbeginning to insert a new node at the beginning of the linked list
    def atbeginning(self, newdata):
        # Create a new node with the given data
        NewNode = Node(newdata)

        # Update the new node's next val to existing node
        NewNode.nextval = self.headval
        self.headval = NewNode

    #Create function for add node at end
    def atEnd(self,newdata2):
        #create a new node with given data
        newNode=Node(newdata2)

        #if the linkedlist is empty ,set the new node as the head
        if self.headval is None:
            self.headval=newNode
            return
        #Travers the linked list to find the last node

        lastn=self.headval
        while lastn.nextval:
            lastn=lastn.nextval
        #Link the last node to the new node 
            lastn.nextval=newNode

# Create an instance of the SLinkedList class
list3 = SLinkedList()

# Create three instances of the Node class with data values "Mon", "Tuesday", and "Wed"
list3.headval = Node("Mon")
e2 = Node("Tuesday")
e3 = Node("Wed")

# Link the first node to the second node
list3.headval.nextval = e2

# Link the second node to the third node
e2.nextval = e3

# Insert a new node with data value "Sun" at the beginning of the linked list
list3.atbeginning("Sun")

#Insert new node at End
list3.atEnd("Thursday")
# Print the linked list
list3.listprint()


