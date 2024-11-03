modulo = 10**9 + 7

def power(a, b): # a: cơ số, b: mũ
	if (b == 0):
		return 1
	if (b % 2 == 0):
		return power((a*a)%modulo, b//2) 
	
	return (power((a*a)%modulo, b//2)*a)%modulo

def count_goodNumber(n):
    if n is None or type(n) is not int or n < 0:
        print("Invalid parameter")
        return 
    even_index = (n + 1) // 2  # Số vị trí chẵn
    odd_index = n // 2         # Số vị trí lẻ
    
    even_ways = power(5,even_index)  
    odd_ways = power(4, odd_index)
    
    return (even_ways * odd_ways) % modulo
