#Example 1 Creating Queue
class Queue:
    def __init__(self):
        self.queue = []  # initialize an empty list
    
    def addelement(self, dataval):
        # use list insert method to add element 
        if dataval not in self.queue:  # check if the element is already present in the queue
            self.queue.insert(0, dataval)  # add the element to the queue
            return True
        return False
    
    def size(self):
        return len(self.queue)  # return the number of elements in the queue
    
    def printqueue(self):
        result = list()
        if self.queue == 0:  # check if the queue is empty
            return "Queue is Empty"
        else:
            for i in self.queue:
                result.append(i)
            return result  # return the elements of the queue as a list
    def remove(self):
        if self.queue==0:
            return ("Queue is empty ")
        else:
            self.queue.pop()    
#Create object of queue
obj=Queue()
obj.addelement(1)
obj.addelement(2)
obj.addelement(3)
obj.addelement(4)

print("Size of Queue:",obj.size())

print("Orignal Queue: ",obj.printqueue())
obj.remove()
obj.remove()
print("After Poped element from Queue: ",obj.printqueue())