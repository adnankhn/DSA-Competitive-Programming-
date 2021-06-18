#Reverse a list
a = [1,2,3,4,5]

def rever(a):
    first = 0
    last = len(a) -1
    
    while (first < last):
        print(a)
        a[first],a[last] = a[last],a[first]
        first +=1
        last -=1
        
    return a
        
print(rever(a))
