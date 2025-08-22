#Example 1 Rename the file name
"""
Following is an example to rename an existing file "test1.txt" to "test2.txt" −"""
#Python os module provides methods that help you perform file-processing operations, such as renaming and deleting files.

import os 
#Rename a file test1.txt to test2.txt
#os.rename("test.bin","test1.bin")#First run chang file second run errur

#Example 2 Remove file
"""
remove() Method
You can use the remove() method to delete files by supplying the name of the file to be deleted as the argument."""
import os 
os.remove('test2.bin')
