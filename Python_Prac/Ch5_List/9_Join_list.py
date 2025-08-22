#Example 1 (+) used for joined two list
list1=[10,20,30,40,50,60] 
list2=["Khan","Umair","Ali"]
list3=list1+list2
print("Joined List1(+): ",list3)

#Example 2  use the augmented concatenation operator with "+=" symbol to append L2 to L1

#the above joined also
list1+=list2
print("\nJoined List2(+=): ",list1)

#Also using Extend() method
list2.extend(list1)
print("\nJoined List3(Extend): \n",list2)

#Using append() method to joined two lists

list5=[1,2,3,4,5]
list6=['one','two','three','four','five']

for x in list6:
    list5.append(x)
    
print("Joined list (append): ",list5)
