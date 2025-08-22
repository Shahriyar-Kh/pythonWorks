#Example 1  PUSH into a Stack
class Stack:
    def __init__(self):
        self.stack=[]
    
    def add(self,dataval):
        #use list append method to add element
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False
    #Use peek to lock at the top
    def peek(self):
        return self.stack[-1]
    
obj=Stack()
obj.add("Monday")
obj.add("Tuesday")
#obj.peek() or
print(obj.peek())
obj.add("Wed")
obj.add("Friday")
print(obj.peek())

#Example POP from a Stack
"""

As we know we can remove only the top most data element from the stack, we implement a python program which does that. The remove function in the following program returns the top most element. we check the top element by calculating the size of the stack first and then use the in-built pop() method to find out the top most element."""

class Stack:
    def __init__(self):
        self.stack = []  # initialize an empty list
    
    def add(self, dataval):
        # use list append method to add element
        if dataval not in self.stack:  # check if the element is already present in the stack
            self.stack.append(dataval)  # add the element to the stack
            return True
        else:
            return False
    
    def peek(self):
        return self.stack[-1]  # return the top element of the stack
    
    def remove(self):
        if len(self.stack) <= 0:  # check if the stack is empty
            return "No element in the Stack"
        else:
            return self.stack.pop()  # remove and return the top element of the stack
    
    def printitem(self):
        if len(self.stack) == 0:  # check if the stack is empty
            return "Stack is empty"
        s = list()
        for i in self.stack:
            s.append(i)
        return s  # return the elements of the stack as a list

obj=Stack()
obj.add(1)
obj.add(2)

print("Top of Stack:",obj.peek())
obj.add(3)
obj.add(4)
obj.add(5)
print("Top of Stack:",obj.peek())

print("Orignal Stack:",obj.printitem())

print("Poped Item:",obj.remove())
print("Poped item:",obj.remove())
print("Stack after Poped items:"+str(obj.printitem()))