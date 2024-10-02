a= 'hello_world'
print(a[1:3])
"""
f = open ("alpha.txt",'r')
data = f.readlines()
    
for i in data:
    sp= i.split()
    if sp[0] == 'you':
      print(i)
        
f.close()
"""
"""
 import statistics as s
l=[11,24,32,45,11]


print ('median:',s.median(l))
print ('mode:',s.mode(l))
"""
"""
l= [1,2,4,5]
l.insert(2,200)
print (l)
message = 'hello how re you?.'
print (message.endswith('.'))"""
"""s= 'LOST'
L = [10,21,33,4]
D = {}
for I in range (len(s)):
    if I%2 == 0:
        D[L.pop()]=s[I]

    else :
        D[L.pop()]= I+3
for k,v in D.items():
    print (k,v,sep='*')
    print (D)
"""        
"""m = open('text.txt','r')
f= m.read()
s=len(f)
print('size=',s)
m.close()
f=f.rstrip()
"""
"""
import random 
num = random.randint(0,3)
col = ['y','w','b','r']
for i in range (1,num):
    print(col[i],end='* ')
    print()
for i in range(1,3):
    print(i)
"""
"""
def fun():
    string = "come let us have some fun"
    t= ()
    s= string.split()
    for i in s:
        l=len(i)
        t=t+(l,)
        return t
        print (t)
fun()

l= []
x= input("enter your value ")
l.append(x)
print(l)
"""
