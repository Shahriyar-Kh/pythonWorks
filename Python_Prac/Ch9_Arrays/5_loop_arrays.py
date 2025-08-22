import array as arr
a=arr.array('d',[1,2,3,4,5])
l=len(a)#length of array
idx=0
while idx<l:
    print(a[idx])
    idx+=1
    
print("\n")
#"for Loop with Array I ndex
l1=len(a)
for i in range(l1):
    print(a[i])
    
#You will get the same output as in the first example.   


