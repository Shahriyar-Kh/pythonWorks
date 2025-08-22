#EXample 1 Creating metrix
import numpy as np
a=np.array([['Mon',5,10,15,20],['Tue',5,10,15,20],['Wed',5,10,15,20]])
print(a)
a1=np.reshape(a,(3,5))

#Example2 Accessing the items
print(a[0])
print(a[0][1])

#Example 3 adding row
a2=np.append(a,[["Tu",5,10,15,20]],0)
print(a2)

#Example4 adding a column
a3=np.insert(a2,[5],[[25],[25],[25],[25]],1)
print(a3)

#Example 5 delete a row
"""We can delete a row from a matrix using the delete() method. We have to specify the index of the row and also the axis value which is 0 for a row and 1 for a column."""
d=np.delete(a3,[3],0)
print('\n',d)

#Example 6 delete a column 
a4=np.delete(a3,[5],1)
print(a4)

#Example 7 Update a row
"""
To update the values in the row of a matrix we simply re-assign the values at the index of the row. In the below example all the values for thrusday's data is marked as zero. The index for this row is 3."""
a3[3]=['TUe',0,0,0,0,0]
print(a3)