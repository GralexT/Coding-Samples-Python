def test():
    return all([True,True, 0])
    
def fits(b1, b2, x):
 if b1 and b2:
     return x == 2
 elif not(b1 or b2):
     return x == 0
 else:
     return x == 1
    
def test_fits():
 return all([fits(False, False, 0)
             ,fits(True, False, 1)
             ,fits(False, True, 1)
             ,fits(True, True, 2)
             ,not fits(False, False, 1)
             ,not fits(True, False, 0)
             ,not fits(False, True, 2)
             ,not fits(True, True, 1)
             ])

def zip(xs, ys):
    zs = []
    for k in range(len(xs)):
        zs.extend([xs[k],ys[k]])
    return zs

def cumulative(xs):
    cumsum = [xs[0]]
    for i in range(len(xs)-1):
        cumsum.append(cumsum[i]+xs[i+1])
    return cumsum

def between(x,y):
    return [k for k in range(x,y+1) if k%x == 0 if y%k == 0]

def pairs(x):
 return [(i, j) for i in range(x) for j in range(i+1,x)]

def test2(x):
    return x[-2]

def loseprefix(xs):
    while len(xs) > 1 and xs[0] == xs[1]:
        xs = xs[1:]
    return xs[1:]

