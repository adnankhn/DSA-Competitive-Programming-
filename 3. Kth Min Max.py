#Find Kth Smallest and largest element
a = [0,3,7,2,2,5,6,6]

def kth(a):
    k = int(input())
    a.sort()
    set(a)
    ksmallest = a[k]
    klargest = a[-k]
    return ksmallest,klargest
    
print(kth(a))
'''
Output:
    2
(2, 6)

