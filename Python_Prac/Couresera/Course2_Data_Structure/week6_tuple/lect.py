#the top 10 most common name
fname=open("romeo.txt")
counts={}
for line in fname:
    words=line.split()
    for word in words:
        counts[word]=counts.get(word,0)+1
lst=list()
for k,v in counts.items():
    newtup=(v,k)
    lst.append(newtup)
# print("list",lst)
lst1=sorted(lst,reverse=True)
# print("Sorted list: ",lst1)
for v,k in lst1[:10]:
     print(k,v)
     
#Even shorted version 
# for k,v in counts.items():
#     newtup=(v,k)
#     lst.append(newtup)
# # print("list",lst)
# lst1=sorted(lst,reverse=True)
#list comprehension same as
lst2=sorted([(v,k) for k,v in counts.items()])
print("list2: ",lst2[:10])

x,y=2,4
print(y)

a=(3,1,4)
b=(2,10,13)
if b>a:
    print("YEs")
else:
    print("no")