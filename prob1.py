a = "(abcd)"
j = a[::-1]
print (j)
for i in j:
    if j == "(" or ")" :
        del(i)

    else :
        print (i)
