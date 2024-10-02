a=int(input('write a no.   a'))
b=int(input('write a no.   b'  ))
c=int(input('write a no.   c'))
if a>b and  c<b:
    print ("a is largest")
elif a>b and b>c:
    print ("a is largest")
elif a>c and c>b:
     print("a is largest")

elif b>c and  a<c:
    print ("b is  largest")
elif b>c and c>a :
    print ("b is largest")
elif b>a and a>c:
     print("b is largest")
     
elif c>b  and a<b :
    print ("c is largest")
elif c>b and b>a:
    print ("c is largest")
elif c>a and a>b:
    print ("c is largest")

elif a==b and b<c:
    print ("c is largest")
elif a==b and b>c:
    print ("a and b are largest")    
elif a==c and b>c :
    print ("b is largest")
elif a==c and b<c :
    print ("a and c are largest")    
elif b==c and a>b:
    print ("a is largest")
elif b==c and a<b:
    print ("b and c are largest")     

else:
    print("all three no. are same")      
