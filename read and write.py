a = open(input('Enter file name:'), 'r')  # Open the file in read mode
k = a.read()
print(k)

#b = open(input('Enter another file name:'), 'r')  # Open the second file in read mode
#for i in b:
  #  print(i)

a.close()  # Close the files after you're done reading them

a = open(input('Enter file name:'), 'r+')  # Open the first file in append mode
a.write('3hello guys')
a.close()  # Close the file after writing to it
