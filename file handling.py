
a= open(input ('file name:'),'r') # used to open a file in python program
k=a.read()
print(k)
a.close()
b= open(input('file name b'),'r')
for i in b :
    print (i)

a= open(input('file name'),'a')
a.write('hello guys') # a.write('hello guys')io.UnsupportedOperation: not writable
a.close
print (a.read())
a.close()

'''
f= open('modules.py')
p= f.read()
k=f.write ('hi friends')
print (p)
print (k)
'''
'''
a = open(input('Enter file name:'), 'r')  # Open the file in read mode
k = a.read()
print(k)

b = open(input('Enter another file name:'), 'r')  # Open the second file in read mode
for i in b:
    print(i)

a.close()  # Close the files after you're done reading them

a = open(input('Enter file name:'), 'a')  # Open the first file in append mode
a.write('hello guys')
a.close()  # Close the file after writing to it
'''
