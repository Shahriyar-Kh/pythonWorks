"""
6.5 Write code using find() and string slicing (see section 6.10) 
to extract the number at the end of the line below. 
Convert the extracted value to a floating point number and print it out.
"""
text = "X-DSPAM-Confidence:    0.8475"
#finde the position for start
pos=text.find("0")
#Slicing to get number end of line
numS=text[pos:]
#convert to float
print(float(numS))