#Example 1 Creating a Heap
import heapq
l1=[21,1,45,78,3,5]
#Use heapify to rearrange the elements
print("\n\n*********************** Creating heap *****************")
print("Orignal list: ",l1)
heapq.heapify(l1)
print("After Heap list:",l1)

#Example 2 Inserting into heap
"""
Inserting a data element to a heap always adds the element at the last index. 
But you can apply heapify function again to bring the newly added element to the first index only if it smallest in value. 
In the below example we insert the number 8."""
print("\n\n ******************************** Inserting in Heap ***********************")


#Add element to above heaplist
heapq.heappush(l1,8)
print("\nAfter inserting 8 in Heap: ",l1)
heapq.heappush(l1,0)
print("\nAfter inserting 0 in Heap: ",l1)

#Example 3 Removing from heap
"""
You can remove the element at first index by using this function. 
In the below example the function will always remove the element at the index position 1."""

print("\n\n*************************** Removing from heap *********************")
#Remove element from the heap
heapq.heappop(l1)
print("\nAfter removing  from heap:",l1)
heapq.heappop(l1)
print("\nAfter removing  from heap:",l1)

#Example 4 Replacing in a Heap
"""
The heap replace function always removes the smallest element of the heap 
and inserts the new incoming element at some place not fixed by any order."""
print("\n\n********************* Replacing in heap*******************")

#Replace an element 
heapq.heapreplace(l1,20)
print("\nAfter replacing (20): ",l1)
heapq.heapreplace(l1,40)
print("\nAfter replacing (40): ",l1)