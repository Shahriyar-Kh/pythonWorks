#Print hello world!
print("Hello world!")
x=-2
if x < 2 :
    print('Below 2')
elif x >= 2 :
     print('Two or more')
else :
    print('Something else')

x = 0
if x < 2 :
    print('Small')
elif x < 10 :
    print('Medium')
else :
    print('LARGE')
print('All done')


astr = 'Hello Bob'
#istr = int(astr)
#print('First', istr)
astr = '123'
istr = int(astr)
print('Second', istr)

astr = 'Hello Bob'
istr = 0
try:
    istr = int(astr)
except:
    istr = -1
    print(istr)
