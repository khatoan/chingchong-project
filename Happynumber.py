def sumSquare(x):
    T = 0
    for i in str(x):
        T += (int(i)**2)
    return T
def HappyNumber(n):
    H = set() 
    while n != 1:
        n = sumSquare(n)
        if n in H: 
            return False  
        H.add(n) 
    return True
