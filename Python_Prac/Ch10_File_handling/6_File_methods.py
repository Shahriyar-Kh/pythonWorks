#EXample 1 fileno() method
# Open a file
fo = open("fo.txt", "wb")
print ("Name of the file: ", fo.name)
fid = fo.fileno()
print ("File Descriptor: ", fid)

# Close the opened file
fo.close()

#EXample 2 isatty() method
"""The method isatty() returns True if the file is connected 
(is associated with a terminal device) to a tty(-like) device, else False."""
# Open a file
fo = open("foo.txt", "wb")
print ("Name of the file: ", fo.name)
ret = fo.isatty()
print ("Return value : ", ret)

# Close the opened file
fo.close()
