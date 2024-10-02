def m ():
    yield "hello"
    yield 51
    yield "line"
    
x = m()
print (x)

for i in x:
    print (i)
