#Python - String Exercises
#Example 1
"""Python program to find number of vowels in a given string."""
mystr="i am living in peshawer! and i am studying in abasyn university And STUDENT "
lvowels="aeiou"
cVowels="AEIOU"
count1=0
count2=0

for x in mystr:
    if x in lvowels:#best is if x.lower() in lvowels:
        count1+=1
    elif x in cVowels:
        count2+=1
    else:
        print("Other")
print("Number of vowels in lower case: ",count1)
print("Number of vowels in capital: ",count2)

#Example 2
"""Python program to convert a string with binary digits to integer."""
string="10101"
#Method 1 short 
print(int(string,2))

#Method 2 by function
# Define a function named 'strtoint' that takes a binary string as input
def strtoint(string):
    # Iterate through each character in the string
    for x in string:
        # Check if the character is not '0' or '1'
        if x not in '01':
            # If any character is not '0' or '1', return an error message
            return "Error. String with non-binary characters"
    
    # Convert the binary string to an integer
    num = int(string, 2)
    
    # Return the resulting integer
    return num

# Example binary string
string = "110110"

# Print the binary string and the result of the strtoint function
print(f"Binary: {string} Integer: {strtoint(string)}")

#Example 3
"""Python program to drop all digits from a string."""
#1 Create a list of digits
digits=[str(x) for x in range(10)]
print(digits)#['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

#2 initialize variables
mystr="He12llo, Py00th55on!"#input string
chars=[]#empty list store non digit character

#3 Iterate through each character
for x in mystr:
    #Check for non digit ch
    if x not in digits:
     
     #append non digit ch to list
     chars.append(x)
    
#Join the ch in the 'chars list to form a new string
newStr=''.join(chars)

#print string without digit
print(newStr)
    
#Example 4
"""Python program to find number of words in a string"""    
name="shahriyar khan"
print(f"Total numbers of words in \n {name} : ",len(name))

#Example 5
"""Python program to sort the characters in a string """
#method 1 using list and sort method

#Convert to list
list1=list(name)
print("List:",list1)
#Sort the list
list1.sort()
print("Sorted list",list1)
#convert list to string
str1=''.join(list1)
print(str1)

#Mtheod 2 using sorted() function
def stringsort(input_str):
    sorted_str=''.join(sorted(input_str))
    return sorted_str

input_str="yxzfdhfskabcd"
result=stringsort(input_str)
print("Orignal string: ",input_str)
print("Sorted String: ",result)

#Example Python program to remove duplicate characters from a string

#Method 1 in simple
inputStr="Shahriyar khan"

#empty set store unique characters
u_chars=set()

#empty string result without dulication
result_Ch=''

#iterate each character in the input string
for char in inputStr:
    #check ch is not in set u_ch
    if char not in u_chars:
        #if ch not in set add it in set
        u_chars.add(char)
        #also append ch to result string
        result_Ch+=char
print("Orignal String: ",inputStr)
print("Duplicate String: ",u_chars)
print("With out duplicate Strings: ",result_Ch)
print("\n\n")

#Method 2 using orderdict (Preserving order)

#import the orderDict class from the collection modulse
from collections import OrderedDict
#create function for R_duplicates

def R_duplicates(a):
    #use orderdict to create dictionary with unique keys
    U_set=OrderedDict.fromkeys(a)
    print("unique set: ",U_set)
    result_Ch=''.join(U_set)
    #return final result without duplicates
    
    return result_Ch
inputStr="\nAbasyn university"
result_Char=R_duplicates(inputStr)
print("Origna String: ",inputStr)
print("String without duplicates: ",result_Char)

#Example Python program to list unique characters with their count in a string

inputStr="Hello word!"
u_set=set()
result=''

for char in inputStr:
    if char not in u_set:
        u_set.add(char)
        result+=char
print(f"\nTotal number of String in {inputStr}: {len(inputStr)}")
print(f"Total number of unique character in string {inputStr}: {len(result)}")

