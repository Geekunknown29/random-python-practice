
import math
A = float (input('give any FLOAT value to A'))
B = float (input('give any FLOAT value to B'))
C = int(input ('INTEGER for rounding off upto certain digit'))
print ("click enter and then i for operators availble or click n if you dont want")
Z= input('n or i')

if Z=='i' :
       print ("operators availible as of now are:-''1 +' , '2 -' , '3 /' , '4 *' , '5 power', '6 round off")


O= input ('choose desired operator ')


def cal(A,B,C):
    if O=='+' :
      print('A+B is ',A+B, sep='=')
    elif O=='-':  
        print('A-B is',A-B, sep='=')
    elif O=='/' :
        print('A/B  is',A/B, sep='=')
    elif O =='*' :
        print('A*B',A*B, sep='=')
    elif O== 'pow(A,B)':
        print ('A raised to power B is',pow(A,B), sep='=')
    elif O== 'sqrt' :
        print ('square root of desired number is',math.sqrt(A or B),sep='=')
    elif O == 'round off' :
        print ('round off of A upto C digits is', round(A,C), sep='=')
  
cal(A,B,C)
 



