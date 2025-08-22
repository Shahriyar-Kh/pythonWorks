import collections
doubleEnded=collections.deque([4,5,6,7])
doubleEnded.append(8)
print("8 Appended at Right :",doubleEnded)

doubleEnded.appendleft(3)
print("3 is Appeded at left:",doubleEnded)

doubleEnded.pop()
print("Item Deleted from right: ",doubleEnded)

doubleEnded.popleft()
print("Item deleting from left: ",doubleEnded)

