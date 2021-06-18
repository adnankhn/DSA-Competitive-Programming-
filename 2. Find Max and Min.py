#Find max and min
a = [0,2,3,5,6,7]
'''
def maxmin(a):
    a.sort()
    min = a[0]
    max = a[-1]
    return min,max
    
print(maxmin(a))
'''

def maxmin(a):
    min = a[0]
    max = a[1]
    
    
    for i in range(1,len(a)):
        if a[i] < min:
            min = a[i]
            
        elif a[i] > min:
            max = a[i]
            
    return print("Max =",max,"Min =",min)
    
maxmin(a)
