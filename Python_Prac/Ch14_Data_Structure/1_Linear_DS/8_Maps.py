import collections
d1={'Day1':'Mon','Day2':'Tuesday','Day3':'Wed'}
d2={'Day4':'Thrusday','Day1':'Friday'}

res=collections.ChainMap(d1,d2)

#Creating a single dict
print(res.maps,'\n')

print("keys={}".format(list(res.keys())))
print("Values={}".format(list(res.values())))

#Print all elements from the results
print("Elements: ")
for key, value in res.items():
    print('{}={}'.format(key,value))

#find a specific value in the results
print("Day1 in res: {}".format('Day1' in res))

#Example 2 Map Reordering

"""
If we change the order the dictionaries while clubbing them in the above example we see that the position of the elements get interchanged as if they are in a continuous chain. This again shows the behavior of Maps as stacks."""

res1=collections.ChainMap(d1,d2)
print(res1.maps,'\n')
res2=collections.ChainMap(d2,d1)
print(res2.maps,'\n')


#Example 3 Updating Map
"""
When the element of the dictionary is updated, the result is instantly updated in the result of the ChainMap. In the below example we see that the new updated value reflects in the result without explicitly applying the ChainMap method again."""
d2['Day4']='Sunday'
print(res2.maps,'\n')