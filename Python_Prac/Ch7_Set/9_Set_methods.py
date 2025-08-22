#Example 1 Add()
s1={1,2,3,4}
s1.add(5)
s1.add("khan")
s11=(6,7)
s1.add(s11)
print("Added set: ",s1)

#Example 2 clear() Remove all elements from this set.
s1.clear()
print("Set: ",s1)

#Example 3 discard() Remove an element from a set if it is a member.
s2={2,4,5,6,8}
s2.discard(8)
print("Set: ",s2)

#Example 4 isdisjoint()
s1={1,2,3,4}
s2={5,6,2}
s3=s1.isdisjoint(s2)
print(f"{s1} is {s2}:{s3} ")

#Example 5 issubset()
s5=s1.issubset(s2)
print(f"{s1} issubset {s2}:{s5} ")

#Example 6 pop() Remove and return an arbitrary set element
s9=s2.pop()
print("Poped Element: ",s9)#deleted 2

#Example 7 remove() Remove an element from a set; it must be a member.
s10=s1.remove(1)
print("Set: ",s10)


