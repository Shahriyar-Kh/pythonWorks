"""
7.1 Write a program that prompts for a file name, 
then opens that file and reads through the file,
and print the contents of the file in upper case. 
Use the file words.txt to produce the output below.

    """


#Using the word.txt file from user to promp file name 
fname=input("Please Enter the file nam e: ")
#concat the filepath with filename
#Open the file for reading
fileh=open(fname)
#read the whole file
fr=fileh.read()
fstrip=fr.strip()
#convert the file to upper case
print(fstrip.upper()) 



