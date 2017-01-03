import math
def isprime():
    n = int(input('input a num:'))
    if n < 1:
    	return False
    for i in range (1,int(math.sqrt(n))+1):
        if n % i == 0:
            return False
        return True
    for i in range(0, 101):
        if isprime():
            print(i)

isprime()
