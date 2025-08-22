#Example 1 open file 
fo=open("foo.txt",'wb')
print("Name of the file: ",fo.name)
print("Closed or not: ",fo.closed)
print("Opinning mode: ",fo.mode)
fo.close()