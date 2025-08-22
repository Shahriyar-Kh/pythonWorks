# 10.4.1 mkdir() method
#Example 1 
"""Following is an example to create a directory test in the current directory −"""
import os
#Create a directory "test"
#os.mkdir("test1")

#10.4.2 The chdir() Method
"""
You can use the chdir() method to change the current directory. 
The chdir() method takes an argument, which is the name of the directory that you want to make the current directory."""

#Example 2 
"""
Following is an example to go into "/home/newdir" directory −"""
import os 
#Create a directory to "/home/newdir"
os.chdir("E:\DCIM")

#10.4.3The getcwd() Method
"""The getcwd() method displays the current working directory."""
#Example 3
"""Following is an example to give current directory """
Current_Dir=os.getcwd()
print("current working directory :",Current_Dir )

#10.4.4 The rmdir() Method
"""
The rmdir() method deletes the directory, which is passed as an argument in the method.

Before removing a directory, all the contents in it should be removed."""

#Example 4
"""Following is an example to remove the "/tmp/test" directory."""
#os.rmdir("test")

#List Directories and Files in Python
list_Dir=os.listdir(Current_Dir)
print(list_Dir)
#Also
print(os.listdir("E:\\"))

