#Rotate array by one
a = [9, 8, 7, 6, 4, 2, 1, 3]

def rotate(a):
    last = a[-1]
    for i in range(len(a)-1,0,-1):
        a[i] = a[i-1]
    a[0] = last
    return a
print(rotate(a))


'''Output:
[3, 9, 8, 7, 6, 4, 2, 1]
'''
