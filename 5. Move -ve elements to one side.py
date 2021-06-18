#Move all the negative elements to one side
a = [-1, 2, -3, 4, 5, 6, -7, 8, 9]



print(a)

def negativeSort(a):
    left = 0
    right = len(a) -1
    while left <= right:
        if a[left] < 0 and a[right] < 0:
            left += 1
            
            
        elif a[left] > 0 and  a[right] < 0:
            a[left],a[right] = a[right],a[left]
            left +1 
            right -=1
            
        elif a[left] < 0 and a[right] > 0:
            right -= 1
            
        else:
            left+=1
            right-=1
    return a
    
print(negativeSort(a))

'''
#method 2 using partition algorithm
i = -1
pivot=0
for j in range(len(a)):
    if a[j] < pivot:
        i+=1
        a[i],a[j] = a[j],a[i]
print(a)
    ''' 
    
'''output:
[-1, 2, -3, 4, 5, 6, -7, 8, 9]
[-1, -7, -3, 4, 5, 6, 2, 8, 9]'''
    

