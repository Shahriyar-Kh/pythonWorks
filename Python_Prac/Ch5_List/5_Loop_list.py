#Example 1
list1=[1,2,3,4,7,6,5]
for num in list1:
    print(num,end=' ')
    
#Example 2
""" 
To iterate through the items in a list, obtain the range object of integers "0" to "len-1"""  

list2=[5,10,15,20,25]
indexes=range(len(list2))
for i in indexes:
    print(f"List[{i}]: {list2[i]}")