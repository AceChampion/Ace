#global
num = 5
def func():
    global num
    num = 10
    print ('sth.')
print(num)

#closure
def funcX(x):
    def funcY(y):
        return x * y
    return funcY
func(5)(8)

#lambda
>>> p = lambda x : 2 * x + 1
>>> p(4)
9

#filter
>>> list(filter(lambda x : x % 2,range(10)))
[1, 3, 5, 7, 9]
>>> list(filter(lambda x : x > 5,range(10)))
[6, 7, 8, 9]
>>> 10 % 2
0

#map
>>> list(map(lambda x : 2 * x + 1,range(10)))
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

#Fibonacci self
def fibo(n):
    s = 1
    print(s)
    i = 0
    print(s)
    s1 = 2
    print(s1)
    for i in range(n):
    	s += s1
    	print(s)
    	s1 += s
    	print(s1)
    	i += 1
#Fibonacci better
def feb(n):
    if n < 1:
        print('wrong!')
        return -1
    if n == 1 or n == 2:
        return fab(n-1) + fab(n-2)
result = fab(9)
if result != -1:
    print('we have %d result:'% result)
