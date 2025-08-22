import re
file=open(r"E:\Python_Prac\Couresera\3_Web_Access_python\week2_Regular_EXp\regex3.txt")
read=file.read()
find=re.findall(r'[0-9]+',read)
total_sum=sum(map(int,find))
print(total_sum)
