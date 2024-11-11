def A(n:int): # Don't working with 10**9
    arr = [i for i in range(1,n+1)]
    def last_remain(arr, left_right = True):
        if len(arr)==1:
            return arr[0]
        if left_right == True:
            arr = arr[1::2]
        else: 
            arr = arr[::-1][1::2][::-1] 
        return last_remain(arr, left_right=not left_right)
    return last_remain(arr, left_right=True) 

def lastRemaining(n: int):
    if n is None or type(n) is not int or n<=0:
        print("Invalid parameter error")
        return
    head = 1
    step = 1
    left = True
    remaining = n

    while remaining > 1:
        if left or remaining %2 != 0:  
            head += step
        step *= 2
        remaining //= 2
        left = not left

    return head

    