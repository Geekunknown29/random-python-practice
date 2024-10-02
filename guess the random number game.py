#number guessing game
def draw():
    if flag == 0 :
        x = """ __________+
               ?         !
               |         |
               |         !
               |         !
                         !
                         |
                         /
                         !
                         !
                         !
                         !
                         1
                         !
                         !
                     ////!\\\\
                   //||||!|||||\\\
                 //////!!!!!\\\\\\\\"""
                   

    print(x)

import random as rand

num = rand.randint(0,10)


print ("guess a number in range of 0 to 10^50")



flag = 0
while flag <= 6 :
    inp = int(input("your guess : "))
    flag += 1
    draw()
    
    if inp == num :
        print("congo")
        print('numbr was : ', num , 'your answer was : ', inp)
        break

    elif inp-num in range (-10,10):
        print ("very close")
    else :
        print ("better luck next time !!!")


