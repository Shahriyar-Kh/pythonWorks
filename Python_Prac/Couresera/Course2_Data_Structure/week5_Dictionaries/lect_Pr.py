#Empty dic
#Comparing list and Dict
purse=dict()
purse['money']=12
purse['candy']=3
purse['tissue']=78
print(purse)
print(purse['candy'])
purse['candy']=purse['candy']+2
print(purse)

list1=list()
list1.append(1)
list1.append(2)
list1.append(3)
list1.append(4)
print(list1)
list1[0]=10
print(list1)

#Lect 2 Most Common Name?
counts={}
names=['csev','cwen','csev','cwen','cwen','Khan ']
for name in names:
    if name not in counts:
        counts[name]=1
    else:
        counts[name]=counts[name]+1
print(counts)

#The get method for dict
if name in counts:
    x=counts[name]
else:
    x=0
x=counts.get(name,0)

#simplified Counting with get()
counts2={}
for name in names:
    counts2[name]=counts2.get(name,0)+1
print(counts2)

#Counting pattren 
counts3={}
text=input('Input a line of text: ')
words=text.split()
print("Words:",words)

print("Counting....")
for word in words:
    if word not in counts3:
        counts3[word]=counts3.get(word,0)+1
print("Counts3: ",counts3)

#Counting my name letter repeated
letters=[]
counts4={}
for word in text:
    word.split()
    letters.append(word)
print("List: ",letters)
for letter in letters:
    #also same worked
    # if letter not in counts4:
    #     counts4[letter]=1
    # else:
    #    counts4[letter]=counts4[letter]+1
       counts4[letter]=counts4.get(letter,0) + 1
print("Counts: ",counts4)


#Definite loop and dict
#dict or not sorted in order so for this we used for loop
dict1={"khan":3,"umair":5,"Ali":6}
print(list(dict1)) #print list of keys
print(dict1.keys())# also list of keys 
print(dict1.values()) #print list of values
print(dict1.items())# print list of tuple 

#Two iteration variables
for a,b in dict1.items():
    print(a,b)# a=keys and b =values
    
