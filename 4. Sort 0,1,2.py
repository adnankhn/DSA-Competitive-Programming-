#Sort an array consisting of 0,1,2 without sort function
a = [0,1,2,1,1,1,2,2,0,0]

def zsort(a):
    zero = a.count(0)
    one = a.count(1)
    two = a.count(2)
    new = []
    new.extend([0]*zero)
    new.extend([1]*one)
    new.extend([2]*two)
    return new

print(zsort(a))

