import random

def getqk(n):
    n = n-1
    k = 1
    q = n
    while q == int(q):
        i = q
        q = n / 2**k
        k += 1

    return int(i), k-2
    

def mil(n):
    q, k = getqk(n)
    
    a = random.randrange(n-1)
    print("rand: ", a)
    if a**q % n == n-1:
        return "inconclusive"
    
    for j in range(0, k-1):
        if a**2**j % n == n-1:
            return "inconclusive"
    
    return "composite"
    
print(mil(53))
