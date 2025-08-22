# 10 .1 Python - Write to File
# open a file
fo=open("foo.txt","w")
fo.write("Python is a great language.\nYeah its great!!\n")
#Close file
fo.close()

# 10.1.2 Writing in Binary Mode

"""
By default, read/write operation on a file object are performed on text string data. 
If we want to handle files of different other types such as media (mp3), executables (exe), 
pictures (jpg) etc., we need to add 'b' prefix to read/write mode.

Following statement will convert a string to bytes and write in a file.
"""
f=open("test.bin","wb")
data=(b"Hello word") #b is for Opens the file in binary mode
f.write(data)
f.close()
"""Conversion of text string to bytes is also possible using encode() function."""
data1='Hello word'.encode('utf-8')
print(data1)

#10.1.3  Appending to a File
"""
When any existing file is opened in 'w' mode to store additional text, its earlier contents are erased. 
Whenever a file is opened with write permission, it is treated as if it is a new file.
To add data to an existing file, use 'a' for append mode.

"""
#Open a file in append mode
append_f=open("foo.txt","a")
text="TutorialPoint has a fabulous python tutorial"
append_f.write(text)
#close file 
append_f.close()

# 10.1.4 Using the w+ Mode
"""
When a file is opened for writing (with 'w' or 'a'), 
it is not possible to perform write operation at any earlier byte position in the file. 
Th 'w+' mode enables using write() as well as read() methods without closing a file. 
The File object supports seek() unction to rewind the stream to any desired byte position.
"""
#Open a file in read write mode
# fo3=open("foo.txt","w+")
# fo3.write("This is a rat race")
"""
Parameters
offset : This is the position of the read/write pointer within the file.
whence : This is optional and defaults to 0 which means absolute file positioning, 
other values are 1 which means seek relative to the current position and 2 means seek relative to the file's end.
    """
# fo3.seek(10,0)#offset 10 and whence 0
# data=fo3.read(3)
# fo3.seek(10,0)#seek() method to show how simultaneous read/write operation on a file can be done.
# fo3.write('cat')
# fo3.close()
