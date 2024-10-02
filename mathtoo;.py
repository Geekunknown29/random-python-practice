pi=22/7
import math

print ("which operation do you want to perform:-''1 +' , '2 -' , '3 /' , '4 *' , '5 power', '6 square root','7 round off','8 area of circle','9 factorial'")





 
# C = int(input ('INTEGER for rounding off upto certain digit or enter 0 if not rounding off'))

O= input ('choose desired operator ')
#print(A,O,B)

#elif w=='area of circle':
   #  R= float (input('radius of circle ?'))
   #  print('area of circle is =', pi*R*R)
     

def cal():
       if O=='1' :
         A = float(input('give any FLOAT value to A'))
         B = float(input('give any FLOAT value to B'))
         print('A+B is ',A+B, sep='=')
       elif O=='2':
         A = float(input('give any FLOAT value to A'))
         B = float(input('give any FLOAT value to B'))
         print('A-B is',A-B, sep='=')
       elif O=='3' :
         A = float (input('give any FLOAT value to A'))
         B = float (input('give any FLOAT value to B'))
         print('A/B  is',A/B, sep='=')
       elif O =='4' :
         A = float (input('give any FLOAT value to A'))
         B = float (input('give any FLOAT value to B'))
         print('A*B',A*B, sep='=')
       elif O== '5':
          A = float (input('give any FLOAT value to A'))
          B = flo
          at (input('give any FLOAT value to B'))
          print ('A raised to power B is',pow(A,B), sep='=')
       elif O== '6' :
          A = float (input('give any FLOAT value to A'))
          print ('square root of desired number is',math.sqrt(A or B),sep='=')
       elif O == '7' :
          A = float (input('give any FLOAT value to A'))
          C = int(input ('INTEGER for rounding off upto certain digit'))
          print ('round off of A upto C digits is', round(A,C), sep='=')
       elif O== '8':
           R= float (input('radius of circle ?'))
           print ('area of circle', pi*R*R, sep='=')
       elif O=='9':
           A= int(input ('no.?'))
           print (math.factorial(A))
cal()

