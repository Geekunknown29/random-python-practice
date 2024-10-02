"""
try:
    a= int(input ("denominator ___ = "))
    answer = 3/a
    print (answer)


except:
    answer = 0/3
    print (answer)
    print("you can not have zero as a denominator")
    """



try :
    name = input("name")
    assert name != "dog", name_ERROR
    print (name)

except name_ERROR :
    print("name cannot be dog")
    print(f"entered name = {name}")
    
    
