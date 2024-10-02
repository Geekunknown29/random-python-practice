def bubblesort():
    for i in range(len(arr)) :
        for j in range(len(arr)) :
            if arr[i] > arr[j] :
                [arr[j], arr[i]] =[arr[i],arr[j]]
    x = input("ascending or descending ? ")
    if x == 'a':
        print (arr[::-1])
    else :
        print(arr)


arr = [2,5,3,6,4,7,6,8,432,65,78,8]



bubblesort()
