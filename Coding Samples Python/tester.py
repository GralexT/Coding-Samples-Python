def zip(xs,ys):
    zs = []
    for i in range(len(xs)):
        zs.extend([xs[i],ys[i]])
    return zs

def cumulative(xs):
    zs = [xs[0]]
    for i in xs[1:]:
        zs.append(zs[-1]+i)
    return zs

def between(x,y):
    return [i for i in range(x,y+1) if i%x==0 if y%i==0]

def pairs(n):
    return [(x,y) for x in range(n) for y in range(x+1,n)]

def uncompress(xs):
    uncompList = []
    bool = True
    for x in xs:
        uncompList.extend([bool for i in range(x)])
        bool = not bool
    return uncompList

def palindrome(xs):
    for i in range(len(xs)//2):
        if xs[i] != xs[-i-1]:
            return False
    return True

def loseprefix(xs):
    while len(xs)>1 and xs[0] == xs[1]:
        xs = xs[1:]
    return xs[1:]

def flatten(x):
    out = []
    for i in x:
        print(i)

