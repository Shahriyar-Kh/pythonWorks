import re
x="From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"

find=re.findall('@(\S+)',x)
print(find)

find2=re.findall('[a-z0-9]',x)
print(find2)

find3=re.findall('\S+?@\S+',x)
print(find3)