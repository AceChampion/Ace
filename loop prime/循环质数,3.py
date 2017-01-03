#from BAIDU
import time
start=time.time()
def euler35(limit):
    def isprimesieve(n):
        sieve = bytearray([1])*(n+1)
        sieve[0] = sieve[1] = 0
        for p in range(2, int(n**0.5) + 1):
            if sieve[p]:
                m = n//p - p + 1
                sieve[p*p::p] = bytearray(m)
        return sieve

    def rotations(s):
        for n in range(len(s)): yield s[n:] + s[:n]

    count = 0; isprime = isprimesieve(limit); unwanted = '024568'
    for n, prime in enumerate(isprime):
        if prime:
            s = str(n)
            if any(c in s for c in unwanted): continue
            if all(isprime[int(r)] for r in rotations(s)):
                count += 1
    return count + 2
print(euler35(1000000),time.time()-start)