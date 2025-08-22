# 10.2 Python - Read Files
"""
To programmatically read data from a file using Python, it must be opened first. Use the built-in open() function 
These two statements are identica
 
"""
fo4=open("foo.txt","r")
fo4=open("foo.txt")

#Example 1
#Open a file
fo1=open("foo.txt","r")
print("Read the foo file: ",fo1.read())
#close file
fo1.close()

#10.2.1 Reading in Binary Mode
"""
By default, read/write operation on a file object are performed on text string data. 
If we want to handle files of different other types such as media (mp3), executables (exe), 
pictures (jpg) etc., we need to add 'b' prefix to read/write mode.

Assuming that the test.bin file has already been written with binary mode
    """
fo2=open("test.bin","rb")
print("Read the test.bin  file: ",fo2.read())
fo2.close()
#Output: b'Hello word'
    
"""
We need to use 'rb' mode to read binary file. Returned value of read() method is first decoded before printing
    """
#the above code also writen
fo3=open("test.bin","rb")
data2=fo3.read()
print(data.decode(encoding='utf-8'))
#Output: Hello word

#10.2.3 Read Integer Data from F ile
"In order to write integer data in a binary file, the integer object should be converted to bytes by to_bytes() method."""
n=23
n.to_bytes(8,'big')#n.to_bytes(8, 'big'): This method converts the integer n to a bytes object of length 8 (using 8 bytes) and specifies the byte order as 'big endian' (most significant byte first). The result is stored in the variable data.
fo4=open('test.bin',"wb")#Opens the file 'test.bin' in binary write mode
data=n.to_bytes(8,"big")
fo4.write(data)# Writes the bytes data to the binary file.
fo4.close()

"""To read back from a binary file, convert the output of read() function to integer by using the from_bytes() function."""
fo5=open('test.bin','rb')
data=fo5.read()

n=int.from_bytes(data,"big")#Converts the bytes data back to an integer. 
#The 'big' parameter indicates the byte order, specifying 'big endian'.
print(n)
fo5.close()

#important point
"""
he term "big" refers to the byte order, specifically "big endian." Endianness refers to the order in which bytes are stored in computer memory. In 'big endian
big:  ' the most significant byte (the one with the highest value) is stored at the lowest memory address.
little:  The alternative is 'little endian,' where the least significant byte is stored at the lowest memory address.
"""

#10.2.4 Read Float Data from File
"""
For floating point data, we need to use struct module from Python's standard library."""

import struct
x=23.4
data3=struct.pack('f',x)#This function packs the floating-point number x into a bytes object using the format specifier 'f' (indicating a 4-byte float).  
                                    #The result is stored in the variable data3."""
fo6=open('test2.bin','wb')
fo6.write(data3) # Writes the packed binary data to the file.
fo6.close()

"""Unpacking the string from read() function to retrieve the float data from binary file."""
fo7=open('test2.bin','rb')
data4=fo7.read()
x=struct.unpack('f',data4)#Unpacks the binary data using the format
print(x)

#10.2.5  Using the r+ M ode
"""
When a file is opened for reading (with 'r' or 'rb'), it is not possible to write data in it. 
We need to close the file before doing other operation. 
In order to perform both operations simultaneously, we have to add '+' character in the mode parameter. 
Hence 'w+' or 'r+' mode enables using write() as well as read() methods without closing a file."""
#Example 1
"""This program opens the file in w+ mode (which is a read-write mode), adds some data. The it seeks a certain position in file and overwrites its earlier contents with new text."""
fo8=open('foo.txt','r+')
fo8.seek(6,0)#it means start reading from 7 char and read total 11 char
data5=fo8.read(11)
print(data5)
fo8.close()

#Example 2 
#open a file in read write mode
""" Opens the file 'foo1.txt' in write mode with the ability to read ('w+'). If the file does not exist, it will be created. If it does exist, its contents will be truncated."""
fo9=open('foo1.txt','w+') 
fo9.write("This is rat race")#Write the string to the file
fo9.seek(8,0)#Moves the file cursor to the 8th byte from the beginning of the file (absolute seek).
data61=fo9.read(3)#Reads 3 bytes of data starting from the current file cursor position and stores it in the variable data61.
print(data61)
fo9.seek(8,0)#Moves the file cursor back to the 8th byte from the beginning of the file.
fo9.write('cat')
fo9.seek(0,0)#Moves the file cursor to the beginning of the file.
data6=fo9.read()#Reads the entire content of the file and stores it in the variable data6.
print(data6)
fo9.close()

