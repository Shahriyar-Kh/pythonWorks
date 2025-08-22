"""
7.2 Write a program that prompts for a file name, 
then opens that file and reads through the file, 
looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values 
from each of the lines and compute the average of those values and produce an output as shown below. 
Do not use the sum() function or a variable named sum in your solution.
You can download the sample data at http://www.py4e.com/code3/mbox-short.txt 
when you are testing below enter mbox-short.txt as the file name.

    """
fname=input("Enter the filename: ")
fo=open(fname)
count=0
t_c_v=0
for line in fo:
    if line.startswith("X-DSPAM-Confidence:"):
       count+=1
       pos=(line.find(':'))
       C_values=float(line[pos+1:])
       t_c_v+=C_values
       
if count>0:
    avg=t_c_v/count
    print(avg)
fo.close()

#Second method
# Use the file name mbox-short.txt as the file name
fname = input("Enter the filename: ")

try:
    fo = open(fname)
    count = 0
    total_confidence = 0

    for line in fo:
        if line.startswith("X-DSPAM-Confidence:"):
            count += 1
            # Fix the syntax error in the following line
            # Use [-1] to get the last element after splitting by ":"
            C_values = float(line.split(":")[-1].strip())
            total_confidence += C_values

    if count > 0:
        average_confidence = total_confidence / count
        print(f"Count: {count}")
        print(f"Average spam confidence: {average_confidence:.4f}")
    else:
        print("No lines starting with 'X-DSPAM-Confidence:' found in the file.")

    fo.close()

except FileNotFoundError:
    print(f"File '{fname}' not found. Please make sure the file exists.")
except Exception as e:
    print(f"An error occurred: {e}")
