
import math

print ("operators availible as of now are:-''1 +' , '2 -' , '3 /' , '4 *' , '5 power','6 square root ' ,'7 round off', '8 factorial c'")

O= input ('choose desired operator ')

if O=='+' or O=='-' or O== '/' or O== '*' :
       A = float (input('give any FLOAT value to A'))
       B = float (input('give any FLOAT value to B'))
elif O=='factorial' :
       C = int(input (' factorial of = '))
elif O=='round off' :
       K= float(input('number you want to round off='))
       L= int (input('digit upto which youu want to round off? ='))
elif O== 'square root':
       S=float (input ('no.? ='))


#print(A,O,B)



def cal():
       if O=='+' :
              print('A+B is ',A+B, sep='=')
       elif O=='-':
              print('A-B is',A-B, sep='=')
       elif O=='/' :
              if not B=='0':
                print('A/B  is',A/B, sep='=')
       elif O =='*' :
              print('A*B',A*B, sep='=')
       elif O== 'pow(A,B)':
              print ('A raised to power B is',pow(A,B), sep='=')
       elif O== 'square root' :
              print ('square root of desired number is',math.sqrt(S),sep='=')
       elif O == 'round off' :
              print ('round off of K upto L digits is', round(K,L), sep='=')
       elif O== 'factorial':
              print (math.factorial(C ))

cal()
