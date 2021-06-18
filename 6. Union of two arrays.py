#Union and intersection of arrays
a = [1, 2,3,5]
b = [1,1,1,1,1,1,1,2,2,2,2,2, 2, 6,7]
'''
intersection = list(set(a) and set(b))
a.extend(b)
union = list(set(a))
print(intersection,union)
'''

temp = {}
for i in b:
    if i in temp:
        temp[i] += 1
    else:
        temp[i] = 1
for i in a:
    if i in temp:
        temp[i] += 1
    else:
        temp[i] = 1
    
print(len(temp))
