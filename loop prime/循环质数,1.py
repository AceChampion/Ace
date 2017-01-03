#基本思路是先用筛除法筛选出1，000，000以下质数，并转化为集合（为了快速验证元素是否为质数）
# 然后对集合内元素做迭代，对于每个元素按照该锁链法计算下一元素
# 若该元素不属于集合，则迭代下一元素若属于则计算下一元素直到与开头元素重合即构成一条链

from time import time

def primes_sieve(limit):
    limitn,not_prime,primes = limit+1,set(),list()
    for i in range(2, limitn):
        if i in not_prime:
            continue
        for f in range(i*2, limitn, i):
            not_prime.add(f)
        primes.append(i)
    return primes 
    
t = time()
i,d,prime_l = 0,1,primes_sieve(10**6)
prime_s = set(prime_l)

for item in prime_l:
    if 10*d < item:
        d *= 10   
    n_next,n_this = item//10 + (item%10)*d,item
    while n_next in prime_s:         
        n_next,n_this = n_this//10 + (n_this%10)*d,n_next
        if n_next == item:
            #print(n_next)
            i += 1
            break   
        
print(i,time()-t)
