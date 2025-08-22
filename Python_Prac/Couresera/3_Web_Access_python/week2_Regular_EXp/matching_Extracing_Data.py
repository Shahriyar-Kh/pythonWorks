

#Matching and Extracting Data part 2
#Example 1 
print("\n\n************* Matching and Extracting *************** ")
import re
x="My 2 favorite numbers are 19 and 42 "
y=re.findall('[0-9]+',x)  #  + reg  >=1 mean one or more digits
print(y)

y2=re.findall('[aeoui]+',x)
print(y2)
y3=re.findall('[AEOUI]+',x)
print(y3)


print("\n\n**************** Warnning : Greedy Matching ****************")
#Example 2 Warnning : Greedy Matching
x2="From: using the : Character"
y4=re.findall('^F.+:',x2)
print(y4)

print("\n\n**************** No Greedy Matching ****************")
#Example 3 No Greedy Matching
gr=re.findall('^F.+?:',x2)
print(gr)

print("\n\n**************** Fine Tuning String Extraction ****************")
#Example 4 Fine Tuning String Extraction
file="My email address shahriyarkhanpk1@gmail.com 12:12:2024 to 2050"
find=re.findall('\S+@\S+',file)
print(find)

# paranthesis are not part of the match ,but they tell where to start and stop what string to extract
find2=re.findall('^address (\S+@\S+)',file)
print(find2)

print("\n\n**************** Double Split pattern  ****************")
#Example 4 Double Split pattern
words=file.split()
print(words)
email=words[3]
print(email)
pieces=email.split('@')
print(pieces)


print("\n\n**************** RegExp Version  ****************")
#Example 5 RegEXp Version
find3=re.findall('@([^ ]*)',file)
print(find3)

print("\n\n**************** Even Cooler RegExp Version  ****************")
#Example 6  Even Cooler RegEXp Version

find4=re.findall('^address .*@([^ ]*)',file)
print(find4)