d= int(input ('A'))
def I():
    i = int(input ('value of i'))
    if i > d:
        I()
    elif i==d :
        return max(i)
        
I()


